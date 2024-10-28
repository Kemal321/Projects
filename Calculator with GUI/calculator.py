from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 440)
        MainWindow.setMinimumSize(QtCore.QSize(370, 440))
        MainWindow.setMaximumSize(QtCore.QSize(370, 440))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.centralwidget.setObjectName("centralwidget")
        self.resultWindow = QtWidgets.QLabel(self.centralwidget)
        self.resultWindow.setGeometry(QtCore.QRect(1, 1, 369, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.resultWindow.setFont(font)
        self.resultWindow.setStyleSheet("color: rgb(0, 141, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.resultWindow.setFrameShape(QtWidgets.QFrame.Box)
        self.resultWindow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.resultWindow.setLineWidth(2)
        self.resultWindow.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultWindow.setObjectName("resultWindow")
        self.Yuzde = QtWidgets.QPushButton(self.centralwidget)
        self.Yuzde.setGeometry(QtCore.QRect(10, 90, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Yuzde.setFont(font)
        self.Yuzde.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.Yuzde.setObjectName("Yuzde")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(100, 90, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.clear.setObjectName("clear")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(190, 90, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.back.setObjectName("back")
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(280, 90, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.division.setFont(font)
        self.division.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.division.setObjectName("division")
        self.multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication.setGeometry(QtCore.QRect(280, 160, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.multiplication.setFont(font)
        self.multiplication.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.multiplication.setObjectName("multiplication")
        self.substraction = QtWidgets.QPushButton(self.centralwidget)
        self.substraction.setGeometry(QtCore.QRect(280, 230, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.substraction.setFont(font)
        self.substraction.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.substraction.setObjectName("substraction")
        self.addition = QtWidgets.QPushButton(self.centralwidget)
        self.addition.setGeometry(QtCore.QRect(280, 300, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addition.setFont(font)
        self.addition.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.addition.setObjectName("addition")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(280, 370, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.result.setObjectName("result")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 160, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(100, 160, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(190, 160, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(100, 230, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(190, 230, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 230, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 300, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.sign = QtWidgets.QPushButton(self.centralwidget)
        self.sign.setGeometry(QtCore.QRect(10, 370, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sign.setFont(font)
        self.sign.setStyleSheet("background-color: rgb(190, 127, 0);")
        self.sign.setObjectName("sign")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(100, 300, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(100, 370, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(190, 370, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(190, 300, 80, 64))
        font = QtGui.QFont()
        font.setFamily("Marcellus")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.three.setFont(font)
        self.three.setObjectName("three")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.resultWindow.setText(_translate("MainWindow", "0"))
        self.Yuzde.setText(_translate("MainWindow", "%"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.back.setText(_translate("MainWindow", "←"))
        self.division.setText(_translate("MainWindow", "÷"))
        self.multiplication.setText(_translate("MainWindow", "x"))
        self.substraction.setText(_translate("MainWindow", "-"))
        self.addition.setText(_translate("MainWindow", "+"))
        self.result.setText(_translate("MainWindow", "="))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.four.setText(_translate("MainWindow", "4"))
        self.one.setText(_translate("MainWindow", "1"))
        self.sign.setText(_translate("MainWindow", "+/-"))
        self.two.setText(_translate("MainWindow", "2"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.three.setText(_translate("MainWindow", "3"))
