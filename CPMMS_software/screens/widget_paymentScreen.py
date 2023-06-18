from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMessageBox
from DB.connectionDB import FirebaseAccessor, FirebaseMutator
import datetime

def paymentScreen(self):
    self.stackedWidget.setCurrentWidget(self.payment)
    self.lbl_total_pymnt.setText("TOTAL: RM"+str("{:.2f}".format(self.total)))
    self.pymnt_amount.setText(str("{:.2f}".format(self.total)))
    regexAmnt = QRegularExpression(r'^[0-9]+(\.[0-9]{1,2})?$')
    validator = QRegularExpressionValidator(regexAmnt)
    self.pymnt_amount.setValidator(validator)
    # self.pymnt_amount.textChanged.connect(self.updateChange)

def transaction(self):
    if self.pymnt_amount.text() == "" or self.change < 0:
        QMessageBox.warning(self, "Error", "Invalid payment amount value.", QMessageBox.Ok)
    else:
        memID = self.lbl_currentMem.text()
        table = self.tbl_checkout

        if memID:
            purchaseHistory = FirebaseMutator('purchaseHistory')
            items_data = []
            # is member - add points rate rm1 = 1pt
            current_mempts = FirebaseAccessor('Member').read(memID)['points']
            new_pts = current_mempts + (self.total // 1)
            member = FirebaseMutator('Member')
            update_data = {'points': int(new_pts)}
            member.update(memID, update_data)
            # update trackingpts here for +ve pt
            pts_track = FirebaseMutator('PointsTracking')
            new_pts_track = {'date': datetime.datetime.now().astimezone(None), 'memberID': memID, 'name': 'Points earned from purchase', 'pointsDiff': (self.total // 1)}
            pts_track.create_autoID(new_pts_track)
            # update purchase history
            for row in range(table.rowCount()):
                item_data = {'item': table.item(row, 0).text(), 'qty': int(table.cellWidget(row, 3).text())}
                items_data.append(item_data)
            purchase_history_data = {'date': datetime.datetime.now().astimezone(None), 'memberID': memID, 'totalPrice': float("{:.2f}".format(self.total)), 'items': items_data, 'paymentMode': self.pymnt_mode.currentText()}
            purchaseHistory.create_autoID(purchase_history_data)

        
        # table = self.tbl_checkout
        inventory = FirebaseMutator('Inventory')
        
        for row in range(table.rowCount()):
            # update stock of every inventory selected
            barcode = table.item(row, 0).text()
            if not barcode == "-":
                qty = int(table.cellWidget(row, 3).text())
                inv_data_stock = FirebaseAccessor('Inventory').read(barcode)['stock']
                updated_inv_data = {'stock': (inv_data_stock - qty)}
                inventory.update(barcode, updated_inv_data)
            else:
                # update trackingpts here for -ve pt
                qty = int(table.item(row, 3).text())
                # pts_track = FirebaseMutator('PointsTracking')
                new_pts_track = {'date': datetime.datetime.now().astimezone(None), 'memberID': memID, 'name': 'RM5 cash rebate (Member Discount)', 'pointsDiff': -(qty*1000)}
                pts_track.create_autoID(new_pts_track)

        ret = QMessageBox.information(self, "Success", "Successfully paid!", QMessageBox.Ok)
        if ret == QMessageBox.Ok:
            self.clearMember()