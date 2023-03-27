from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot, QDate, QThread, Signal, Qt, QTimer
from ui_memberVerificationVideo import Ui_OutputDialog
import cv2
import face_recognition
import datetime
import os
import numpy as np
import time
import sys

class Thread(QThread):
    updateFrame = Signal(QImage)
    updateName = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True

    def set_camera_index(self, camera_index):
        self.cam_index = int(camera_index)

    def run(self):

        path = 'ImagesMembers'
        if not os.path.exists(path):
            os.mkdir(path)
        # known face encoding and known face name list
        images = []
        self.class_names = []
        self.encode_list = []
        members_list = os.listdir(path)

        for cl in members_list:
            cur_img = cv2.imread(f'{path}/{cl}')
            images.append(cur_img)
            self.class_names.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            self.encode_list.append(encodes_cur_frame)

        self.cap = cv2.VideoCapture(self.cam_index)
        while self.status:

            ret, frame = self.cap.read()

            try:
                # face recognition
                faces_cur_frame = face_recognition.face_locations(frame)
                encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)
                # count = 0
                for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
                    match = face_recognition.compare_faces(self.encode_list, encodeFace, tolerance=0.50)
                    face_dis = face_recognition.face_distance(self.encode_list, encodeFace)
                    # name = "unknown"
                    best_match_index = np.argmin(face_dis)
                    if match[best_match_index]:
                        name = self.class_names[best_match_index].upper()
                        y1, x2, y2, x1 = faceLoc
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    self.updateName.emit(name)
            except Exception as e:
                print(e)

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Creating and scaling QImage
            h, w, ch = color_frame.shape
            img = QImage(color_frame, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            # Emit signal
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)

class facialRecog(QDialog, Ui_OutputDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Facial Recognition App CPMMS")

        timer  = QTimer(self)
        timer.timeout.connect(self.TimeDate)
        timer.start(1000)
        
        # Thread in charge of updating the image
        self.th = Thread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)
        self.th.updateName.connect(self.setName)
        self.btn_verify.clicked.connect(self.verify_membership)

    def TimeDate(self):
        #Update time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

    def closeEvent(self, event):
        print("Closing camera...")
        self.th.cap.release()
        cv2.destroyAllWindows()
        self.status = False
        self.th.terminate()
        # Give time for the thread to finish
        time.sleep(1)

    @Slot()
    def verify_membership():
        print("Verify member button is clicked")

    @Slot()
    def startVideo(self, camera_name):
        print("Starting camera...")
        self.th.start()
        self.th.set_camera_index(camera_name)

    @Slot(str)
    def setName(self, name):
        self.NameLabel.setText(name)

    @Slot(QImage)
    def setImage(self, image):
        self.imgLabel.setPixmap(QPixmap.fromImage(image))
        # self.imgLabel.setScaledContents(True)
    