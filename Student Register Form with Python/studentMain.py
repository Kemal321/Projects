from PyQt5 import QtWidgets as qtw
import sys
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt
from student import Ui_MainWindow


class MainApp(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.birthPlace.addItems(['Adana', 'Adiyaman', 'Afyonkarahisar', 'Agri', 'Aksaray', 'Amasya', 'Ankara', 'Antalya', 'Ardahan', 'Artvin', 'Aydin', 'Balikesir', 'Bartin', 'Batman', 'Bayburt', 'Bilecik', 'Bingol', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Canakkale', 'Cankiri', 'Corum', 'Denizli', 'Diyarbakir', 'Duzce', 'Edirne', 'Elazig', 'Erzincan', 'Erzurum', 'Eskisehir', 'Gaziantep', 'Giresun', 'Gumushane', 'Hakkari', 'Hatay', 'Igdir', 'Isparta', 'Istanbul', 'Izmir', 'Kahramanmaras', 'Karabuk', 'Karaman', 'Kars', 'Kastamonu', 'Kayseri', 'Kilis', 'Kirikkale', 'Kirklareli', 'Kirsehir', 'Kocaeli', 'Konya', 'Kutahya', 'Malatya', 'Manisa', 'Mardin', 'Mersin', 'Mugla', 'Mus', 'Nevsehir', 'Nigde', 'Ordu', 'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Sanliurfa', 'Siirt', 'Sinop', 'Sivas', 'Sirnak', 'Tekirdag', 'Tokat', 'Trabzon', 'Tunceli', 'Usak', 'Van', 'Yalova', 'Yozgat', 'Zonguldak'])
        self.ui.department.addItems(["Mechanical Engineering",
                                    "Industrial Engineering",
                                    "Mechatronics Engineering",
                                    "Computer Engineering",
                                    "Electrical Engineering",
                                    "Electronics and Communications Engineering",
                                    "Biomedical Engineering",
                                    "Control and Automation Engineering",
                                    "Civil Engineering",
                                    "Environmental Engineering",
                                    "Geomatic Engineering"
                                    "Chemical Engineering",
                                    "Metallurgical and Materials Engineering",
                                    "Mathematical Engineering",
                                    "Bioengineering",
                                    "Food Engineering",
                                    "Business Administration",
                                    "Economics",
                                    "Political Science and International Relations",
                                    "Architecture",
                                    "City and Regional Planning",
                                    "Conservation and Restoration of Cultural Property",
                                    "Naval Architecture and Marine Engineering",
                                    "Marine Engineering Operations"])
        self.ui.registerAdding.clicked.connect(self.registerAddingFunc)
        self.ui.registerDeleting.clicked.connect(self.registerDeletingFunc)

    def registerAddingFunc(self):
        name=self.ui.name.text()
        surname = self.ui.surname.text()
        tcNo=self.ui.tcnum.text()

        genderGroup = self.ui.Gender.findChildren(qtw.QRadioButton)
        for i in genderGroup:
            if i.isChecked():
                gender = i.text()

        educGroup = self.ui.EducType.findChildren(qtw.QRadioButton)
        for i in educGroup:
            if i.isChecked():
                eductype = i.text()
        
        birthplace = self.ui.birthPlace.currentText()
        departmentT = self.ui.department.currentText()
        dDate = self.ui.calendarWidget.selectedDate().toString("dd-MM-yyyy")

        numberOfRows = self.ui.tableWidget.rowCount()-1

        self.ui.tableWidget.setItem(numberOfRows,0,QTableWidgetItem(name))
        self.ui.tableWidget.setItem(numberOfRows,1,QTableWidgetItem(surname))
        self.ui.tableWidget.setItem(numberOfRows,2,QTableWidgetItem(tcNo))
        self.ui.tableWidget.setItem(numberOfRows,3,QTableWidgetItem(gender))
        self.ui.tableWidget.setItem(numberOfRows,4,QTableWidgetItem(eductype))
        self.ui.tableWidget.setItem(numberOfRows,5,QTableWidgetItem(birthplace))
        self.ui.tableWidget.setItem(numberOfRows,6,QTableWidgetItem(departmentT))
        self.ui.tableWidget.setItem(numberOfRows,7,QTableWidgetItem(dDate))

        self.ui.tableWidget.insertRow(numberOfRows + 1)

    def registerDeletingFunc(self):
        selectedRow = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(selectedRow)


def app():
    app = qtw.QApplication(sys.argv)
    win=MainApp()
    win.show()
    sys.exit(app.exec_())

app()