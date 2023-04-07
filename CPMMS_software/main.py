# File: main.py
import sys
from PySide6 import QtWidgets
from screens.widget_memberVerificationScreen import WidgetMemberVerificationScreen
from DB.connectionDB import FirebaseAccessor
from DB.connectionDB import FirebaseMutator
from DB.connectionDB import FirebaseStorage
import datetime

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent=parent)
#         ui = Ui_MainWindow() insert main window class
#         ui.setupUi(self)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.setWindowTitle("CPMMS")
#     window.show()
#     sys.exit(app.exec())

# update folder ImagesMembers
storage_date_data = FirebaseAccessor('FBStorage').read('storageupdate')
storage_update_date = FirebaseMutator('FBStorage')
if storage_date_data['last_update'] > storage_date_data['last_retrieve']:
    firebase_storage = FirebaseStorage()
    firebase_storage.download_folder("img", "ImagesMembers")
    storage_date_data['last_update']
    new_date = {'last_retrieve': datetime.datetime.now().astimezone(None)}
    storage_update_date.update("storageupdate", new_date)

# create QApplication then connect to QWidget
app = QtWidgets.QApplication(sys.argv)
window = WidgetMemberVerificationScreen()
# window.setWindowTitle("CPMMS")
window.show()
sys.exit(app.exec())