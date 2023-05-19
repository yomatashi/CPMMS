# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 739)
        MainWindow.setMinimumSize(QSize(1020, 600))
        icon = QIcon()
        icon.addFile(u":/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout_4 = QGridLayout(self.login)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.login)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(340, 440))
        self.frame_4.setSizeIncrement(QSize(0, 0))
        self.frame_4.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.lbl_err_msg = QLabel(self.frame_4)
        self.lbl_err_msg.setObjectName(u"lbl_err_msg")
        self.lbl_err_msg.setMaximumSize(QSize(16777215, 30))
        self.lbl_err_msg.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.gridLayout_2.addWidget(self.lbl_err_msg, 6, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 70))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_login = QPushButton(self.frame_6)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setPointSize(11)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.btn_login, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_6, 7, 0, 1, 1)

        self.lbl_goSignUp = QLabel(self.frame_4)
        self.lbl_goSignUp.setObjectName(u"lbl_goSignUp")
        self.lbl_goSignUp.setMaximumSize(QSize(16777215, 30))
        self.lbl_goSignUp.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_goSignUp, 8, 0, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.input_username = QLineEdit(self.frame_4)
        self.input_username.setObjectName(u"input_username")
        self.input_username.setMinimumSize(QSize(0, 0))
        self.input_username.setMaximumSize(QSize(16777215, 35))
        self.input_username.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.input_username.setEchoMode(QLineEdit.Normal)

        self.gridLayout_2.addWidget(self.input_username, 2, 0, 1, 1)

        self.input_password = QLineEdit(self.frame_4)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMinimumSize(QSize(0, 0))
        self.input_password.setMaximumSize(QSize(16777215, 35))
        self.input_password.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.input_password, 5, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 3)

        self.frame_3 = QFrame(self.login)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_5 = QFrame(self.login)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_4.addWidget(self.frame_5, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.login)
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.gridLayout_6 = QGridLayout(self.signup)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.signup)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(340, 440))
        self.frame_10.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_5)

        self.input_username_2 = QLineEdit(self.frame_10)
        self.input_username_2.setObjectName(u"input_username_2")
        self.input_username_2.setMaximumSize(QSize(16777215, 35))
        self.input_username_2.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.input_username_2)

        self.lbl_err_msg_email_exist = QLabel(self.frame_10)
        self.lbl_err_msg_email_exist.setObjectName(u"lbl_err_msg_email_exist")
        self.lbl_err_msg_email_exist.setMaximumSize(QSize(16777215, 0))
        self.lbl_err_msg_email_exist.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.lbl_err_msg_email_exist)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_6)

        self.input_password_2 = QLineEdit(self.frame_10)
        self.input_password_2.setObjectName(u"input_password_2")
        self.input_password_2.setMaximumSize(QSize(16777215, 35))
        self.input_password_2.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.input_password_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.input_password_2)

        self.lbl_err_msg_pw = QLabel(self.frame_10)
        self.lbl_err_msg_pw.setObjectName(u"lbl_err_msg_pw")
        self.lbl_err_msg_pw.setMaximumSize(QSize(16777215, 0))
        self.lbl_err_msg_pw.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.lbl_err_msg_pw)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_7)

        self.input_fullName = QLineEdit(self.frame_10)
        self.input_fullName.setObjectName(u"input_fullName")
        self.input_fullName.setMaximumSize(QSize(16777215, 35))
        self.input_fullName.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.input_fullName)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_8)

        self.input_jobPosition = QComboBox(self.frame_10)
        self.input_jobPosition.addItem("")
        self.input_jobPosition.addItem("")
        self.input_jobPosition.addItem("")
        self.input_jobPosition.setObjectName(u"input_jobPosition")
        self.input_jobPosition.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setPointSize(12)
        self.input_jobPosition.setFont(font1)
        self.input_jobPosition.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.input_jobPosition)

        self.lbl_err_msg_empty = QLabel(self.frame_10)
        self.lbl_err_msg_empty.setObjectName(u"lbl_err_msg_empty")
        self.lbl_err_msg_empty.setMaximumSize(QSize(16777215, 0))
        self.lbl_err_msg_empty.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.verticalLayout.addWidget(self.lbl_err_msg_empty)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.btn_signup = QPushButton(self.frame_11)
        self.btn_signup.setObjectName(u"btn_signup")
        self.btn_signup.setMaximumSize(QSize(150, 50))
        self.btn_signup.setFont(font)
        self.btn_signup.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_signup.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_5.addWidget(self.btn_signup, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_11)

        self.lbl_goLogin = QLabel(self.frame_10)
        self.lbl_goLogin.setObjectName(u"lbl_goLogin")
        self.lbl_goLogin.setMaximumSize(QSize(16777215, 30))
        self.lbl_goLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_goLogin)


        self.gridLayout_6.addWidget(self.frame_10, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.signup)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_7, 0, 0, 1, 3)

        self.frame_9 = QFrame(self.signup)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_9, 1, 2, 1, 1)

        self.frame_8 = QFrame(self.signup)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.signup)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_12, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.signup)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CPMMS", None))
        self.lbl_err_msg.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Log In</span></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.lbl_goSignUp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Don't have an account? <a href=\"#\">Sign Up</a></span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Password</span></p></body></html>", None))
        self.input_password.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Sign Up</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email</span></p></body></html>", None))
        self.lbl_err_msg_email_exist.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Password</span></p></body></html>", None))
        self.lbl_err_msg_pw.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Full Name</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Job Position</span></p></body></html>", None))
        self.input_jobPosition.setItemText(0, QCoreApplication.translate("MainWindow", u"Pharmacist", None))
        self.input_jobPosition.setItemText(1, QCoreApplication.translate("MainWindow", u"Cashier", None))
        self.input_jobPosition.setItemText(2, QCoreApplication.translate("MainWindow", u"Developer", None))

        self.lbl_err_msg_empty.setText("")
        self.btn_signup.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.lbl_goLogin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Already have an account? <a href=\"#\">Log In</a></span></p></body></html>", None))
    # retranslateUi

