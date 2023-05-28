from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton, QSpinBox
from PySide6.QtCore import Qt
from DB.connectionDB import FirebaseAccessor, FirebaseMutator
import resources_rc

def checkoutScreen(self):
    self.stackedWidget.setCurrentWidget(self.checkout)
    self.total = 0
    self.lbl_total.setText("Total:")
    table = self.tbl_checkout
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.horizontalHeader().setMinimumSectionSize(100)
    table.clearContents()
    table.setRowCount(0)
    self.btn_pay.setEnabled(False)
    self.btn_remove_member.setVisible(False)

    memID = self.lbl_currentMem.text()
    if not memID:
        self.lbl_member_status.setText("Member: <span style='color: rgba(215,41,41,255);'>NO</span>")
        self.lbl_total_pts.setText("")
    else:
        self.btn_usepts.setEnabled(True)
        self.btn_remove_member.setVisible(True)
        mem_data = FirebaseAccessor('Member').read(memID)
        self.lbl_member_status.setText("Member: <span style='color: rgba(41,156,39,255);'>YES</span>")
        self.lbl_total_pts.setText("Total points: "+str(mem_data['points']))

def addItem(self, item_data):
    self.btn_pay.setEnabled(True)
    table = self.tbl_checkout
    rowcount = table.rowCount()

    table.insertRow(rowcount)
    barcode = QTableWidgetItem(item_data['barcode'])
    table.setItem(rowcount, 0, barcode)

    name = QTableWidgetItem(item_data['itemName'])
    table.setItem(rowcount, 1, name)

    price = QTableWidgetItem(str("{:.2f}".format(item_data['price'])))
    price.setTextAlignment(Qt.AlignCenter)
    table.setItem(rowcount, 2, price)

    qty = DisabledSpinBox(self)
    qty.setRange(1, item_data['stock'])
    qty.setKeyboardTracking(False)
    qty.setAlignment(Qt.AlignCenter)
    table.setCellWidget(rowcount, 3, qty)

    # cancel
    btn_cancel = QPushButton("X")
    btn_cancel.setStyleSheet("color: red; font-weight: bold;")
    table.setCellWidget(rowcount, 4, btn_cancel)

    # Connect signals
    qty.valueChanged.connect(self.onchangeqty)
    btn_cancel.clicked.connect(self.cancelrow)

    # set total price
    self.total += item_data['price']
    self.lbl_total.setText("Total: RM"+str("{:.2f}".format(self.total)))

def memberDiscount(self, member_pts):
    memID = self.lbl_currentMem.text()
    get_member_pts = FirebaseAccessor('Member').read(memID)['points']
    new_pts = get_member_pts - member_pts
    member = FirebaseMutator('Member')
    update_data = {'points': new_pts}
    member.update(memID, update_data)
    self.lbl_total_pts.setText("Total points: "+str(new_pts))

    table = self.tbl_checkout
    rowcount = table.rowCount()
    qty = member_pts//1000
    discount = -5.00*qty

    table.insertRow(rowcount)
    table.setItem(rowcount, 0, QTableWidgetItem("-"))
    table.setItem(rowcount, 1, QTableWidgetItem("RM5 cash rebate (Member)"))

    disc_item = QTableWidgetItem(str("{:.2f}".format(discount)))
    disc_item.setTextAlignment(Qt.AlignCenter)
    table.setItem(rowcount, 2, disc_item)

    qty_item = QTableWidgetItem(str(qty))
    qty_item.setTextAlignment(Qt.AlignCenter)
    table.setItem(rowcount, 3, qty_item)

    btn_cancel = QPushButton("X")
    btn_cancel.setStyleSheet("color: red; font-weight: bold;")
    table.setCellWidget(rowcount, 4, btn_cancel)
    btn_cancel.clicked.connect(self.cancelrowDisc)

    # set total price
    self.total += discount
    self.lbl_total.setText("Total: RM"+str("{:.2f}".format(self.total)))

class DisabledSpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def keyPressEvent(self, event):
        # Ignore keyboard input
        event.ignore()