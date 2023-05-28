from PySide6.QtWidgets import QDialog, QLabel, QSpinBox, QVBoxLayout, QPushButton
from PySide6.QtCore import Slot
from DB.connectionDB import FirebaseAccessor

# Create the QDialog subclass
class UsePoints(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Use member points")
    
    @Slot()
    def usePtsScreen(self, memID):
        # Check if layout exists, create a new one if not
        if not self.layout():
            self.setLayout(QVBoxLayout())

        # Clear the layout
        while self.layout().count():
            item = self.layout().takeAt(0)
            widgetItem = item.widget()
            if widgetItem:
                widgetItem.deleteLater()

        label = QLabel("Use points (1000pts for RM5 discount)")
        self.layout().addWidget(label)

        get_member_pts = FirebaseAccessor('Member').read(memID)['points']
        
        if int(get_member_pts) < 1000:
            label2 = QLabel("Insufficient member points")
            label2.setStyleSheet("color: red;")
            self.layout().addWidget(label2)
        else:
            max = int(get_member_pts) // 1000
            self.spin_box = DisabledSpinBox(self)
            self.spin_box.setRange(1000, max * 1000)
            self.spin_box.setSingleStep(1000)
            self.layout().addWidget(self.spin_box)
            button = QPushButton("Submit")
            button.clicked.connect(self.on_submit)
            self.layout().addWidget(button)

        self.setFixedSize(250, 100)

    def on_submit(self):
        self.member_pts = self.spin_box.value()
        self.accept()

class DisabledSpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def keyPressEvent(self, event):
        # Ignore keyboard input
        event.ignore()