# File: main.py
import sys
from PySide6 import QtWidgets
from screens.main_loginScreen import MainWindowLoginScreen
from DB.connectionDB import FirebaseAccessor, FirebaseMutator, FirebaseStorage
import datetime

# update folder ImagesMembers
storage_date_data = FirebaseAccessor('FBStorage').read('storageupdate')
storage_update_date = FirebaseMutator('FBStorage')
if storage_date_data['last_update'] > storage_date_data['last_retrieve']:
    firebase_storage = FirebaseStorage()
    firebase_storage.download_folder("img", "ImagesMembers")
    storage_date_data['last_update']
    new_date = {'last_retrieve': datetime.datetime.now().astimezone(None)}
    storage_update_date.update("storageupdate", new_date)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowLoginScreen()
    window.show()
    sys.exit(app.exec())