# File: main.py
import sys
from PySide6 import QtWidgets
from screens.widget_memberVerificationScreen import WidgetMemberVerificationScreen

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

app = QtWidgets.QApplication(sys.argv)
window = WidgetMemberVerificationScreen()
# window.setWindowTitle("CPMMS")
window.show()
sys.exit(app.exec())