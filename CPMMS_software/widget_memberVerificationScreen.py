from PySide6.QtWidgets import QWidget, QDialog
# from PySide6.QtGui import QIcon
from ui_memberVerificationScreen import Ui_Form
from facialRecognitionScreen  import facialRecog
from PySide6.QtCore import QTimer, QDate
import datetime

class WidgetMemberVerificationScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_member_verification.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.verificationMethod))
        self.btn_ic.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ICMethod))
        self.btn_facial_recog.clicked.connect(self.openFacialRecognitionProgram)

        self.facial_recog = facialRecog()
        self.Videocapture_ = "0"

        timer  = QTimer(self)
        timer.timeout.connect(self.TimeDate)
        timer.start(1000)
    
    def TimeDate(self):
        #Update time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

    def openFacialRecognitionProgram(self):
        ret = self.facial_recog.show()
        self.facial_recog.startVideo(self.Videocapture_)
        if(ret == QDialog.Accepted):
            print("Dialog accepted")
        else:
            print("Dialog rejected")