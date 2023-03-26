# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(508, 259)
        Dialog.setMinimumSize(QSize(508, 259))
        Dialog.setMaximumSize(QSize(508, 259))
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.logolabel = QLabel(Dialog)
        self.logolabel.setObjectName(u"logolabel")
        self.logolabel.setGeometry(QRect(0, 0, 500, 133))
        self.logolabel.setPixmap(QPixmap(u":/logo/logo.png"))
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 160, 491, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filelabel = QLabel(self.verticalLayoutWidget)
        self.filelabel.setObjectName(u"filelabel")
        font = QFont()
        font.setFamilies([u"Roboto Condensed"])
        font.setPointSize(14)
        font.setBold(True)
        self.filelabel.setFont(font)

        self.horizontalLayout.addWidget(self.filelabel, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.runButton = QPushButton(self.verticalLayoutWidget)
        self.runButton.setObjectName(u"runButton")
        font1 = QFont()
        font1.setFamilies([u"Roboto Condensed Light"])
        font1.setPointSize(13)
        self.runButton.setFont(font1)

        self.verticalLayout.addWidget(self.runButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Face Recognition Time Attendance App", None))
        self.logolabel.setText("")
        self.filelabel.setText(QCoreApplication.translate("Dialog", u"Face Recognition Time Attendance App", None))
        self.runButton.setText(QCoreApplication.translate("Dialog", u"Start", None))
    # retranslateUi

