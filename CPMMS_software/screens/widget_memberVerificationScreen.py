from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtGui import QRegularExpressionValidator
from ui.ui_memberVerificationScreen import Ui_Form
from screens.facialRecognitionScreen  import facialRecog
from PySide6.QtCore import QTimer, QDate, QRegularExpression
import datetime

class WidgetMemberVerificationScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_member_verification.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.verificationMethod))
        self.btn_ic.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ICMethod))
        self.btn_facial_recog.clicked.connect(self.openFacialRecognitionProgram)

        # IC number method
        self.input_ICNum.setPlaceholderText("Insert IC number here...")
        regex = QRegularExpression("[0-9]{12}")
        validator = QRegularExpressionValidator(regex)
        self.input_ICNum.setValidator(validator)

        # facial recognition method
        self.facial_recog = facialRecog()
        self.Videocapture_ = "0"
        self.cam_input.currentTextChanged.connect(self.set_camera)

        # date-time 
        timer  = QTimer(self)
        timer.timeout.connect(self.TimeDate)
        timer.start(1000)
    
    def set_camera(self, text):
        if text == "External Camera (USB)":
            self.Videocapture_ = "1"
        else:
            self.Videocapture_ = "0"

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