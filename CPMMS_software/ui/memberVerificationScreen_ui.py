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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
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
        self.btn_member_manager.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_member_manager.setIcon(icon1)
        self.btn_member_manager.setIconSize(QSize(40, 40))
        self.btn_member_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_member_manager)

        self.btn_item_manager = QPushButton(self.header)
        self.btn_item_manager.setObjectName(u"btn_item_manager")
        sizePolicy.setHeightForWidth(self.btn_item_manager.sizePolicy().hasHeightForWidth())
        self.btn_item_manager.setSizePolicy(sizePolicy)
        self.btn_item_manager.setMaximumSize(QSize(16777215, 16777215))
        self.btn_item_manager.setFont(font)
        self.btn_item_manager.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_item_manager.setIcon(icon2)
        self.btn_item_manager.setIconSize(QSize(40, 40))
        self.btn_item_manager.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_item_manager)

        self.btn_checkout = QPushButton(self.header)
        self.btn_checkout.setObjectName(u"btn_checkout")
        sizePolicy.setHeightForWidth(self.btn_checkout.sizePolicy().hasHeightForWidth())
        self.btn_checkout.setSizePolicy(sizePolicy)
        self.btn_checkout.setFont(font)
        self.btn_checkout.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_checkout.setIcon(icon3)
        self.btn_checkout.setIconSize(QSize(40, 40))
        self.btn_checkout.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_checkout)

        self.btn_member_verification = QPushButton(self.header)
        self.btn_member_verification.setObjectName(u"btn_member_verification")
        sizePolicy.setHeightForWidth(self.btn_member_verification.sizePolicy().hasHeightForWidth())
        self.btn_member_verification.setSizePolicy(sizePolicy)
        self.btn_member_verification.setFont(font)
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
        self.btn_ic.setFont(font1)
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
        self.btn_facial_recog.setFont(font1)
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
        self.btn_addMember.setFont(font1)
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
        self.btn_listMember.setFont(font1)
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

        self.input_ICNum_reg = QLineEdit(self.addMember)
        self.input_ICNum_reg.setObjectName(u"input_ICNum_reg")
        self.input_ICNum_reg.setMinimumSize(QSize(0, 0))
        self.input_ICNum_reg.setMaximumSize(QSize(328, 30))
        self.input_ICNum_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_ICNum_reg, 7, 2, 1, 3)

        self.btn_cam = QPushButton(self.addMember)
        self.btn_cam.setObjectName(u"btn_cam")
        self.btn_cam.setMaximumSize(QSize(90, 35))
        self.btn_cam.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cam.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        icon5 = QIcon()
        icon5.addFile(u":/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cam.setIcon(icon5)

        self.gridLayout_4.addWidget(self.btn_cam, 9, 4, 1, 1)

        self.label_5 = QLabel(self.addMember)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_5, 6, 2, 1, 3)

        self.label_3 = QLabel(self.addMember)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_3, 2, 2, 1, 2)

        self.input_fullName_reg = QLineEdit(self.addMember)
        self.input_fullName_reg.setObjectName(u"input_fullName_reg")
        self.input_fullName_reg.setMinimumSize(QSize(0, 0))
        self.input_fullName_reg.setMaximumSize(QSize(328, 30))
        self.input_fullName_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_fullName_reg, 3, 2, 1, 3)

        self.input_fileName = QLineEdit(self.addMember)
        self.input_fileName.setObjectName(u"input_fileName")
        self.input_fileName.setMaximumSize(QSize(232, 30))
        self.input_fileName.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.input_fileName.setReadOnly(True)

        self.gridLayout_4.addWidget(self.input_fileName, 9, 2, 1, 2)

        self.label_4 = QLabel(self.addMember)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label_4, 4, 2, 1, 2)

        self.btn_browse = QPushButton(self.addMember)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMaximumSize(QSize(90, 35))
        self.btn_browse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_browse.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_4.addWidget(self.btn_browse, 9, 5, 1, 1)

        self.btn_registerMem = QPushButton(self.addMember)
        self.btn_registerMem.setObjectName(u"btn_registerMem")
        self.btn_registerMem.setMaximumSize(QSize(328, 35))
        self.btn_registerMem.setSizeIncrement(QSize(0, 35))
        self.btn_registerMem.setFont(font1)
        self.btn_registerMem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_registerMem.setStyleSheet(u"background-color: rgba(11,107,194,255);\n"
"color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.btn_registerMem, 11, 2, 1, 3)

        self.label = QLabel(self.addMember)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.label, 8, 2, 1, 3)

        self.input_email_reg = QLineEdit(self.addMember)
        self.input_email_reg.setObjectName(u"input_email_reg")
        self.input_email_reg.setMinimumSize(QSize(0, 0))
        self.input_email_reg.setMaximumSize(QSize(328, 30))
        self.input_email_reg.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_4.addWidget(self.input_email_reg, 5, 2, 1, 3)

        self.stackedWidget.addWidget(self.addMember)
        self.listMember = QWidget()
        self.listMember.setObjectName(u"listMember")
        self.gridLayout_5 = QGridLayout(self.listMember)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.listMember)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_20, 0, 0, 1, 7)

        self.frame_18 = QFrame(self.listMember)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_18, 1, 0, 2, 1)

        self.label_14 = QLabel(self.listMember)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMaximumSize(QSize(16777215, 50))
        self.label_14.setSizeIncrement(QSize(0, 0))
        self.label_14.setStyleSheet(u"")
        self.label_14.setTextFormat(Qt.AutoText)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_14, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.listMember)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_22, 1, 2, 1, 1)

        self.searchMem = QLineEdit(self.listMember)
        self.searchMem.setObjectName(u"searchMem")
        self.searchMem.setMaximumSize(QSize(250, 16777215))
        self.searchMem.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_5.addWidget(self.searchMem, 1, 3, 1, 1)

        self.btn_searchMem = QPushButton(self.listMember)
        self.btn_searchMem.setObjectName(u"btn_searchMem")
        self.btn_searchMem.setMaximumSize(QSize(90, 16777215))
        self.btn_searchMem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_searchMem.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_5.addWidget(self.btn_searchMem, 1, 4, 1, 1)

        self.btn_refreshMem = QPushButton(self.listMember)
        self.btn_refreshMem.setObjectName(u"btn_refreshMem")
        self.btn_refreshMem.setMaximumSize(QSize(50, 16777215))
        self.btn_refreshMem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_refreshMem.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        icon6 = QIcon()
        icon6.addFile(u":/icons/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refreshMem.setIcon(icon6)

        self.gridLayout_5.addWidget(self.btn_refreshMem, 1, 5, 1, 1)

        self.frame_19 = QFrame(self.listMember)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_19, 1, 6, 2, 1)

        self.frame_21 = QFrame(self.listMember)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_21, 3, 0, 1, 7)

        self.tbl_memList = QTableWidget(self.listMember)
        if (self.tbl_memList.columnCount() < 4):
            self.tbl_memList.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_memList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_memList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_memList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_memList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tbl_memList.setObjectName(u"tbl_memList")
        self.tbl_memList.setMaximumSize(QSize(925, 700))
        self.tbl_memList.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.tbl_memList.setFrameShape(QFrame.StyledPanel)
        self.tbl_memList.setFrameShadow(QFrame.Sunken)
        self.tbl_memList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_memList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_5.addWidget(self.tbl_memList, 2, 1, 1, 5)

        self.stackedWidget.addWidget(self.listMember)
        self.editMember = QWidget()
        self.editMember.setObjectName(u"editMember")
        self.gridLayout_6 = QGridLayout(self.editMember)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.editMember)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(100, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_25, 1, 2, 1, 1)

        self.frame_24 = QFrame(self.editMember)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 0))
        self.frame_24.setMaximumSize(QSize(100, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_27 = QFrame(self.editMember)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 30))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_27, 2, 0, 1, 3)

        self.frame_23 = QFrame(self.editMember)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(925, 650))
        self.frame_23.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_23.setLineWidth(1)
        self.gridLayout_7 = QGridLayout(self.frame_23)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_30, 3, 4, 5, 1)

        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_29, 3, 0, 5, 1)

        self.frame_28 = QFrame(self.frame_23)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 40))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_deleteMemEdit = QPushButton(self.frame_28)
        self.btn_deleteMemEdit.setObjectName(u"btn_deleteMemEdit")
        self.btn_deleteMemEdit.setMaximumSize(QSize(180, 40))
        self.btn_deleteMemEdit.setFont(font1)
        self.btn_deleteMemEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deleteMemEdit.setStyleSheet(u"background-color: rgba(215,41,41,255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_deleteMemEdit)

        self.btn_updateMemEdit = QPushButton(self.frame_28)
        self.btn_updateMemEdit.setObjectName(u"btn_updateMemEdit")
        self.btn_updateMemEdit.setMaximumSize(QSize(180, 40))
        self.btn_updateMemEdit.setFont(font1)
        self.btn_updateMemEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_updateMemEdit.setStyleSheet(u"background-color: rgba(41,156,39,255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_updateMemEdit)


        self.gridLayout_7.addWidget(self.frame_28, 8, 0, 1, 5)

        self.btn_back = QPushButton(self.frame_23)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"background-color: rgba(217,217,217,255)")

        self.gridLayout_7.addWidget(self.btn_back, 0, 0, 1, 1, Qt.AlignLeft)

        self.input_email_edit = QLineEdit(self.frame_23)
        self.input_email_edit.setObjectName(u"input_email_edit")
        self.input_email_edit.setMinimumSize(QSize(0, 0))
        self.input_email_edit.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(12)
        self.input_email_edit.setFont(font5)
        self.input_email_edit.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_7.addWidget(self.input_email_edit, 5, 2, 1, 2)

        self.label_2 = QLabel(self.frame_23)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_2, 6, 1, 1, 1)

        self.label_18 = QLabel(self.frame_23)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_18, 7, 1, 1, 1)

        self.input_pts_edit = QLineEdit(self.frame_23)
        self.input_pts_edit.setObjectName(u"input_pts_edit")
        self.input_pts_edit.setMinimumSize(QSize(0, 0))
        self.input_pts_edit.setMaximumSize(QSize(16777215, 30))
        self.input_pts_edit.setFont(font5)
        self.input_pts_edit.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.input_pts_edit.setReadOnly(True)

        self.gridLayout_7.addWidget(self.input_pts_edit, 7, 2, 1, 2)

        self.label_15 = QLabel(self.frame_23)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMaximumSize(QSize(16777215, 40))
        self.label_15.setSizeIncrement(QSize(0, 0))
        self.label_15.setStyleSheet(u"")
        self.label_15.setTextFormat(Qt.AutoText)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_15, 1, 1, 1, 3, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame_23)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(130, 30))

        self.gridLayout_7.addWidget(self.label_6, 3, 1, 1, 1)

        self.input_fullName_edit = QLineEdit(self.frame_23)
        self.input_fullName_edit.setObjectName(u"input_fullName_edit")
        self.input_fullName_edit.setMinimumSize(QSize(0, 0))
        self.input_fullName_edit.setMaximumSize(QSize(16777215, 30))
        self.input_fullName_edit.setFont(font5)
        self.input_fullName_edit.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_7.addWidget(self.input_fullName_edit, 3, 2, 1, 2)

        self.label_16 = QLabel(self.frame_23)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_16, 4, 1, 1, 1)

        self.input_IC_edit = QLineEdit(self.frame_23)
        self.input_IC_edit.setObjectName(u"input_IC_edit")
        self.input_IC_edit.setMinimumSize(QSize(0, 0))
        self.input_IC_edit.setMaximumSize(QSize(16777215, 30))
        self.input_IC_edit.setFont(font5)
        self.input_IC_edit.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_7.addWidget(self.input_IC_edit, 4, 2, 1, 2)

        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_7.addWidget(self.label_17, 5, 1, 1, 1)

        self.lbl_memID = QLabel(self.frame_23)
        self.lbl_memID.setObjectName(u"lbl_memID")
        self.lbl_memID.setFont(font5)

        self.gridLayout_7.addWidget(self.lbl_memID, 6, 2, 1, 2)


        self.gridLayout_6.addWidget(self.frame_23, 1, 1, 1, 1)

        self.frame_26 = QFrame(self.editMember)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy3)
        self.frame_26.setMaximumSize(QSize(16777215, 30))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.frame_26, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.editMember)
        self.adminProfile = QWidget()
        self.adminProfile.setObjectName(u"adminProfile")
        self.gridLayout_8 = QGridLayout(self.adminProfile)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.adminProfile)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(100, 16777215))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_33, 1, 0, 1, 1)

        self.frame_31 = QFrame(self.adminProfile)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 30))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_31, 0, 0, 1, 3)

        self.frame_35 = QFrame(self.adminProfile)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 30))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_35, 2, 0, 1, 3)

        self.frame_34 = QFrame(self.adminProfile)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(100, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_34, 1, 2, 1, 1)

        self.frame_32 = QFrame(self.adminProfile)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy4)
        self.frame_32.setMaximumSize(QSize(925, 650))
        self.frame_32.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_32)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_32)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setMaximumSize(QSize(925, 50))
        self.label_19.setSizeIncrement(QSize(0, 0))
        self.label_19.setStyleSheet(u"")
        self.label_19.setTextFormat(Qt.AutoText)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_19, 0, 1, 1, 2)

        self.frame_36 = QFrame(self.frame_32)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy5)
        self.frame_36.setMaximumSize(QSize(16777215, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_36, 1, 0, 4, 1)

        self.label_20 = QLabel(self.frame_32)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(130, 30))

        self.gridLayout_10.addWidget(self.label_20, 1, 1, 1, 1)

        self.input_fullName_admin = QLineEdit(self.frame_32)
        self.input_fullName_admin.setObjectName(u"input_fullName_admin")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.input_fullName_admin.sizePolicy().hasHeightForWidth())
        self.input_fullName_admin.setSizePolicy(sizePolicy6)
        self.input_fullName_admin.setMinimumSize(QSize(235, 0))
        self.input_fullName_admin.setMaximumSize(QSize(16777215, 30))
        self.input_fullName_admin.setFont(font5)
        self.input_fullName_admin.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_10.addWidget(self.input_fullName_admin, 1, 2, 1, 1)

        self.frame_37 = QFrame(self.frame_32)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy5.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy5)
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_37, 1, 3, 4, 1)

        self.label_21 = QLabel(self.frame_32)
        self.label_21.setObjectName(u"label_21")
        sizePolicy5.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy5)
        self.label_21.setMaximumSize(QSize(130, 30))

        self.gridLayout_10.addWidget(self.label_21, 2, 1, 1, 1)

        self.lbl_admin_email = QLabel(self.frame_32)
        self.lbl_admin_email.setObjectName(u"lbl_admin_email")
        sizePolicy5.setHeightForWidth(self.lbl_admin_email.sizePolicy().hasHeightForWidth())
        self.lbl_admin_email.setSizePolicy(sizePolicy5)
        self.lbl_admin_email.setMaximumSize(QSize(16777215, 30))
        self.lbl_admin_email.setFont(font5)

        self.gridLayout_10.addWidget(self.lbl_admin_email, 2, 2, 1, 1)

        self.label_31 = QLabel(self.frame_32)
        self.label_31.setObjectName(u"label_31")
        sizePolicy3.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy3)
        self.label_31.setMaximumSize(QSize(130, 30))

        self.gridLayout_10.addWidget(self.label_31, 3, 1, 1, 1)

        self.lbl_adminID = QLabel(self.frame_32)
        self.lbl_adminID.setObjectName(u"lbl_adminID")
        sizePolicy5.setHeightForWidth(self.lbl_adminID.sizePolicy().hasHeightForWidth())
        self.lbl_adminID.setSizePolicy(sizePolicy5)
        self.lbl_adminID.setMaximumSize(QSize(16777215, 30))
        self.lbl_adminID.setFont(font5)

        self.gridLayout_10.addWidget(self.lbl_adminID, 3, 2, 1, 1)

        self.label_22 = QLabel(self.frame_32)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(130, 30))

        self.gridLayout_10.addWidget(self.label_22, 4, 1, 1, 1)

        self.input_jobPosition = QComboBox(self.frame_32)
        self.input_jobPosition.addItem("")
        self.input_jobPosition.addItem("")
        self.input_jobPosition.addItem("")
        self.input_jobPosition.setObjectName(u"input_jobPosition")
        sizePolicy6.setHeightForWidth(self.input_jobPosition.sizePolicy().hasHeightForWidth())
        self.input_jobPosition.setSizePolicy(sizePolicy6)
        self.input_jobPosition.setMaximumSize(QSize(16777215, 30))
        self.input_jobPosition.setFont(font5)
        self.input_jobPosition.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_10.addWidget(self.input_jobPosition, 4, 2, 1, 1)

        self.frame_38 = QFrame(self.frame_32)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(925, 40))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.btn_updateAdmin = QPushButton(self.frame_38)
        self.btn_updateAdmin.setObjectName(u"btn_updateAdmin")
        self.btn_updateAdmin.setMaximumSize(QSize(180, 40))
        self.btn_updateAdmin.setFont(font1)
        self.btn_updateAdmin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_updateAdmin.setStyleSheet(u"background-color: rgba(41,156,39,255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.btn_updateAdmin)


        self.gridLayout_10.addWidget(self.frame_38, 5, 0, 1, 4)


        self.gridLayout_8.addWidget(self.frame_32, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.adminProfile)
        self.checkout = QWidget()
        self.checkout.setObjectName(u"checkout")
        self.gridLayout_9 = QGridLayout(self.checkout)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.checkout)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy7)
        self.frame_40.setMaximumSize(QSize(95, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_40, 1, 2, 1, 1)

        self.frame_43 = QFrame(self.checkout)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy8)
        self.frame_43.setMinimumSize(QSize(0, 20))
        self.frame_43.setMaximumSize(QSize(16777215, 30))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_43, 2, 0, 1, 3)

        self.frame_41 = QFrame(self.checkout)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy8.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy8)
        self.frame_41.setMinimumSize(QSize(0, 20))
        self.frame_41.setMaximumSize(QSize(16777215, 30))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_41, 0, 0, 1, 3)

        self.frame_39 = QFrame(self.checkout)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy7.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy7)
        self.frame_39.setMaximumSize(QSize(95, 16777215))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_39, 1, 0, 1, 1)

        self.frame_42 = QFrame(self.checkout)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(925, 650))
        self.frame_42.setStyleSheet(u"background-color: rgba(217,217,217,255)")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_42)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(20, -1, 20, -1)
        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy7.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy7)
        self.frame_45.setMaximumSize(QSize(150, 16777215))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_45, 5, 3, 1, 1)

        self.frame_46 = QFrame(self.frame_42)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy3.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy3)
        self.frame_46.setMinimumSize(QSize(0, 26))
        self.frame_46.setMaximumSize(QSize(16777215, 16777215))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_46)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.label_23 = QLabel(self.frame_46)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setMaximumSize(QSize(16777215, 50))
        self.label_23.setSizeIncrement(QSize(0, 0))
        self.label_23.setStyleSheet(u"")
        self.label_23.setTextFormat(Qt.AutoText)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_23, 0, Qt.AlignHCenter)


        self.gridLayout_11.addWidget(self.frame_46, 1, 0, 1, 4)

        self.lbl_member_status = QLabel(self.frame_42)
        self.lbl_member_status.setObjectName(u"lbl_member_status")
        sizePolicy2.setHeightForWidth(self.lbl_member_status.sizePolicy().hasHeightForWidth())
        self.lbl_member_status.setSizePolicy(sizePolicy2)
        self.lbl_member_status.setMaximumSize(QSize(100, 50))
        self.lbl_member_status.setSizeIncrement(QSize(0, 0))
        self.lbl_member_status.setFont(font5)
        self.lbl_member_status.setStyleSheet(u"")
        self.lbl_member_status.setTextFormat(Qt.AutoText)
        self.lbl_member_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.lbl_member_status, 10, 0, 1, 1)

        self.btn_pay = QPushButton(self.frame_42)
        self.btn_pay.setObjectName(u"btn_pay")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_pay.sizePolicy().hasHeightForWidth())
        self.btn_pay.setSizePolicy(sizePolicy9)
        self.btn_pay.setMinimumSize(QSize(140, 40))
        self.btn_pay.setMaximumSize(QSize(140, 40))
        self.btn_pay.setFont(font1)
        self.btn_pay.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pay.setStyleSheet(u"background-color: rgba(41,156,39,255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.btn_pay, 10, 3, 1, 1)

        self.lbl_currentMem = QLabel(self.frame_42)
        self.lbl_currentMem.setObjectName(u"lbl_currentMem")
        self.lbl_currentMem.setFont(font5)

        self.gridLayout_11.addWidget(self.lbl_currentMem, 10, 1, 1, 1)

        self.lbl_total = QLabel(self.frame_42)
        self.lbl_total.setObjectName(u"lbl_total")
        sizePolicy2.setHeightForWidth(self.lbl_total.sizePolicy().hasHeightForWidth())
        self.lbl_total.setSizePolicy(sizePolicy2)
        self.lbl_total.setMaximumSize(QSize(16777215, 50))
        self.lbl_total.setSizeIncrement(QSize(0, 0))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.lbl_total.setFont(font6)
        self.lbl_total.setStyleSheet(u"")
        self.lbl_total.setTextFormat(Qt.AutoText)
        self.lbl_total.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lbl_total, 4, 3, 1, 1)

        self.tbl_checkout = QTableWidget(self.frame_42)
        if (self.tbl_checkout.columnCount() < 5):
            self.tbl_checkout.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_checkout.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_checkout.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_checkout.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_checkout.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_checkout.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tbl_checkout.setObjectName(u"tbl_checkout")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.tbl_checkout.sizePolicy().hasHeightForWidth())
        self.tbl_checkout.setSizePolicy(sizePolicy10)
        self.tbl_checkout.setMaximumSize(QSize(925, 400))
        self.tbl_checkout.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.tbl_checkout.setFrameShape(QFrame.StyledPanel)
        self.tbl_checkout.setFrameShadow(QFrame.Sunken)
        self.tbl_checkout.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_checkout.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_11.addWidget(self.tbl_checkout, 2, 0, 1, 4)

        self.lbl_total_pts = QLabel(self.frame_42)
        self.lbl_total_pts.setObjectName(u"lbl_total_pts")
        sizePolicy2.setHeightForWidth(self.lbl_total_pts.sizePolicy().hasHeightForWidth())
        self.lbl_total_pts.setSizePolicy(sizePolicy2)
        self.lbl_total_pts.setMaximumSize(QSize(16777215, 50))
        self.lbl_total_pts.setSizeIncrement(QSize(0, 0))
        self.lbl_total_pts.setFont(font5)
        self.lbl_total_pts.setStyleSheet(u"")
        self.lbl_total_pts.setTextFormat(Qt.AutoText)
        self.lbl_total_pts.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.lbl_total_pts, 6, 3, 1, 1)

        self.btn_usepts = QPushButton(self.frame_42)
        self.btn_usepts.setObjectName(u"btn_usepts")
        self.btn_usepts.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.btn_usepts.sizePolicy().hasHeightForWidth())
        self.btn_usepts.setSizePolicy(sizePolicy1)
        self.btn_usepts.setMinimumSize(QSize(140, 40))
        self.btn_usepts.setMaximumSize(QSize(140, 40))
        self.btn_usepts.setFont(font1)
        self.btn_usepts.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usepts.setStyleSheet(u"background-color: rgba(231,179,29,255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_11.addWidget(self.btn_usepts, 7, 3, 1, 1)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_44, 5, 0, 3, 3)

        self.btn_additem = QPushButton(self.frame_42)
        self.btn_additem.setObjectName(u"btn_additem")
        self.btn_additem.setMinimumSize(QSize(100, 0))
        self.btn_additem.setMaximumSize(QSize(100, 30))
        font7 = QFont()
        font7.setPointSize(9)
        self.btn_additem.setFont(font7)
        self.btn_additem.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_additem.setStyleSheet(u"background-color: rgb(255, 255, 255)")

        self.gridLayout_11.addWidget(self.btn_additem, 4, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_42, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.checkout)
        self.frame_42.raise_()
        self.frame_39.raise_()
        self.frame_40.raise_()
        self.frame_41.raise_()
        self.frame_43.raise_()

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)


        self.retranslateUi(Form)

        self.btn_member_verification.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CPMMS", None))
        self.btn_member_manager.setText(QCoreApplication.translate("Form", u"Member Manager", None))
        self.btn_item_manager.setText(QCoreApplication.translate("Form", u"Item Manager", None))
        self.btn_checkout.setText(QCoreApplication.translate("Form", u"Checkout", None))
        self.btn_member_verification.setText(QCoreApplication.translate("Form", u"Member Verification", None))
        self.btn_signout.setText(QCoreApplication.translate("Form", u"SIGN OUT", None))
        self.profile_img.setText("")
        self.name_label.setText(QCoreApplication.translate("Form", u"name", None))
        self.position_label.setText(QCoreApplication.translate("Form", u"staff position", None))
        self.btn_edit_profile.setText(QCoreApplication.translate("Form", u"Edit profile", None))
        self.Date_Label.setText("")
        self.Time_Label.setText("")
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
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Register new member</span></p></body></html>", None))
        self.input_ICNum_reg.setText("")
        self.btn_cam.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">IC number</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Full Name</span></p></body></html>", None))
        self.input_fullName_reg.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email address</span></p></body></html>", None))
        self.btn_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
        self.btn_registerMem.setText(QCoreApplication.translate("Form", u"REGISTER", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Upload a clear photo of the member's face</span></p></body></html>", None))
        self.input_email_reg.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Member list</span></p></body></html>", None))
        self.btn_searchMem.setText(QCoreApplication.translate("Form", u"Search", None))
        self.btn_refreshMem.setText("")
        ___qtablewidgetitem = self.tbl_memList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tbl_memList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem2 = self.tbl_memList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"IC number", None));
        ___qtablewidgetitem3 = self.tbl_memList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Points", None));
        self.btn_deleteMemEdit.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.btn_updateMemEdit.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Back", None))
        self.input_email_edit.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Member ID:</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Member Points:</span></p></body></html>", None))
        self.input_pts_edit.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Member information</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Full Name:</span></p></body></html>", None))
        self.input_fullName_edit.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">IC number:</span></p></body></html>", None))
        self.input_IC_edit.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email Address:</span></p></body></html>", None))
        self.lbl_memID.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">MemID</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Edit Profile</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Full Name:</span></p></body></html>", None))
        self.input_fullName_admin.setText("")
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Email Address:</span></p></body></html>", None))
        self.lbl_admin_email.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">email admin</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Admin ID:</span></p></body></html>", None))
        self.lbl_adminID.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">AdminID</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Job Position:</span></p></body></html>", None))
        self.input_jobPosition.setItemText(0, QCoreApplication.translate("Form", u"Pharmacist", None))
        self.input_jobPosition.setItemText(1, QCoreApplication.translate("Form", u"Cashier", None))
        self.input_jobPosition.setItemText(2, QCoreApplication.translate("Form", u"Developer", None))

        self.btn_updateAdmin.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Checkout</span></p></body></html>", None))
        self.lbl_member_status.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Member:</p></body></html>", None))
        self.btn_pay.setText(QCoreApplication.translate("Form", u"Proceed payment", None))
        self.lbl_currentMem.setText("")
        self.lbl_total.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total:</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.tbl_checkout.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem5 = self.tbl_checkout.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem6 = self.tbl_checkout.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Price (RM)", None));
        ___qtablewidgetitem7 = self.tbl_checkout.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem8 = self.tbl_checkout.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Cancel", None));
        self.lbl_total_pts.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">Total points:</span></p></body></html>", None))
        self.btn_usepts.setText(QCoreApplication.translate("Form", u"Use points", None))
        self.btn_additem.setText(QCoreApplication.translate("Form", u"Add Item", None))
    # retranslateUi

