from PySide6 import QtWidgets
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
        self.input_username_2.setPlaceholderText("Email")
        self.input_password_2.setPlaceholderText("Password")
        self.input_fullName.setPlaceholderText("Full Name")
        self.input_jobPosition.setPlaceholderText("Job Position")
        self.btn_signup.clicked.connect(self.createAcc)

    def clearLogin(self):
        self.input_username.setText("")
        self.input_password.setText("")
        self.lbl_err_msg.setText("")
    
    def clearSignup(self):
        self.input_username_2.setText("")
        self.input_password_2.setText("")
        self.input_fullName.setText("")
        self.input_jobPosition.setText("")
        self.lbl_err_msg_email_exist.setText("")
        self.lbl_err_msg_email_exist.setMaximumHeight(0)
        self.lbl_err_msg_empty.setText("")
        self.lbl_err_msg_empty.setMaximumHeight(0)

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
        jobPos = self.input_jobPosition.text()
        tryRegister = FirebaseAuthentication.register(email, password)
        if not all([email, password, fullname, jobPos]):
            self.lbl_err_msg_empty.setMaximumHeight(25)
            self.lbl_err_msg_empty.setText("Please fill in the empty field(s)")
            # tmbah lgi 1 validation for email field pstikan it is @email.com
            # klo rajin buatkn utk password gak
        else:
            if tryRegister == "Pass":
                print("account created successfully")
                Admin = FirebaseMutator('Admin')
                counter = FirebaseAccessor('counter').read("indices")
                counterUpdate = FirebaseMutator('counter')

                Admindata = {'email': email, 'fullName': fullname, 'position': jobPos}
                Admin.create(Admindata, "staf" + str(counter['staf']+1))
                counterUpdate.update("indices", {'staf': counter['staf']+1})
                # pstu sni ltk popup ckp account created pstu suh gi login page
            else:
                self.lbl_err_msg_email_exist.setMaximumHeight(25)
                self.lbl_err_msg_email_exist.setText(tryRegister)