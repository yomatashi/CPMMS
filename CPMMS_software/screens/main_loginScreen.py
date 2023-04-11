from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from UI.loginScreen_ui import Ui_MainWindow
from DB.connectionDB import FirebaseAuthentication, FirebaseAccessor, FirebaseMutator
from screens.widget_memberVerificationScreen import WidgetMemberVerificationScreen

class MainWindowLoginScreen(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowLoginScreen, self).__init__(parent=parent)
        self.setupUi(self)
        self.widgetApp = WidgetMemberVerificationScreen()
        self.lbl_goSignUp.linkHovered.connect(self.clearSignup)
        self.lbl_goSignUp.linkActivated.connect(lambda: self.stackedWidget.setCurrentWidget(self.signup))
        self.lbl_goLogin.linkHovered.connect(self.clearLogin)
        self.lbl_goLogin.linkActivated.connect(lambda: self.stackedWidget.setCurrentWidget(self.login))
    
        # Login screen
        self.input_username.setPlaceholderText("Email")
        self.input_password.setPlaceholderText("Password")
        self.btn_login.clicked.connect(self.validateLogin)

        # Signup screen
        self.jobpos = "Pharmacist"
        self.input_username_2.setPlaceholderText("Email")
        regex = QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        validator = QRegularExpressionValidator(regex)
        self.input_username_2.setValidator(validator)
        self.input_password_2.setPlaceholderText("Password")
        regexpw = QRegularExpression(".{7,}")
        validatorpw = QRegularExpressionValidator(regexpw)
        self.input_password_2.setValidator(validatorpw)
        self.input_fullName.setPlaceholderText("Full Name")
        # self.input_jobPosition.setPlaceholderText("Job Position")
        self.btn_signup.clicked.connect(self.createAcc)

    def clearLogin(self):
        self.input_username.setText("")
        self.input_password.setText("")
        self.lbl_err_msg.setText("")
    
    def clearSignup(self):
        self.input_username_2.setText("")
        self.input_password_2.setText("")
        self.input_fullName.setText("")
        self.lbl_err_msg_email_exist.setText("")
        self.lbl_err_msg_email_exist.setMaximumHeight(0)
        self.lbl_err_msg_empty.setText("")
        self.lbl_err_msg_empty.setMaximumHeight(0)
        self.lbl_err_msg_pw.setMaximumHeight(0)
        self.lbl_err_msg_pw.setText("")
    
    def clearErrMsg(self):
        self.lbl_err_msg_empty.setMaximumHeight(0)
        self.lbl_err_msg_empty.setText("")
        self.lbl_err_msg_email_exist.setMaximumHeight(0)
        self.lbl_err_msg_email_exist.setText("")
        self.lbl_err_msg_pw.setMaximumHeight(0)
        self.lbl_err_msg_pw.setText("")

    def set_jobpos(self, text):
        self.jobpos = text

    def validateLogin(self):
        email = self.input_username.text()
        password = self.input_password.text()
        tryLogin = FirebaseAuthentication.login(email, password)
        if tryLogin == "Pass":
            get_admin = FirebaseAccessor('Admin').read_all()
            for admin in get_admin:
                if admin['email'] == email:
                    self.widgetApp.updateLabel(admin)
                    self.setCentralWidget(self.widgetApp)
                    break
                else:
                    self.lbl_err_msg.setText("The email used is not a staff member")
        else:
            self.lbl_err_msg.setText(tryLogin)

    def createAcc(self):
        email = self.input_username_2.text()
        password = self.input_password_2.text()
        fullname = self.input_fullName.text()
        jobPos = self.input_jobPosition.currentText()
        tryRegister = FirebaseAuthentication.register(email, password)
        if not all([email, password, fullname, jobPos]):
            self.clearErrMsg()
            self.lbl_err_msg_empty.setMaximumHeight(25)
            self.lbl_err_msg_empty.setText("Please fill in the empty field(s)")
        elif not self.input_username_2.hasAcceptableInput():
            self.clearErrMsg()
            self.lbl_err_msg_email_exist.setMaximumHeight(25)
            self.lbl_err_msg_email_exist.setText("Invalid email address")
        elif not self.input_password_2.hasAcceptableInput():
            self.clearErrMsg()
            self.lbl_err_msg_pw.setMaximumHeight(25)
            self.lbl_err_msg_pw.setText("Password must have at least 7 character")
        else:
            if tryRegister == "Pass":
                self.clearErrMsg()
                Admin = FirebaseMutator('Admin')
                counter = FirebaseAccessor('counter').read("indices")
                counterUpdate = FirebaseMutator('counter')

                Admindata = {'email': email, 'fullName': fullname, 'position': jobPos}
                Admin.create(Admindata, "staf" + str(counter['staf']+1))
                counterUpdate.update("indices", {'staf': counter['staf']+1})

                ret = QMessageBox.information(self, "Success", "Your account has successfully created!\nPlease login.", QMessageBox.Ok)
                if ret == QMessageBox.Ok:
                    self.stackedWidget.setCurrentWidget(self.login)
            else:
                self.clearErrMsg()
                self.lbl_err_msg_email_exist.setMaximumHeight(25)
                self.lbl_err_msg_email_exist.setText(tryRegister)