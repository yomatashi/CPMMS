from PySide6.QtWidgets import QWidget, QMessageBox, QDialog
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Slot
from UI.memberVerificationScreen_ui import Ui_Form
from screens.facialRecognitionScreen  import facialRecog
from PySide6.QtCore import QTimer, QDate, QRegularExpression
from DB.connectionDB import FirebaseAccessor
import datetime
import sys
import screens.widget_memberManagerScreen as mem_manager
import screens.widget_adminProfileScreen as admin_profile
import screens.widget_checkoutScreen as checkout
from screens.cameraCaptureScreen import Camera
from screens.addItemScreen import TextInputDialog

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
        self.btn_browse.clicked.connect(lambda: mem_manager.browseFile(self))
        self.cam_screen = Camera()
        self.btn_cam.clicked.connect(self.openCameraCapture)
        self.btn_registerMem.clicked.connect(lambda: mem_manager.registerNewMember(self))

        # List members
        self.btn_listMember.clicked.connect(lambda: mem_manager.ListMemberScreen(self))
        self.btn_searchMem.clicked.connect(lambda: mem_manager.searchMem(self))
        self.btn_refreshMem.clicked.connect(lambda: mem_manager.ListMemberScreen(self))
        self.tbl_memList.doubleClicked.connect(lambda: mem_manager.show_member_details(self))
        self.btn_back.clicked.connect(lambda: mem_manager.ListMemberScreen(self))
        self.btn_deleteMemEdit.clicked.connect(lambda: mem_manager.delete_member(self))
        self.btn_updateMemEdit.clicked.connect(lambda: mem_manager.update_member(self))

        # ---Admin Profile Screen---
        self.btn_edit_profile.clicked.connect(lambda: admin_profile.editProfile(self))
        self.btn_updateAdmin.clicked.connect(lambda: admin_profile.updateProfile(self))

        # ---Checkout Screen---
        self.btn_checkout.clicked.connect(lambda: checkout.checkoutScreen(self))
        # self.btn_additem.clicked.connect(lambda: checkout.addItem(self))
        self.btn_additem.clicked.connect(self.openTextInputWindow)
        self.wadditem = TextInputDialog()

    # ---Member Verification Screen---
    def ICmethodscreen(self):
        self.lbl_error_msg.setText("")
        self.input_ICNum.setText("")
        self.stackedWidget.setCurrentWidget(self.ICMethod)
    
    def check_members(self):
        value = self.input_ICNum.text()
        get_members = FirebaseAccessor('Member').read_all_with_id()
        has_member = 0
        for member in get_members:
            if member['data']['IC'] == value:
                has_member = 1
                self.member_data = member['data']
                self.member_id = member['id']
                break
        if has_member == 0:
            self.lbl_error_msg.setText("No member found!")
        else:
            self.lbl_error_msg.setText("")
            message = "Name: "+ self.member_data['fullName'] + "\nIC number: " + self.member_data['IC'] + "\nPoints: " + str(self.member_data['points']) + "\n\nSet this member for checkout process?"
            ret = QMessageBox.information(self, "Member information", message, QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.lbl_currentMem.setText(self.member_id)
                checkout.checkoutScreen(self)
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
        ret = self.facial_recog.exec()
        if ret == QDialog.Accepted:
            self.lbl_currentMem.setText(self.facial_recog.memID)
            checkout.checkoutScreen(self)

    @Slot()
    def updateLabel(self, admin):
        # Update user information on screen
        self.name_label.setText(admin['fullName'])
        self.position_label.setText(admin['position'])

    # ---Member Manager Screen---
    def openCameraCapture(self):
        self.cam_screen.openCameraReg()
        self.cam_screen.show()

    # ---Checkout Screen---
    def openTextInputWindow(self):
        self.wadditem.reset()
        ret = self.wadditem.exec()
        if ret == QDialog.Accepted:
            checkout.addItem(self, self.wadditem.item_data) 