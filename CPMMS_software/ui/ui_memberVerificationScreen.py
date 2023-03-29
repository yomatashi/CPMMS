# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memberVerificationScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1020, 600)
        Form.setMinimumSize(QSize(1020, 600))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(Form)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 180))
        self.header.setMaximumSize(QSize(16777215, 180))
        self.header.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_member_manager = QPushButton(self.header)
        self.btn_member_manager.setObjectName(u"btn_member_manager")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_member_manager.sizePolicy().hasHeightForWidth())
        self.btn_member_manager.setSizePolicy(sizePolicy)
        self.btn_member_manager.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.btn_member_manager.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_member_manager.setIcon(icon)
        self.btn_member_manager.setIconSize(QSize(40, 40))
        self.btn_member_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_member_manager)

        self.btn_item_manager = QPushButton(self.header)
        self.btn_item_manager.setObjectName(u"btn_item_manager")
        sizePolicy.setHeightForWidth(self.btn_item_manager.sizePolicy().hasHeightForWidth())
        self.btn_item_manager.setSizePolicy(sizePolicy)
        self.btn_item_manager.setMaximumSize(QSize(16777215, 16777215))
        self.btn_item_manager.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_item_manager.setIcon(icon1)
        self.btn_item_manager.setIconSize(QSize(40, 40))
        self.btn_item_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_item_manager)

        self.btn_checkout = QPushButton(self.header)
        self.btn_checkout.setObjectName(u"btn_checkout")
        sizePolicy.setHeightForWidth(self.btn_checkout.sizePolicy().hasHeightForWidth())
        self.btn_checkout.setSizePolicy(sizePolicy)
        self.btn_checkout.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_checkout.setIcon(icon2)
        self.btn_checkout.setIconSize(QSize(40, 40))
        self.btn_checkout.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_checkout)

        self.btn_member_verification = QPushButton(self.header)
        self.btn_member_verification.setObjectName(u"btn_member_verification")
        sizePolicy.setHeightForWidth(self.btn_member_verification.sizePolicy().hasHeightForWidth())
        self.btn_member_verification.setSizePolicy(sizePolicy)
        self.btn_member_verification.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_member_verification.setIcon(icon3)
        self.btn_member_verification.setIconSize(QSize(40, 40))
        self.btn_member_verification.setCheckable(False)
        self.btn_member_verification.setChecked(False)
        self.btn_member_verification.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btn_member_verification)


        self.gridLayout.addWidget(self.header, 0, 1, 1, 1)

        self.sidebar = QFrame(Form)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(230, 0))
        self.sidebar.setMaximumSize(QSize(230, 16777215))
        self.sidebar.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.sidebar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_signout = QPushButton(self.sidebar)
        self.btn_signout.setObjectName(u"btn_signout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_signout.sizePolicy().hasHeightForWidth())
        self.btn_signout.setSizePolicy(sizePolicy1)
        self.btn_signout.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btn_signout.setFont(font1)
        self.btn_signout.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_2.addWidget(self.btn_signout, 2, 0, 1, 1)

        self.profileFrame = QFrame(self.sidebar)
        self.profileFrame.setObjectName(u"profileFrame")
        self.profileFrame.setMaximumSize(QSize(16777215, 950))
        self.profileFrame.setFrameShape(QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.profileFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.profile_img = QLabel(self.profileFrame)
        self.profile_img.setObjectName(u"profile_img")

        self.verticalLayout_2.addWidget(self.profile_img)

        self.profile = QVBoxLayout()
        self.profile.setSpacing(10)
        self.profile.setObjectName(u"profile")
        self.profile.setContentsMargins(-1, 10, -1, 10)
        self.name_label = QLabel(self.profileFrame)
        self.name_label.setObjectName(u"name_label")
        font2 = QFont()
        font2.setPointSize(16)
        self.name_label.setFont(font2)

        self.profile.addWidget(self.name_label, 0, Qt.AlignHCenter)

        self.position_label = QLabel(self.profileFrame)
        self.position_label.setObjectName(u"position_label")
        self.position_label.setFont(font2)

        self.profile.addWidget(self.position_label, 0, Qt.AlignHCenter)

        self.btn_edit_profile = QToolButton(self.profileFrame)
        self.btn_edit_profile.setObjectName(u"btn_edit_profile")
        self.btn_edit_profile.setFont(font)

        self.profile.addWidget(self.btn_edit_profile, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.profile)

        self.frame = QFrame(self.profileFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.dateTime = QVBoxLayout()
        self.dateTime.setSpacing(10)
        self.dateTime.setObjectName(u"dateTime")
        self.Date_Label = QLabel(self.profileFrame)
        self.Date_Label.setObjectName(u"Date_Label")
        self.Date_Label.setFont(font2)

        self.dateTime.addWidget(self.Date_Label, 0, Qt.AlignHCenter)

        self.Time_Label = QLabel(self.profileFrame)
        self.Time_Label.setObjectName(u"Time_Label")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.Time_Label.setFont(font3)

        self.dateTime.addWidget(self.Time_Label, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.dateTime)

        self.frame_2 = QFrame(self.profileFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout_2.addWidget(self.profileFrame, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.sidebar, 0, 0, 3, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.verificationMethod = QWidget()
        self.verificationMethod.setObjectName(u"verificationMethod")
        self.verticalLayout = QVBoxLayout(self.verificationMethod)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.verificationMethod)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(600, 50))
        self.label_7.setSizeIncrement(QSize(0, 0))
        self.label_7.setStyleSheet(u"")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.verificationMethod)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMaximumSize(QSize(600, 50))
        self.label_8.setSizeIncrement(QSize(0, 0))
        self.label_8.setStyleSheet(u"")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.btn_ic = QPushButton(self.verificationMethod)
        self.btn_ic.setObjectName(u"btn_ic")
        sizePolicy2.setHeightForWidth(self.btn_ic.sizePolicy().hasHeightForWidth())
        self.btn_ic.setSizePolicy(sizePolicy2)
        self.btn_ic.setMinimumSize(QSize(0, 0))
        self.btn_ic.setMaximumSize(QSize(600, 50))
        self.btn_ic.setSizeIncrement(QSize(0, 0))
        self.btn_ic.setFont(font1)
        self.btn_ic.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")
        self.btn_ic.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.btn_ic, 0, Qt.AlignHCenter)

        self.btn_facial_recog = QPushButton(self.verificationMethod)
        self.btn_facial_recog.setObjectName(u"btn_facial_recog")
        sizePolicy2.setHeightForWidth(self.btn_facial_recog.sizePolicy().hasHeightForWidth())
        self.btn_facial_recog.setSizePolicy(sizePolicy2)
        self.btn_facial_recog.setMaximumSize(QSize(600, 50))
        self.btn_facial_recog.setFont(font1)
        self.btn_facial_recog.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.btn_facial_recog, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.verificationMethod)
        self.ICMethod = QWidget()
        self.ICMethod.setObjectName(u"ICMethod")
        self.gridLayout_3 = QGridLayout(self.ICMethod)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.ICMethod)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMaximumSize(QSize(600, 50))
        self.label_9.setSizeIncrement(QSize(0, 0))
        self.label_9.setStyleSheet(u"")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2, Qt.AlignHCenter)

        self.input_ICNum = QLineEdit(self.ICMethod)
        self.input_ICNum.setObjectName(u"input_ICNum")
        self.input_ICNum.setMaximumSize(QSize(600, 30))
        self.input_ICNum.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.input_ICNum, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.ICMethod)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(160, 40))
        self.pushButton.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.ICMethod)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)


        self.retranslateUi(Form)

        self.btn_member_verification.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_member_manager.setText(QCoreApplication.translate("Form", u"Member Manager", None))
        self.btn_item_manager.setText(QCoreApplication.translate("Form", u"Item Manager", None))
        self.btn_checkout.setText(QCoreApplication.translate("Form", u"Checkout", None))
        self.btn_member_verification.setText(QCoreApplication.translate("Form", u"Member Verification", None))
        self.btn_signout.setText(QCoreApplication.translate("Form", u"SIGN OUT", None))
        self.profile_img.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"name", None))
        self.position_label.setText(QCoreApplication.translate("Form", u"staff position", None))
        self.btn_edit_profile.setText(QCoreApplication.translate("Form", u"Edit profile", None))
        self.Date_Label.setText(QCoreApplication.translate("Form", u"date", None))
        self.Time_Label.setText(QCoreApplication.translate("Form", u"time", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Member verification</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Select method to verify membership</span></p></body></html>", None))
        self.btn_ic.setText(QCoreApplication.translate("Form", u"IC NUMBER VERIFICATION", None))
        self.btn_facial_recog.setText(QCoreApplication.translate("Form", u"FACIAL RECOGNITION VERIFICATION", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Insert member IC number</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Verify member", None))
    # retranslateUi

