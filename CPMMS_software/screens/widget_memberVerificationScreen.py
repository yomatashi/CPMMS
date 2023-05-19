from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Slot
from UI.memberVerificationScreen_ui import Ui_Form
from screens.facialRecognitionScreen  import facialRecog
from PySide6.QtCore import QTimer, QDate, QRegularExpression
from DB.connectionDB import FirebaseAccessor
import datetime
import sys
import screens.widget_memberManagerScreen as mem_manager
from screens.cameraCaptureScreen import Camera

class WidgetMemberVerificationScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # date-time 
        timer  = QTimer(self)
        timer.timeout.connect(self.TimeDate)
        timer.start(1000)

        # ---Member Verification Screen---
        self.btn_member_verification.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.verificationMethod))
        self.btn_ic.clicked.connect(self.ICmethodscreen)
        self.btn_facial_recog.clicked.connect(self.openFacialRecognitionProgram)
        self.btn_signout.clicked.connect(sys.exit)

        # IC number method
        self.input_ICNum.setPlaceholderText("Insert IC number here...")
        regex = QRegularExpression("[0-9]{12}")
        validator = QRegularExpressionValidator(regex)
        self.input_ICNum.setValidator(validator)
        self.btn_verify.clicked.connect(self.check_members)

        # facial recognition method
        self.facial_recog = facialRecog()
        self.Videocapture_ = "0"
        self.cam_input.currentTextChanged.connect(self.set_camera)

        # ---Member Manager Screen---
        self.btn_member_manager.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.memberManager))
        self.btn_addMember.clicked.connect(lambda: mem_manager.AddMemberScreen(self))
        self.btn_listMember.clicked.connect(lambda: mem_manager.ListMemberScreen(self))
        self.btn_browse.clicked.connect(lambda: mem_manager.browseFile(self))
        self.btn_cam.clicked.connect(self.openCameraCapture)
        self.btn_registerMem.clicked.connect(lambda: mem_manager.registerNewMember(self))
        self.cam_screen = Camera()

    def openCameraCapture(self):
        self.cam_screen.exec()

    def ICmethodscreen(self):
        self.lbl_error_msg.setText("")
        self.input_ICNum.setText("")
        self.stackedWidget.setCurrentWidget(self.ICMethod)
    
    def check_members(self):
        value = self.input_ICNum.text()
        get_members = FirebaseAccessor('Member').read_all()
        has_member = 0
        for member in get_members:
            if member['IC'] == value:
                has_member = 1
                self.member_data = member
                break
        if has_member == 0:
            self.lbl_error_msg.setText("No member found!")
        else:
            self.lbl_error_msg.setText("")
            message = "Name: "+ self.member_data['fullName'] + "\nIC number: " + self.member_data['IC'] + "\nPoints: " + str(self.member_data['points']) + "\n\nSet this member for checkout process?"
            ret = QMessageBox.information(self, "Member information", message, QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                print("User chose Yes")
            else:
                print("User chose No")

    def set_camera(self, text):
        if text == "External Camera (USB)":
            self.Videocapture_ = "1"
        else:
            self.Videocapture_ = "0"

    def TimeDate(self):
        # Update time
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

    def openFacialRecognitionProgram(self):
        self.facial_recog.resetLabel()
        self.facial_recog.startVideo(self.Videocapture_)
        self.facial_recog.exec()

    @Slot()
    def updateLabel(self, admin):
        # Update user information on screen
        self.name_label.setText(admin['fullName'])
        self.position_label.setText(admin['position'])