<<<<<<< HEAD

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
class Calculator(QWidget):
    def __init__(self, parent=None):
         super().__init__(parent)
         self.interfejs()
    def interfejs(self):
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
         addBtn = QPushButton("Add", self)
         substractBtn = QPushButton("Substract", self)
         multiplicateBtn = QPushButton("Multiplicate", self)
         endBtn = QPushButton("End", self)
         endBtn.resize(endBtn.sizeHint())

         self.setLayout(layoutT)
         self.setGeometry(20, 20, 300, 100)
         self.setWindowIcon(QIcon('calculator.png'))
         self.setWindowTitle("Graphic calc")
         self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = calculator()
    sys.exit(app.exec_())
=======
print ("derk")
>>>>>>> 40a29f2a7fa550f48e51a09afd296e43f8301a16
