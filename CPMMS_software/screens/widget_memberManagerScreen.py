from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator, QPixmap
from PySide6.QtWidgets import QFileDialog
from DB.connectionDB import FirebaseAuthentication, FirebaseAccessor, FirebaseMutator, FirebaseStorage
from PySide6.QtWidgets import QMessageBox
import datetime
import os
    
# Add member account
def AddMemberScreen(self):
    self.stackedWidget.setCurrentWidget(self.addMember)
    # clear screen
    self.input_fullName_reg.setText("")
    self.input_email_reg.setText("")
    self.input_ICNum_reg.setText("")
    self.input_fileName.setText("")

    self.input_fullName_reg.setPlaceholderText("Full Name")
    self.input_email_reg.setPlaceholderText("Email")
    regexEmail = QRegularExpression(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    validator = QRegularExpressionValidator(regexEmail)
    self.input_email_reg.setValidator(validator)
    self.input_ICNum_reg.setPlaceholderText("IC number")
    regexIC = QRegularExpression("[0-9]{12}")
    validator = QRegularExpressionValidator(regexIC)
    self.input_ICNum_reg.setValidator(validator)

# List members
def ListMemberScreen(self):
    self.stackedWidget.setCurrentWidget(self.listMember)

def browseFile(self):
    pictures_dir = os.path.expanduser("~/Pictures")
    fname = QFileDialog.getOpenFileName(self, "Open File", pictures_dir, "Images (*.png *.xpm *.jpg *.bmp)")

    if fname:
        self.input_fileName.setText(fname[0])

def registerNewMember(self):
    fullName = self.input_fullName_reg.text()
    email = self.input_email_reg.text()
    ICnum = self.input_ICNum_reg.text()
    photoDir = self.input_fileName.text()

    if not all([fullName, email, ICnum]):
        QMessageBox.warning(self, "Error", "Please fill in the empty field(s)", QMessageBox.Ok)
    elif not self.input_email_reg.hasAcceptableInput():
        QMessageBox.warning(self, "Error", "Invalid email address", QMessageBox.Ok)
    elif not self.input_ICNum_reg.hasAcceptableInput():
        QMessageBox.warning(self, "Error", "Invalid IC number", QMessageBox.Ok)
    elif not photoDir:
        QMessageBox.warning(self, "No photo attached", "Please upload a photo of the member's face", QMessageBox.Ok)
    else:
        tryRegister = FirebaseAuthentication.register(email, "cpmmspw123")
        if tryRegister == "Pass":
            Member = FirebaseMutator('Member')
            counter = FirebaseAccessor('counter').read("indices")
            counterUpdate = FirebaseMutator('counter')

            Memberdata = {'email': email, 'fullName': fullName, 'IC': ICnum, 'points': 0}
            Member.create(Memberdata, "mem" + str(counter['mem']+1))
            new_file_name = fullName+"-mem"+str(counter['mem']+1)+".jpg"
            counterUpdate.update("indices", {'mem': counter['mem']+1})

            # send password reset to new user
            tryPwReset = FirebaseAuthentication.send_password_reset_email(email)
            print(tryPwReset)

            # upload photo to firebase storage
            firebase_storage = FirebaseStorage()
            firebase_storage.upload_file(photoDir, "img", new_file_name)
            storage_update_date = FirebaseMutator('FBStorage')
            new_date = {'last_update': datetime.datetime.now().astimezone(None)}
            storage_update_date.update("storageupdate", new_date)

            ret = QMessageBox.information(self, "Success", "New member has been added!\nThe member can now login into Consult Pharmacy mobile application.\nFor member:\nPlease check your email address to reset your password for first time login.", QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                self.input_fullName_reg.setText("")
                self.input_email_reg.setText("")
                self.input_ICNum_reg.setText("")
                self.input_fileName.setText("")
                firebase_storage.download_folder("img", "ImagesMembers")
        else:
            QMessageBox.warning(self, "Failed to register", tryRegister, QMessageBox.Ok)