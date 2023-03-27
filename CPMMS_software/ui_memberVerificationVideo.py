# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memberVerificationVideo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_OutputDialog(object):
    def setupUi(self, OutputDialog):
        if not OutputDialog.objectName():
            OutputDialog.setObjectName(u"OutputDialog")
        OutputDialog.resize(951, 591)
        OutputDialog.setMinimumSize(QSize(0, 0))
        OutputDialog.setMaximumSize(QSize(1280, 720))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setBold(True)
        OutputDialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        OutputDialog.setWindowIcon(icon)
        self.imgLabel = QLabel(OutputDialog)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(10, 10, 640, 480))
        self.imgLabel.setMinimumSize(QSize(4, 0))
        self.imgLabel.setMaximumSize(QSize(640, 480))
        self.horizontalLayoutWidget = QWidget(OutputDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 500, 641, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_verify = QPushButton(self.horizontalLayoutWidget)
        self.btn_verify.setObjectName(u"btn_verify")
        font1 = QFont()
        font1.setFamilies([u"Roboto Condensed Light"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_verify.setFont(font1)
        self.btn_verify.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_verify)

        self.gridLayoutWidget = QWidget(OutputDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(660, 10, 281, 61))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto Condensed Light"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.Date_Label = QLabel(self.gridLayoutWidget)
        self.Date_Label.setObjectName(u"Date_Label")
        font3 = QFont()
        font3.setFamilies([u"Roboto Condensed Light"])
        font3.setPointSize(15)
        font3.setBold(True)
        self.Date_Label.setFont(font3)

        self.gridLayout_2.addWidget(self.Date_Label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.Time_Label = QLabel(self.gridLayoutWidget)
        self.Time_Label.setObjectName(u"Time_Label")
        self.Time_Label.setFont(font3)

        self.gridLayout_2.addWidget(self.Time_Label, 1, 1, 1, 1)

        self.groupBox = QGroupBox(OutputDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(660, 110, 271, 271))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 114, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamilies([u"Roboto Condensed Light"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_3.setFont(font4)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout.addWidget(self.label_5)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(120, 30, 131, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(self.verticalLayoutWidget_2)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setFont(font4)

        self.verticalLayout_2.addWidget(self.NameLabel)

        self.MemberLabel = QLabel(self.verticalLayoutWidget_2)
        self.MemberLabel.setObjectName(u"MemberLabel")
        self.MemberLabel.setFont(font4)

        self.verticalLayout_2.addWidget(self.MemberLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.HoursLabel = QLabel(self.verticalLayoutWidget_2)
        self.HoursLabel.setObjectName(u"HoursLabel")
        self.HoursLabel.setFont(font4)

        self.horizontalLayout_2.addWidget(self.HoursLabel)

        self.MinLabel = QLabel(self.verticalLayoutWidget_2)
        self.MinLabel.setObjectName(u"MinLabel")
        self.MinLabel.setFont(font4)

        self.horizontalLayout_2.addWidget(self.MinLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(OutputDialog)

        QMetaObject.connectSlotsByName(OutputDialog)
    # setupUi

    def retranslateUi(self, OutputDialog):
        OutputDialog.setWindowTitle(QCoreApplication.translate("OutputDialog", u"Face Recognition Attendance App", None))
        self.imgLabel.setText("")
        self.btn_verify.setText(QCoreApplication.translate("OutputDialog", u"Verify Membership", None))
        self.label.setText(QCoreApplication.translate("OutputDialog", u"Date :", None))
        self.Date_Label.setText(QCoreApplication.translate("OutputDialog", u"-", None))
        self.label_2.setText(QCoreApplication.translate("OutputDialog", u"Time :", None))
        self.Time_Label.setText(QCoreApplication.translate("OutputDialog", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("OutputDialog", u"Details", None))
        self.label_3.setText(QCoreApplication.translate("OutputDialog", u"Name : ", None))
        self.label_4.setText(QCoreApplication.translate("OutputDialog", u"Member ID :", None))
        self.label_5.setText(QCoreApplication.translate("OutputDialog", u"Clocked Time : ", None))
        self.NameLabel.setText("")
        self.MemberLabel.setText("")
        self.HoursLabel.setText("")
        self.MinLabel.setText("")
    # retranslateUi

