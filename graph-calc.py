from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    def __init__(self, parent=None):
         super().__init__(parent)
         self.interface()
    def interface(self):
         self.resize(300, 100)
         self.setWindowTitle("calculator")
         self.show()
         label1 = QLabel("Number 1:", self)
         label2 = QLabel("Number 2:", self)
         label3 = QLabel("Result:", self)
         layoutT =QGridLayout()
         layoutT.addWidget(label1, 0, 0)
         layoutT.addWidget(label2, 0, 1)
         layoutT.addWidget(label3, 0, 2)
         self.number1Edt = QLineEdit()
         self.number2Edt = QLineEdit()
         self.resultEdt = QLineEdit()
         self.resultEdt.readonly = True
         self.resultEdt.setToolTip("Write <b>number</b> and choose equation...")
         layoutT.addWidget(self.number1Edt, 1, 0)
         layoutT.addWidget(self.number2Edt, 1, 1)
         layoutT.addWidget(self.resultEdt, 1, 2)
         addBtn = QPushButton("&Add", self)
         substractBtn = QPushButton("&Substract", self)
         multiplicateBtn = QPushButton("&Multiplicate", self)
         divisionBtn = QPushButton("&Division", self)
         endBtn = QPushButton("&End", self)
         endBtn.resize(endBtn.sizeHint())
         layoutH = QHBoxLayout()
         layoutH.addWidget(addBtn)
         layoutH.addWidget(substractBtn)
         layoutH.addWidget(multiplicateBtn)
         layoutH.addWidget(divisionBtn)
         layoutT.addLayout(layoutH, 2, 0, 1, 3)
         layoutT.addWidget(endBtn, 3, 0, 1, 3)
         self.setLayout(layoutT)
         endBtn.clicked.connect(self.end)
         self.setGeometry(20, 20, 300, 100)
         self.setWindowIcon(QIcon('calculator.png'))
         self.setWindowTitle("Graphic calc")
         self.show()
    def end(self):
        self.close()
    def closeEvent(self, event):
        ans = QMessageBox.question(
            self, "Message",
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox
            if ans == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        )

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
