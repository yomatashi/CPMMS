import sys

from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtGui import QIcon
from ui_memberVerificationScreen import Ui_Form
from facialRecognitionScreen  import facialRecog

import resources_rc

class WidgetMemberVerificationScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_member_verification.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.verificationMethod))
        self.btn_ic.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ICMethod))
        self.btn_facial_recog.clicked.connect(self.openFacialRecognitionProgram)

        self.facial_recog = facialRecog()
    
    def openFacialRecognitionProgram(self):
        ret = self.facial_recog.exec()
        if(ret == QDialog.Accepted):
            # self.info_label.setText("Your position is " + self.facial_recog.position +
            #                      " and your favorite os is " + self.facial_recog.favorite_os)
            print("Dialog accepted")
        else:
            print("Dialog rejected")