from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator, QPixmap, QCursor, Qt
from PySide6.QtWidgets import QFileDialog, QHeaderView, QTableWidgetItem, QPushButton
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
    # clear screen
    self.searchMem.setText("")
    tableMem = self.tbl_memList
    tableMem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    tableMem.horizontalHeader().setMinimumSectionSize(100)

    # display member list
    get_member = FirebaseAccessor('Member').read_all_with_id()
    self.tbl_memList.setRowCount(len(get_member))
    row = 0
    for member in get_member:
        mem_data = member['data']
        id_item = QTableWidgetItem(member['id'])
        tableMem.setItem(row, 0, id_item)

        name_item = QTableWidgetItem(mem_data['fullName'])
        tableMem.setItem(row, 1, name_item)

        IC_item = QTableWidgetItem(mem_data['IC'])
        tableMem.setItem(row, 2, IC_item)

        points_item = QTableWidgetItem(str(mem_data['points']))
        tableMem.setItem(row, 3, points_item)
        row += 1

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

def searchMem(self):
    tableMem = self.tbl_memList
    tableMem.clearContents()
    tableMem.setRowCount(0)

    # display searched member list
    search_input = self.searchMem.text()
    get_member = FirebaseAccessor('Member').read_all_with_id()

    lenCounter = 0
    row = 0
    for member in get_member:
        mem_data = member['data']
        if search_input.lower() in mem_data['fullName'].lower() or search_input in mem_data['IC']:
            lenCounter += 1
            self.tbl_memList.setRowCount(lenCounter)
            mem_data = member['data']
            id_item = QTableWidgetItem(member['id'])
            tableMem.setItem(row, 0, id_item)

            name_item = QTableWidgetItem(mem_data['fullName'])
            tableMem.setItem(row, 1, name_item)

            IC_item = QTableWidgetItem(mem_data['IC'])
            tableMem.setItem(row, 2, IC_item)

            points_item = QTableWidgetItem(str(mem_data['points']))
            tableMem.setItem(row, 3, points_item)
            row += 1

def show_member_details(self):
    selected_items = self.tbl_memList.selectedItems()
    if len(selected_items) == 0:
        return
    row = selected_items[0].row()
    selected_data = self.tbl_memList.item(row, 0).text() if self.tbl_memList.item(row, 0) is not None else ""
    self.stackedWidget.setCurrentWidget(self.editMember)
    memberInfo = FirebaseAccessor('Member').read(selected_data)
    self.input_fullName_edit.setText(memberInfo['fullName'])
    self.input_IC_edit.setText(memberInfo['IC'])
    self.input_email_edit.setText(memberInfo['email'])
    self.lbl_memID.setText(selected_data)
    self.input_pts_edit.setText(str(memberInfo['points']))

def delete_member(self):
    mem_id = self.lbl_memID.text()
    ret = QMessageBox.warning(self, "Delete confirmation", "Are you sure you want to delete this member?", QMessageBox.Yes | QMessageBox.No)
    if ret == QMessageBox.Yes:
        mem_data = FirebaseAccessor('Member').read(mem_id)
        del_msg = FirebaseAuthentication.delete_user_auth(mem_data['email'])
        if del_msg == "Failed to delete user":
            QMessageBox.warning(self, "Error", del_msg, QMessageBox.Ok)
        else:
            firebase_storage = FirebaseStorage()
            new_file_name = mem_data['fullName']+"-"+mem_id+".jpg"
            firebase_storage.delete_file("img", new_file_name)
            FirebaseMutator('Member').delete(mem_id)
            self.stackedWidget.setCurrentWidget(self.listMember)
            QMessageBox.information(self, "Success", "Selected member data deleted!\nPlease refresh member list", QMessageBox.Ok)

def update_member(self):
    fullName = self.input_fullName_edit.text()
    ICnum = self.input_IC_edit.text()
    email = self.input_email_edit.text()
    memberID = self.lbl_memID.text()
    points = self.input_pts_edit.text()
    update_mem = FirebaseMutator('Member')
    update_data = {'email': email, 'fullName': fullName, 'IC': ICnum, 'points': points}
    update_mem.update(memberID, update_data)
    QMessageBox.information(self, "Updated", "Member information successfully updated.", QMessageBox.Ok)