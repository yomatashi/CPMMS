# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import os
from pathlib import Path

from PySide6.QtMultimedia import (QAudioInput, QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices, QMediaMetaData,
                                  QMediaRecorder)
from PySide6.QtWidgets import QDialog, QMainWindow, QMessageBox
from PySide6.QtGui import QAction, QActionGroup, QIcon, QImage, QPixmap
from PySide6.QtCore import QDateTime, QDir, QTimer, Qt, Slot

from UI.cam_UI.camera_ui import Ui_Camera
from UI.cam_UI.imagesettings import ImageSettings


class Camera(QMainWindow):
    def __init__(self):
        super().__init__()

        self._video_devices_group = None

        self.m_devices = QMediaDevices()
        self.m_imageCapture = None
        self.m_captureSession = QMediaCaptureSession()
        self.m_camera = None

        self.m_isCapturingImage = False
        self.m_applicationExiting = False
        self.m_doImageCapture = True

        self.m_metaDataDialog = None

        self._ui = Ui_Camera()
        self._ui.setupUi(self)
        image = Path(__file__).parent / "shutter.svg"
        self._ui.takeImageButton.setIcon(QIcon(os.fspath(image)))

        # disable all buttons by default
        self.updateCameraActive(False)
        self.readyForCapture(False)

    @Slot()
    def openCameraReg(self):
        # try to actually initialize camera
        self._video_devices_group = QActionGroup(self)
        self._video_devices_group.setExclusive(True)
        self.updateCameras()
        self.m_devices.videoInputsChanged.connect(self.updateCameras)

        self._video_devices_group.triggered.connect(self.updateCameraDevice)
        self._ui.captureWidget.currentChanged.connect(self.updateCaptureMode)

        self._ui.exposureCompensation.valueChanged.connect(self.setExposureCompensation)

        self.setCamera(QMediaDevices.defaultVideoInput())

    @Slot(QCameraDevice)
    def setCamera(self, cameraDevice):
        self.m_camera = QCamera(cameraDevice)
        self.m_captureSession.setCamera(self.m_camera)

        self.m_camera.activeChanged.connect(self.updateCameraActive)
        self.m_camera.errorOccurred.connect(self.displayCameraError)

        if not self.m_imageCapture:
            self.m_imageCapture = QImageCapture()
            self.m_captureSession.setImageCapture(self.m_imageCapture)
            self.m_imageCapture.readyForCaptureChanged.connect(self.readyForCapture)
            self.m_imageCapture.imageCaptured.connect(self.processCapturedImage)
            self.m_imageCapture.imageSaved.connect(self.imageSaved)
            self.m_imageCapture.errorOccurred.connect(self.displayCaptureError)

        self.m_captureSession.setVideoOutput(self._ui.viewfinder)

        self.updateCameraActive(self.m_camera.isActive())
        self.readyForCapture(self.m_imageCapture.isReadyForCapture())

        self.updateCaptureMode()

        self.m_camera.start()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key_CameraFocus:
            self.displayViewfinder()
            event.accept()
        elif key == Qt.Key_Camera:
            if self.m_doImageCapture:
                self.takeImage()

            event.accept()
        else:
            super().keyPressEvent(event)

    @Slot(int, QImage)
    def processCapturedImage(self, requestId, img):
        scaled_image = img.scaled(self._ui.viewfinder.size(), Qt.KeepAspectRatio,
                                  Qt.SmoothTransformation)

        self._ui.lastImagePreviewLabel.setPixmap(QPixmap.fromImage(scaled_image))

        # Display captured image for 4 seconds.
        self.displayCapturedImage()
        QTimer.singleShot(4000, self.displayViewfinder)

    @Slot()
    def configureCaptureSettings(self):
        if self.m_doImageCapture:
            self.configureImageSettings()
        else:
            self.configureVideoSettings()

    @Slot()
    def configureImageSettings(self):
        settings_dialog = ImageSettings(self.m_imageCapture)

        if settings_dialog.exec():
            settings_dialog.apply_image_settings()

    @Slot(bool)
    def setMuted(self, muted):
        self.m_captureSession.audioInput().setMuted(muted)

    @Slot()
    def takeImage(self):
        self.m_isCapturingImage = True
        self.m_imageCapture.captureToFile()

    @Slot(int, QImageCapture.Error, str)
    def displayCaptureError(self, id, error, errorString):
        QMessageBox.warning(self, "Image Capture Error", errorString)
        self.m_isCapturingImage = False

    @Slot()
    def startCamera(self):
        self.m_camera.start()

    @Slot()
    def stopCamera(self):
        self.m_camera.stop()

    @Slot()
    def updateCaptureMode(self):
        tab_index = self._ui.captureWidget.currentIndex()
        self.m_doImageCapture = (tab_index == 0)

    @Slot(bool)
    def updateCameraActive(self, active):
        if active:
            self._ui.actionStartCamera.setEnabled(False)
            self._ui.actionStopCamera.setEnabled(True)
            self._ui.captureWidget.setEnabled(True)
            self._ui.actionSettings.setEnabled(True)
        else:
            self._ui.actionStartCamera.setEnabled(True)
            self._ui.actionStopCamera.setEnabled(False)
            self._ui.captureWidget.setEnabled(False)
            self._ui.actionSettings.setEnabled(False)

    @Slot(int)
    def setExposureCompensation(self, index):
        self.m_camera.setExposureCompensation(index * 0.5)

    @Slot()
    def displayCameraError(self):
        if self.m_camera.error() != QCamera.NoError:
            QMessageBox.warning(self, "Camera Error",
                                self.m_camera.errorString())

    @Slot(QAction)
    def updateCameraDevice(self, action):
        self.setCamera(QMediaDevices(action))

    @Slot()
    def displayViewfinder(self):
        self._ui.stackedWidget.setCurrentIndex(0)

    @Slot()
    def displayCapturedImage(self):
        self._ui.stackedWidget.setCurrentIndex(1)

    @Slot(bool)
    def readyForCapture(self, ready):
        self._ui.takeImageButton.setEnabled(ready)

    @Slot(int, str)
    def imageSaved(self, id, fileName):
        f = QDir.toNativeSeparators(fileName)
        self._ui.statusbar.showMessage(f"Captured \"{f}\"")

        self.m_isCapturingImage = False
        if self.m_applicationExiting:
            self.close()

    def closeEvent(self, event):
        self.m_camera.stop()
        if self.m_isCapturingImage:
            self.setEnabled(False)
            self.m_applicationExiting = True
            event.ignore()
        else:
            event.accept()

    @Slot()
    def updateCameras(self):
        self._ui.menuDevices.clear()
        available_cameras = QMediaDevices.videoInputs()
        for cameraDevice in available_cameras:
            video_device_action = QAction(cameraDevice.description(),
                                          self._video_devices_group)
            video_device_action.setCheckable(True)
            video_device_action.setData(cameraDevice)
            if cameraDevice == QMediaDevices.defaultVideoInput():
                video_device_action.setChecked(True)

            self._ui.menuDevices.addAction(video_device_action)
