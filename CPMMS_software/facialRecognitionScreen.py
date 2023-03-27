from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtCore import Slot, QDate, QTimer, QThread, Signal, Qt
from ui_memberVerificationVideo import Ui_OutputDialog
import cv2
import face_recognition
import datetime
import os
import numpy as np
import time
import sys

import resources_rc

class Thread(QThread):
    updateFrame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True

    def set_file(self, fname):
        # The data comes with the 'opencv-python' module
        self.trained_file = os.path.join(cv2.data.haarcascades, fname)

    def set_camera_index(self, camera_index):
        self.cam_index = int(camera_index)

    def run(self):
        self.cap = cv2.VideoCapture(self.cam_index)
        while self.status:
            # cascade = cv2.CascadeClassifier(self.trained_file)
            ret, frame = self.cap.read()
            if not ret:
                continue

            # Reading frame in gray scale to process the pattern
            # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # detections = cascade.detectMultiScale(gray_frame, scaleFactor=1.1,
            #                                       minNeighbors=5, minSize=(30, 30))

            # Drawing green rectangle around the pattern
            # for (x, y, w, h) in detections:
            #     pos_ori = (x, y)
            #     pos_end = (x + w, y + h)
            #     color = (0, 255, 0)
            #     cv2.rectangle(frame, pos_ori, pos_end, color, 2)

            # Reading the image in RGB to display it
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Creating and scaling QImage
            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)

class facialRecog(QDialog, Ui_OutputDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Facial Recognition App CPMMS")
        
        # Thread in charge of updating the image
        self.th = Thread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)
        self.btn_verify.clicked.connect(self.verify_membership)

    def closeEvent(self, event):
    #   print("X is clicked")
        print("Closing camera...")
        self.th.cap.release()
        cv2.destroyAllWindows()
        self.status = False
        self.th.terminate()
        # Give time for the thread to finish
        time.sleep(1)

    @Slot()
    def verify_membership():
        print("Verify button is clicked")

    @Slot()
    def startVideo(self, camera_name):
        self.th.start()
        self.th.set_camera_index(camera_name)

    @Slot(QImage)
    def setImage(self, image):
        self.imgLabel.setPixmap(QPixmap.fromImage(image))




    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
    #     self.setWindowTitle("Facial Recognition App CPMMS")

    #     #Update time
    #     now = QDate.currentDate()
    #     current_date = now.toString('ddd dd MMMM yyyy')
    #     current_time = datetime.datetime.now().strftime("%I:%M %p")
    #     self.Date_Label.setText(current_date)
    #     self.Time_Label.setText(current_time)

    #     self.image = None
    
    # @Slot()
    # def startVideo(self, camera_name):
    #     """
    #     :param camera_name: link of camera or usb camera
    #     :return:
    #     """
        # if len(camera_name) == 1:
    #         self.capture = cv2.VideoCapture(int(camera_name))
    #     else:
    #         self.capture = cv2.VideoCapture(camera_name)
    #     self.timer = QTimer(self)  # Create Timer
    #     path = 'ImagesMembers'
    #     if not os.path.exists(path):
    #         os.mkdir(path)
    #     # known face encoding and known face name list
    #     images = []
    #     self.class_names = []
    #     self.encode_list = []
    #     self.TimeList1 = []
    #     self.TimeList2 = []
    #     member_list = os.listdir(path)

    #     for cl in member_list:
    #         cur_img = cv2.imread(f'{path}/{cl}')
    #         images.append(cur_img)
    #         self.class_names.append(os.path.splitext(cl)[0])
    #     for img in images:
    #         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #         boxes = face_recognition.face_locations(img)
    #         encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
    #         # encode = face_recognition.face_encodings(img)[0]
    #         self.encode_list.append(encodes_cur_frame)
    #     # self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
    #     # self.timer.start(10)  # emit the timeout() signal at x=10ms
    #     self.update_frame()

    # def face_rec_(self, frame, encode_list_known, class_names):
    #     """
    #     :param frame: frame from camera
    #     :param encode_list_known: known face encoding
    #     :param class_names: known face names
    #     :return:
    #     """

    #     def mark_attendance(name):
    #         """
    #         :param name: detected face known or unknown one
    #         :return:
    #         """
    #         if self.btn_verify.isChecked():
    #             print("clicked!")
    #             self.capture.release()
    #             cv2.destroyAllWindows()
    #             self.sv = facialRecog(self)
    #             self.sv.terminate()
    #             time.sleep(1)
            
    #     # face recognition
    #     faces_cur_frame = face_recognition.face_locations(frame)
    #     encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
    #     # count = 0
    #     for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
    #         match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
    #         face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
    #         name = "unknown"
    #         best_match_index = np.argmin(face_dis)
    #         # print("s",best_match_index)
    #         if match[best_match_index]:
    #             name = class_names[best_match_index].upper()
    #             y1, x2, y2, x1 = faceLoc
    #             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #             cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
    #             cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
    #             self.NameLabel.setText(name)
    #         mark_attendance(name)

    #     return frame
    
    # def update_frame(self):
    #     ret, self.image = self.capture.read()
    #     self.displayImage(self.image, self.encode_list, self.class_names, 1)

    # def displayImage(self, image, encode_list, class_names, window=1):
    #     """
    #     :param image: frame from camera
    #     :param encode_list: known face encoding list
    #     :param class_names: known face names
    #     :param window: number of window
    #     :return:
    #     """
    #     image = cv2.resize(image, (640, 480))
    #     try:
    #         image = self.face_rec_(image, encode_list, class_names)
    #     except Exception as e:
    #         print(e)
    #     qformat = QImage.Format_Indexed8
    #     if len(image.shape) == 3:
    #         if image.shape[2] == 4:
    #             qformat = QImage.Format_RGBA8888
    #         else:
    #             qformat = QImage.Format_RGB888
    #     outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
    #     outImage = outImage.rgbSwapped()

    #     if window == 1:
    #         self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
    #         self.imgLabel.setScaledContents(True)