import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import Qt
from calculator import Ui_MainWindow

class appC(qtw.QMainWindow):
    def __init__(self):
        self.num1 = 0
        self.num2 = False

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Yuzde.clicked.connect(self.percentageFunc)
        self.ui.clear.clicked.connect(self.press)
        self.ui.back.clicked.connect(self.press)
        self.ui.zero.clicked.connect(self.press)
        self.ui.one.clicked.connect(self.press)
        self.ui.two.clicked.connect(self.press)
        self.ui.three.clicked.connect(self.press)
        self.ui.four.clicked.connect(self.press)
        self.ui.five.clicked.connect(self.press)
        self.ui.six.clicked.connect(self.press)
        self.ui.seven.clicked.connect(self.press)
        self.ui.eight.clicked.connect(self.press)
        self.ui.nine.clicked.connect(self.press)
        self.ui.multiplication.clicked.connect(self.math)
        self.ui.division.clicked.connect(self.math)
        self.ui.substraction.clicked.connect(self.math)
        self.ui.addition.clicked.connect(self.math)
        self.ui.result.clicked.connect(self.calc)
        self.ui.sign.clicked.connect(self.signFunc)
        self.ui.dot.clicked.connect(self.dotFunc)
        

        self.ui.addition.setCheckable(True)
        self.ui.multiplication.setCheckable(True)
        self.ui.division.setCheckable(True)
        self.ui.substraction.setCheckable(True)
        self.ui.result.setCheckable(True)
        
    def press(self):
        # assign pressing result to text and add it to previous
        button = self.sender()
        if ((self.num2) and (self.ui.result.isChecked())):
            self.ui.resultWindow.setText(format(float(button.text()),'.15g'))
            self.num2 = True
            self.ui.result.setChecked(False)
        elif (((self.ui.addition.isChecked()) or (self.ui.division.isChecked()) or (self.ui.substraction.isChecked()) or (self.ui.multiplication.isChecked())) and (not self.num2)):
            self.ui.resultWindow.setText(format(float(button.text()),'.15g'))
            self.num2 = True
        else:
            if (('.' in self.ui.resultWindow.text()) and button.text() == '0'):
                self.ui.resultWindow.setText(format(self.ui.resultWindow.text() + button.text()))
            else:
                self.ui.resultWindow.setText(format(float(self.ui.resultWindow.text() + button.text()), '.15g'))
        
    def dotFunc(self):
        if "." not in self.ui.resultWindow.text():
            self.ui.resultWindow.setText(self.ui.resultWindow.text() + '.')
    def signFunc(self):
        value = float(self.ui.resultWindow.text())*(-1)
        self.ui.resultWindow.setText(format(value,'.15g'))
    def percentageFunc(self):
        value = float(self.ui.resultWindow.text())*(0.01)
        self.ui.resultWindow.setText(format(value,'.15g'))

    def clearFunc(self):
        self.num1 = 0
        self.num2 = False
        self.ui.resultWindow.setText("0")

        self.ui.addition.setChecked(False)
        self.ui.multiplication.setChecked(False)
        self.ui.substraction.setChecked(False)
        self.ui.division.setChecked(False)
        self.ui.result.setChecked(False)
    def math(self):
        button = self.sender()
        self.num1 = float(self.ui.resultWindow.text())
        button.setChecked(True)

    def calc(self):
        self.num2 = float(self.ui.resultWindow.text())
        if self.ui.addition.isChecked():
            newValue = self.num1 + self.num2
            self.ui.resultWindow.setText(format(newValue,'.15g'))
            self.ui.addition.setChecked(False)

        elif self.ui.substraction.isChecked():
            newValue = self.num1 - self.num2
            self.ui.resultWindow.setText(format(newValue,'.15g'))
            self.ui.substraction.setChecked(False)

        elif self.ui.multiplication.isChecked():
            newValue = self.num1 * self.num2
            self.ui.resultWindow.setText(format(newValue,'.15g'))
            self.ui.multiplication.setChecked(False)

        elif self.ui.division.isChecked():
            newValue = self.num1 / self.num2
            self.ui.resultWindow.setText(format(newValue,'.15g'))
            self.ui.division.setChecked(False)

        self.num1 = newValue
        self.ui.result.setChecked(True)

def appF():
    appF = qtw.QApplication(sys.argv)
    win = appC()
    win.show()
    sys.exit(appF.exec_())

appF()