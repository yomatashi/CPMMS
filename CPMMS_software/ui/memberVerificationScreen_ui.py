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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QStackedWidget, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1020, 600)
        Form.setMinimumSize(QSize(1020, 600))
        icon = QIcon()
        icon.addFile(u":/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_signout.sizePolicy().hasHeightForWidth())
        self.btn_signout.setSizePolicy(sizePolicy)
        self.btn_signout.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_signout.setFont(font)
        self.btn_signout.setCursor(QCursor(Qt.PointingHandCursor))
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
        font1 = QFont()
        font1.setPointSize(16)
        self.name_label.setFont(font1)

        self.profile.addWidget(self.name_label, 0, Qt.AlignHCenter)

        self.position_label = QLabel(self.profileFrame)
        self.position_label.setObjectName(u"position_label")
        self.position_label.setFont(font1)

        self.profile.addWidget(self.position_label, 0, Qt.AlignHCenter)

        self.btn_edit_profile = QToolButton(self.profileFrame)
        self.btn_edit_profile.setObjectName(u"btn_edit_profile")
        font2 = QFont()
        font2.setPointSize(11)
        self.btn_edit_profile.setFont(font2)
        self.btn_edit_profile.setCursor(QCursor(Qt.PointingHandCursor))

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
        self.Date_Label.setFont(font1)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_member_manager.sizePolicy().hasHeightForWidth())
        self.btn_member_manager.setSizePolicy(sizePolicy1)
        self.btn_member_manager.setMaximumSize(QSize(16777215, 16777215))
        self.btn_member_manager.setFont(font2)
        self.btn_member_manager.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_member_manager.setIcon(icon1)
        self.btn_member_manager.setIconSize(QSize(40, 40))
        self.btn_member_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_member_manager)

        self.btn_item_manager = QPushButton(self.header)
        self.btn_item_manager.setObjectName(u"btn_item_manager")
        sizePolicy1.setHeightForWidth(self.btn_item_manager.sizePolicy().hasHeightForWidth())
        self.btn_item_manager.setSizePolicy(sizePolicy1)
        self.btn_item_manager.setMaximumSize(QSize(16777215, 16777215))
        self.btn_item_manager.setFont(font2)
        self.btn_item_manager.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_item_manager.setIcon(icon2)
        self.btn_item_manager.setIconSize(QSize(40, 40))
        self.btn_item_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_item_manager)

        self.btn_checkout = QPushButton(self.header)
        self.btn_checkout.setObjectName(u"btn_checkout")
        sizePolicy1.setHeightForWidth(self.btn_checkout.sizePolicy().hasHeightForWidth())
        self.btn_checkout.setSizePolicy(sizePolicy1)
        self.btn_checkout.setFont(font2)
        self.btn_checkout.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_checkout.setIcon(icon3)
        self.btn_checkout.setIconSize(QSize(40, 40))
        self.btn_checkout.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_checkout)

        self.btn_member_verification = QPushButton(self.header)
        self.btn_member_verification.setObjectName(u"btn_member_verification")
        sizePolicy1.setHeightForWidth(self.btn_member_verification.sizePolicy().hasHeightForWidth())
        self.btn_member_verification.setSizePolicy(sizePolicy1)
        self.btn_member_verification.setFont(font2)
        self.btn_member_verification.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_member_verification.setIcon(icon4)
        self.btn_member_verification.setIconSize(QSize(40, 40))
        self.btn_member_verification.setCheckable(False)
        self.btn_member_verification.setChecked(False)
        self.btn_member_verification.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btn_member_verification)


        self.gridLayout.addWidget(self.header, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(205,241,239,255)")
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.verticalLayout_3 = QVBoxLayout(self.welcomePage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.welcomePage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_9)

        self.label_10 = QLabel(self.welcomePage)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMaximumSize(QSize(16777215, 50))
        self.label_10.setSizeIncrement(QSize(0, 0))
        font4 = QFont()
        font4.setBold(True)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgba(194,96,155,255)")
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.welcomePage)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setMaximumSize(QSize(16777215, 50))
        self.label_11.setSizeIncrement(QSize(0, 0))
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"color: rgba(194,96,155,255)")
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.welcomePage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.welcomePage)
        self.verificationMethod = QWidget()
        self.verificationMethod.setObjectName(u"verificationMethod")
        self.verticalLayout = QVBoxLayout(self.verificationMethod)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.verificationMethod)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 250))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.label_7 = QLabel(self.verificationMethod)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setSizeIncrement(QSize(0, 0))
        self.label_7.setStyleSheet(u"")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.verificationMethod)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setSizeIncrement(QSize(0, 0))
        self.label_8.setStyleSheet(u"")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.btn_ic = QPushButton(self.verificationMethod)
        self.btn_ic.setObjectName(u"btn_ic")
        sizePolicy2.setHeightForWidth(self.btn_ic.sizePolicy().hasHeightForWidth())
        self.btn_ic.setSizePolicy(sizePolicy2)
        self.btn_ic.setMinimumSize(QSize(300, 0))
        self.btn_ic.setMaximumSize(QSize(16777215, 50))
        self.btn_ic.setSizeIncrement(QSize(0, 0))
        self.btn_ic.setFont(font)
        self.btn_ic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ic.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")
        self.btn_ic.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.btn_ic, 0, Qt.AlignHCenter)

        self.btn_facial_recog = QPushButton(self.verificationMethod)
        self.btn_facial_recog.setObjectName(u"btn_facial_recog")
        sizePolicy2.setHeightForWidth(self.btn_facial_recog.sizePolicy().hasHeightForWidth())
        self.btn_facial_recog.setSizePolicy(sizePolicy2)
        self.btn_facial_recog.setMinimumSize(QSize(300, 0))
        self.btn_facial_recog.setMaximumSize(QSize(16777215, 50))
        self.btn_facial_recog.setFont(font)
        self.btn_facial_recog.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_facial_recog.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.btn_facial_recog, 0, Qt.AlignHCenter)

        self.cam_input = QComboBox(self.verificationMethod)
        self.cam_input.addItem("")
        self.cam_input.addItem("")
        self.cam_input.setObjectName(u"cam_input")
        self.cam_input.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.cam_input, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.verificationMethod)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 250))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.verificationMethod)
        self.ICMethod = QWidget()
        self.ICMethod.setObjectName(u"ICMethod")
        self.gridLayout_3 = QGridLayout(self.ICMethod)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_6 = QFrame(self.ICMethod)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 250))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_6, 4, 1, 1, 1)

        self.input_ICNum = QLineEdit(self.ICMethod)
        self.input_ICNum.setObjectName(u"input_ICNum")
        self.input_ICNum.setMinimumSize(QSize(0, 0))
        self.input_ICNum.setMaximumSize(QSize(600, 30))
        self.input_ICNum.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_3.addWidget(self.input_ICNum, 2, 1, 1, 1)

        self.label_9 = QLabel(self.ICMethod)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setSizeIncrement(QSize(0, 0))
        self.label_9.setStyleSheet(u"")
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 2, Qt.AlignHCenter)

        self.btn_verify = QPushButton(self.ICMethod)
        self.btn_verify.setObjectName(u"btn_verify")
        self.btn_verify.setMinimumSize(QSize(140, 40))
        self.btn_verify.setMaximumSize(QSize(140, 40))
        self.btn_verify.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_verify.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_3.addWidget(self.btn_verify, 2, 2, 1, 1)

        self.frame_7 = QFrame(self.ICMethod)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_7, 2, 0, 1, 1)

        self.frame_8 = QFrame(self.ICMethod)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_8, 2, 3, 1, 1)

        self.lbl_error_msg = QLabel(self.ICMethod)
        self.lbl_error_msg.setObjectName(u"lbl_error_msg")
        self.lbl_error_msg.setMaximumSize(QSize(16777215, 20))
        self.lbl_error_msg.setStyleSheet(u"color: rgb(255, 0, 0)")

        self.gridLayout_3.addWidget(self.lbl_error_msg, 3, 1, 1, 1)

        self.frame_5 = QFrame(self.ICMethod)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.ICMethod)
        self.memberManager = QWidget()
        self.memberManager.setObjectName(u"memberManager")
        self.verticalLayout_4 = QVBoxLayout(self.memberManager)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.memberManager)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_11)

        self.label_12 = QLabel(self.memberManager)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMaximumSize(QSize(16777215, 50))
        self.label_12.setSizeIncrement(QSize(0, 0))
        self.label_12.setStyleSheet(u"")
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.btn_addMember = QPushButton(self.memberManager)
        self.btn_addMember.setObjectName(u"btn_addMember")
        sizePolicy2.setHeightForWidth(self.btn_addMember.sizePolicy().hasHeightForWidth())
        self.btn_addMember.setSizePolicy(sizePolicy2)
        self.btn_addMember.setMinimumSize(QSize(300, 0))
        self.btn_addMember.setMaximumSize(QSize(16777215, 50))
        self.btn_addMember.setSizeIncrement(QSize(0, 0))
        self.btn_addMember.setFont(font)
        self.btn_addMember.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addMember.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")
        self.btn_addMember.setIconSize(QSize(16, 16))

        self.verticalLayout_4.addWidget(self.btn_addMember, 0, Qt.AlignHCenter)

        self.btn_listMember = QPushButton(self.memberManager)
        self.btn_listMember.setObjectName(u"btn_listMember")
        sizePolicy2.setHeightForWidth(self.btn_listMember.sizePolicy().hasHeightForWidth())
        self.btn_listMember.setSizePolicy(sizePolicy2)
        self.btn_listMember.setMinimumSize(QSize(300, 0))
        self.btn_listMember.setMaximumSize(QSize(16777215, 50))
        self.btn_listMember.setFont(font)
        self.btn_listMember.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_listMember.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")

        self.verticalLayout_4.addWidget(self.btn_listMember, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.memberManager)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.memberManager)
        self.addMember = QWidget()
        self.addMember.setObjectName(u"addMember")
        self.gridLayout_4 = QGridLayout(self.addMember)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.addMember)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_13, 0, 0, 1, 7)

        self.frame_17 = QFrame(self.addMember)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 10))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_17, 10, 2, 1, 3)

        self.frame_14 = QFrame(self.addMember)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 80))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_14, 12, 0, 1, 7)

        self.label_3 = QLabel(self.addMember)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_3, 2, 2, 1, 2)

        self.btn_browse = QPushButton(self.addMember)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMaximumSize(QSize(90, 35))
        self.btn_browse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_4.addWidget(self.btn_browse, 9, 5, 1, 1)

        self.input_fullName_reg = QLineEdit(self.addMember)
        self.input_fullName_reg.setObjectName(u"input_fullName_reg")
        self.input_fullName_reg.setMinimumSize(QSize(0, 0))
        self.input_fullName_reg.setMaximumSize(QSize(16777215, 30))
        self.input_fullName_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_fullName_reg, 3, 2, 1, 3)

        self.label_13 = QLabel(self.addMember)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setMaximumSize(QSize(16777215, 50))
        self.label_13.setSizeIncrement(QSize(0, 0))
        self.label_13.setStyleSheet(u"")
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 1, 1, 1, 5, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.addMember)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_15, 1, 0, 11, 1)

        self.frame_16 = QFrame(self.addMember)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_16, 1, 6, 11, 1)

        self.label_4 = QLabel(self.addMember)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_4, 4, 2, 1, 2)

        self.label_5 = QLabel(self.addMember)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_5, 6, 2, 1, 3)

        self.input_fileName = QLineEdit(self.addMember)
        self.input_fileName.setObjectName(u"input_fileName")
        self.input_fileName.setMaximumSize(QSize(16777215, 30))
        self.input_fileName.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.input_fileName.setReadOnly(True)

        self.gridLayout_4.addWidget(self.input_fileName, 9, 2, 1, 2)

        self.label = QLabel(self.addMember)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label, 8, 2, 1, 3)

        self.btn_cam = QPushButton(self.addMember)
        self.btn_cam.setObjectName(u"btn_cam")
        self.btn_cam.setMaximumSize(QSize(90, 35))
        self.btn_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cam.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        icon5 = QIcon()
        icon5.addFile(u":/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cam.setIcon(icon5)

        self.gridLayout_4.addWidget(self.btn_cam, 9, 4, 1, 1)

        self.btn_registerMem = QPushButton(self.addMember)
        self.btn_registerMem.setObjectName(u"btn_registerMem")
        self.btn_registerMem.setMaximumSize(QSize(16777215, 35))
        self.btn_registerMem.setSizeIncrement(QSize(0, 35))
        self.btn_registerMem.setFont(font)
        self.btn_registerMem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registerMem.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.btn_registerMem, 11, 2, 1, 3)

        self.input_ICNum_reg = QLineEdit(self.addMember)
        self.input_ICNum_reg.setObjectName(u"input_ICNum_reg")
        self.input_ICNum_reg.setMinimumSize(QSize(0, 0))
        self.input_ICNum_reg.setMaximumSize(QSize(16777215, 30))
        self.input_ICNum_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_ICNum_reg, 7, 2, 1, 3)

        self.input_email_reg = QLineEdit(self.addMember)
        self.input_email_reg.setObjectName(u"input_email_reg")
        self.input_email_reg.setMinimumSize(QSize(0, 0))
        self.input_email_reg.setMaximumSize(QSize(16777215, 30))
        self.input_email_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_email_reg, 5, 2, 1, 3)

        self.stackedWidget.addWidget(self.addMember)
        self.listMember = QWidget()
        self.listMember.setObjectName(u"listMember")
        self.label_2 = QLabel(self.listMember)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 140, 181, 16))
        self.stackedWidget.addWidget(self.listMember)

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)


        self.retranslateUi(Form)

        self.btn_member_verification.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CPMMS", None))
        self.btn_signout.setText(QCoreApplication.translate("Form", u"SIGN OUT", None))
        self.profile_img.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"name", None))
        self.position_label.setText(QCoreApplication.translate("Form", u"staff position", None))
        self.btn_edit_profile.setText(QCoreApplication.translate("Form", u"Edit profile", None))
        self.Date_Label.setText("")
        self.Time_Label.setText("")
        self.btn_member_manager.setText(QCoreApplication.translate("Form", u"Member Manager", None))
        self.btn_item_manager.setText(QCoreApplication.translate("Form", u"Item Manager", None))
        self.btn_checkout.setText(QCoreApplication.translate("Form", u"Checkout", None))
        self.btn_member_verification.setText(QCoreApplication.translate("Form", u"Member Verification", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Welcome to Consult Pharmacy Membership</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Management System (CPMMS)</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Member verification</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Select method to verify membership</span></p></body></html>", None))
        self.btn_ic.setText(QCoreApplication.translate("Form", u"IC NUMBER VERIFICATION", None))
        self.btn_facial_recog.setText(QCoreApplication.translate("Form", u"FACIAL RECOGNITION VERIFICATION", None))
        self.cam_input.setItemText(0, QCoreApplication.translate("Form", u"Integrated Camera", None))
        self.cam_input.setItemText(1, QCoreApplication.translate("Form", u"External Camera (USB)", None))

        self.input_ICNum.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">Insert member IC number</span></p></body></html>", None))
        self.btn_verify.setText(QCoreApplication.translate("Form", u"Verify member", None))
        self.lbl_error_msg.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Member Manager</span></p></body></html>", None))
        self.btn_addMember.setText(QCoreApplication.translate("Form", u"ADD NEW MEMBER", None))
        self.btn_listMember.setText(QCoreApplication.translate("Form", u"MEMBER LIST", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Full Name</span></p></body></html>", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.input_fullName_reg.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Register new member</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email address</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">IC number</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Upload a clear photo of the member's face</span></p></body></html>", None))
        self.btn_cam.setText("")
        self.btn_registerMem.setText(QCoreApplication.translate("Form", u"Register", None))
        self.input_ICNum_reg.setText("")
        self.input_email_reg.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"sini letak list members", None))
    # retranslateUi

