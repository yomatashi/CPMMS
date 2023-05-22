from DB.connectionDB import FirebaseAuthentication, FirebaseAccessor, FirebaseMutator
from PySide6.QtWidgets import QMessageBox

def editProfile(self):
    self.stackedWidget.setCurrentWidget(self.adminProfile)
    get_current_email = FirebaseAuthentication.getAuthEmail()
    get_admin = FirebaseAccessor('Admin').read_all_with_id()
    for admin in get_admin:
        if admin['data']['email'] ==  get_current_email:
            current_user = admin
    self.input_fullName_admin.setText(current_user['data']['fullName'])
    self.lbl_admin_email.setText(current_user['data']['email'])
    self.lbl_adminID.setText(current_user['id'])
    self.input_jobPosition.setCurrentText(current_user['data']['position'])

def updateProfile(self):
    fullName = self.input_fullName_admin.text()
    email = self.lbl_admin_email.text()
    position = self.input_jobPosition.currentText()
    adminID = self.lbl_adminID.text()

    update_admin = FirebaseMutator('Admin')
    update_data = {'email': email, 'fullName': fullName, 'position': position}
    update_admin.update(adminID, update_data)
    ret = QMessageBox.information(self, "Updated", "Admin information successfully updated.", QMessageBox.Ok)
    if ret == QMessageBox.Ok:
        self.name_label.setText(fullName)
        self.position_label.setText(position)