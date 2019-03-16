from backend import *
from form import *
from PyQt5 import QtWidgets, QtCore

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.labels = [self.ui.label_4, self.ui.label_5, self.ui.label_6, self.ui.label_7]
        self.lines = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4]

        self.load_base()
        self.load_ids()

        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.groupBox_4.hide()

        self.ui.actionExit.triggered.connect(sys.exit)
        self.ui.pushButton.clicked.connect(self.add)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.ui.pushButton_3.clicked.connect(self.edit)
        self.ui.pushButton_5.clicked.connect(self.add_apply)
        self.ui.pushButton_6.clicked.connect(self.delete_apply)
        self.ui.pushButton_7.clicked.connect(self.edit_apply)

    def load_base(self):
        result = sql_select()
        self.ui.tableWidget.setRowCount(len(result))
        header = self.ui.tableWidget.horizontalHeader()
        for i in range(len(result)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem()
                item.setText("{}".format(result[i][j]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(i, j, item)
                header.setSectionResizeMode(j, QtWidgets.QHeaderView.ResizeToContents)

    def load_ids(self):
        result = sql_select()
        self.ui.comboBox.clear()
        for i in range(len(result)):
            self.ui.comboBox.addItem("")
            self.ui.comboBox.setItemText(i, "{}".format(i+1))

    def if_zero(self):
        result = sql_select()
        if len(result) == 0:
            self.ui.groupBox_2.setDisabled(True)
        else:
            self.ui.groupBox_2.setDisabled(False)

    def add(self):
        self.group_box_3("add new product", True, False)
        self.ui.pushButton_5.show()
        self.ui.pushButton_6.hide()
        self.ui.pushButton_7.hide()

    def delete(self):
        self.if_zero()
        self.group_box_2("deletion by id")
        self.ui.pushButton_4.clicked.connect(self.delete_ok)

    def edit(self):
        self.if_zero()
        self.group_box_2("editing by id")
        self.ui.pushButton_4.clicked.connect(self.edit_ok)

    def delete_ok(self):
        self.group_box_3("deletion information:", False, True)
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.show()
        self.ui.pushButton_7.hide()

    def edit_ok(self):
        self.group_box_3("change information:", False, False)
        self.ui.pushButton_5.hide()
        self.ui.pushButton_6.hide()
        self.ui.pushButton_7.show()

    def add_apply(self):
        input_name = self.lines[0].text()
        input_price = self.lines[1].text()
        input_link = self.lines[2].text()
        input_note = self.lines[3].text()
        sql_insert(input_name, input_price, input_link, input_note)
        self.refresh()

    def delete_apply(self):
        delete_id = self.ui.comboBox.currentIndex() + 1
        sql_delete(delete_id)
        auto_inc()
        self.refresh()

    def edit_apply(self):
        current_id = self.ui.comboBox.currentIndex() + 1
        new_name = self.lines[0].text()
        new_price = self.lines[1].text()
        new_link = self.lines[2].text()
        new_note = self.lines[3].text()
        sql_update(current_id, new_name, new_price, new_link, new_note)
        self.refresh()

    def refresh(self):
        self.load_base()
        self.load_ids()
        self.update()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.groupBox_4.hide()

    def group_box_2(self, lbl):
        self.ui.groupBox_2.show()
        self.ui.groupBox_3.hide()
        self.ui.groupBox_4.hide()
        self.ui.label.setText(lbl)
        self.ui.comboBox.setEnabled(True)
        self.ui.comboBox.setCurrentIndex(0)

    def group_box_3(self, lbl3, flag, read):
        self.ui.groupBox_3.show()
        self.ui.groupBox_4.show()
        self.ui.label_3.setText(lbl3)
        if flag:
            self.ui.groupBox_2.hide()
            for i in range(len(self.lines)):
                self.lines[i].setText("")
                self.lines[i].setReadOnly(read)
        if not flag:
            result = sql_select()
            ind = self.ui.comboBox.currentIndex()
            self.ui.comboBox.setEnabled(False)
            for i in range(len(self.lines)):
                self.lines[i].setText("{}".format(result[ind][i + 1]))
                self.lines[i].setReadOnly(read)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
