from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Slot
from DB.connectionDB import FirebaseAccessor
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

class TextInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input barcode")

        layout = QVBoxLayout(self)

        self.text_edit = QLineEdit(self)
        regexDigit = QRegularExpression(r"\d*")
        validator = QRegularExpressionValidator(regexDigit)
        self.text_edit.setValidator(validator)
        
        layout.addWidget(self.text_edit)

        self.label = QLabel(self)
        self.label.setStyleSheet("color: red;")
        layout.addWidget(self.label)

        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)

    def on_submit(self):
        # check item in db
        hasItem = False
        get_items = FirebaseAccessor('Inventory').read_all()
        for item in get_items:
            if self.text_edit.text() == item['barcode']:
                self.item_data = item
                hasItem = True
                self.accept()
                break
        if hasItem == False:
            self.label.setText("Item not found!")

    @Slot()
    def reset(self):
        self.text_edit.setText("")
        self.label.setText("")
