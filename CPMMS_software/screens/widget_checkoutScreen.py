from PySide6.QtWidgets import QHeaderView, QTableWidgetItem, QPushButton
from PySide6.QtCore import Qt
from DB.connectionDB import FirebaseAccessor
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

    memID = self.lbl_currentMem.text()
    if not memID:
        self.lbl_member_status.setText("Member: <span style='color: rgba(215,41,41,255);'>NO</span>")
        self.lbl_total_pts.setText("")
    else:
        self.btn_usepts.setEnabled(True)
        mem_data = FirebaseAccessor('Member').read(memID)
        self.lbl_member_status.setText("Member: <span style='color: rgba(41,156,39,255);'>YES</span>")
        self.lbl_total_pts.setText("Total points: "+mem_data['points'])

def addItem(self, item_data):
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

    qty = QTableWidgetItem("1")
    qty.setTextAlignment(Qt.AlignCenter)
    table.setItem(rowcount, 3, qty)

    # cancel
    btn_cancel = QPushButton("X")
    btn_cancel.setStyleSheet("color: red; font-weight: bold;")
    table.setCellWidget(rowcount, 4, btn_cancel)

    # set total price
    self.total += item_data['price']
    self.lbl_total.setText("Total: RM"+str("{:.2f}".format(self.total)))
    