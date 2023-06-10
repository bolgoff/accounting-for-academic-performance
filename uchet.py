from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        birth TEXT,
        course TEXT,
        lesson TEXT,
        hours TEXT,
        mark TEXT
)''')

for i in cursor.execute('SELECT * FROM users'):
      print(i)

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(797, 593)
                MainWindow.setMinimumSize(QtCore.QSize(797, 593))
                MainWindow.setMaximumSize(QtCore.QSize(797, 593))
                MainWindow.setStyleSheet("background-color: rgb(70, 84, 100);")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
                self.scrollArea.setGeometry(QtCore.QRect(10, 290, 781, 211))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 323))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.lename_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.lename_1.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.lename_1.setObjectName("lename_1")
                self.verticalLayout_2.addWidget(self.lename_1)
                self.len_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.len_1.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.len_1.setObjectName("len_1")
                self.verticalLayout_2.addWidget(self.len_1)
                self.cb_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.cb_1.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);")
                self.cb_1.setCurrentText("")
                self.cb_1.setObjectName("cb_1")
                self.cb_1.addItem("")
                self.cb_1.addItem("")
                self.cb_1.addItem("")
                self.cb_1.addItem("")
                self.cb_1.addItem("")
                self.cb_1.addItem("")
                self.verticalLayout_2.addWidget(self.cb_1)
                self.lename_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.lename_2.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.lename_2.setObjectName("lename_2")
                self.verticalLayout_2.addWidget(self.lename_2)
                self.len_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.len_2.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.len_2.setObjectName("len_2")
                self.verticalLayout_2.addWidget(self.len_2)
                self.cb_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.cb_2.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);")
                self.cb_2.setCurrentText("")
                self.cb_2.setObjectName("cb_2")
                self.cb_2.addItem("")
                self.cb_2.addItem("")
                self.cb_2.addItem("")
                self.cb_2.addItem("")
                self.cb_2.addItem("")
                self.cb_2.addItem("")
                self.verticalLayout_2.addWidget(self.cb_2)
                self.lename_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.lename_3.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.lename_3.setObjectName("lename_3")
                self.verticalLayout_2.addWidget(self.lename_3)
                self.len_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.len_3.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.len_3.setObjectName("len_3")
                self.verticalLayout_2.addWidget(self.len_3)
                self.cb_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.cb_3.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);")
                self.cb_3.setCurrentText("")
                self.cb_3.setObjectName("cb_3")
                self.cb_3.addItem("")
                self.cb_3.addItem("")
                self.cb_3.addItem("")
                self.cb_3.addItem("")
                self.cb_3.addItem("")
                self.cb_3.addItem("")
                self.verticalLayout_2.addWidget(self.cb_3)
                self.lename_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.lename_4.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.lename_4.setObjectName("lename_4")
                self.verticalLayout_2.addWidget(self.lename_4)
                self.len_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                self.len_4.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.len_4.setObjectName("len_4")
                self.verticalLayout_2.addWidget(self.len_4)
                self.cb_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                self.cb_4.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);")
                self.cb_4.setCurrentText("")
                self.cb_4.setObjectName("cb_4")
                self.cb_4.addItem("")
                self.cb_4.addItem("")
                self.cb_4.addItem("")
                self.cb_4.addItem("")
                self.cb_4.addItem("")
                self.cb_4.addItem("")
                self.verticalLayout_2.addWidget(self.cb_4)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.btn_find = QtWidgets.QPushButton(self.centralwidget)
                self.btn_find.setGeometry(QtCore.QRect(370, 240, 93, 41))
                self.btn_find.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(93, 111, 132);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(112, 128, 144);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(128, 128, 128);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}")
                self.btn_find.setObjectName("btn_find")
                self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.layoutWidget.setGeometry(QtCore.QRect(10, 539, 781, 51))
                self.layoutWidget.setObjectName("layoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.btn_create = QtWidgets.QPushButton(self.layoutWidget)
                self.btn_create.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(93, 111, 132);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(112, 128, 144);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(128, 128, 128);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}")
                self.btn_create.setObjectName("btn_create")
                self.horizontalLayout.addWidget(self.btn_create)
                self.btn_update = QtWidgets.QPushButton(self.layoutWidget)
                self.btn_update.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(93, 111, 132);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(112, 128, 144);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(128, 128, 128);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}")
                self.btn_update.setObjectName("btn_update")
                self.horizontalLayout.addWidget(self.btn_update)
                self.btn_delete = QtWidgets.QPushButton(self.layoutWidget)
                self.btn_delete.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(93, 111, 132);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(112, 128, 144);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(128, 128, 128);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}")
                self.btn_delete.setObjectName("btn_delete")
                self.horizontalLayout.addWidget(self.btn_delete)
                self.btn_add = QtWidgets.QPushButton(self.centralwidget)
                self.btn_add.setGeometry(QtCore.QRect(340, 510, 131, 21))
                self.btn_add.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(93, 111, 132);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(112, 128, 144);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    background-color: rgb(128, 128, 128);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius: 7px;\n"
        "}")
                self.btn_add.setObjectName("btn_add")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(8, 11, 781, 221))
                self.widget.setObjectName("widget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.le_name = QtWidgets.QLineEdit(self.widget)
                self.le_name.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.le_name.setObjectName("le_name")
                self.verticalLayout.addWidget(self.le_name)
                self.le_course = QtWidgets.QLineEdit(self.widget)
                self.le_course.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.le_course.setObjectName("le_course")
                self.verticalLayout.addWidget(self.le_course)
                self.le_birth = QtWidgets.QLineEdit(self.widget)
                self.le_birth.setStyleSheet("background-color: rgb(93, 111, 132);\n"
        "padding-left: 6px;\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 7px;")
                self.le_birth.setObjectName("le_birth")
                self.verticalLayout.addWidget(self.le_birth)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.cb_1.setCurrentIndex(-1)
                self.cb_2.setCurrentIndex(-1)
                self.cb_3.setCurrentIndex(-1)
                self.cb_4.setCurrentIndex(-1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.nums_of_preds = 0

                self.functions()



        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Учет успеваемости студентов"))
                self.lename_1.setText(_translate("MainWindow", "Название предмета"))
                self.len_1.setText(_translate("MainWindow", "Кол-во посещенных часов"))
                self.cb_1.setItemText(0, _translate("MainWindow", "зачтено"))
                self.cb_1.setItemText(1, _translate("MainWindow", "не зачтено"))
                self.cb_1.setItemText(2, _translate("MainWindow", "отлично(5)"))
                self.cb_1.setItemText(3, _translate("MainWindow", "хорошо(4)"))
                self.cb_1.setItemText(4, _translate("MainWindow", "удовлетворительно(3)"))
                self.cb_1.setItemText(5, _translate("MainWindow", "неудовлетворительно(2)"))
                self.lename_2.setText(_translate("MainWindow", "Название предмета"))
                self.len_2.setText(_translate("MainWindow", "Кол-во посещенных часов"))
                self.cb_2.setItemText(0, _translate("MainWindow", "зачтено"))
                self.cb_2.setItemText(1, _translate("MainWindow", "не зачтено"))
                self.cb_2.setItemText(2, _translate("MainWindow", "отлично(5)"))
                self.cb_2.setItemText(3, _translate("MainWindow", "хорошо(4)"))
                self.cb_2.setItemText(4, _translate("MainWindow", "удовлетворительно(3)"))
                self.cb_2.setItemText(5, _translate("MainWindow", "неудовлетворительно(2)"))
                self.lename_3.setText(_translate("MainWindow", "Название предмета"))
                self.len_3.setText(_translate("MainWindow", "Кол-во посещенных часов"))
                self.cb_3.setItemText(0, _translate("MainWindow", "зачтено"))
                self.cb_3.setItemText(1, _translate("MainWindow", "не зачтено"))
                self.cb_3.setItemText(2, _translate("MainWindow", "отлично(5)"))
                self.cb_3.setItemText(3, _translate("MainWindow", "хорошо(4)"))
                self.cb_3.setItemText(4, _translate("MainWindow", "удовлетворительно(3)"))
                self.cb_3.setItemText(5, _translate("MainWindow", "неудовлетворительно(2)"))
                self.lename_4.setText(_translate("MainWindow", "Название предмета"))
                self.len_4.setText(_translate("MainWindow", "Кол-во посещенных часов"))
                self.cb_4.setItemText(0, _translate("MainWindow", "зачтено"))
                self.cb_4.setItemText(1, _translate("MainWindow", "не зачтено"))
                self.cb_4.setItemText(2, _translate("MainWindow", "отлично(5)"))
                self.cb_4.setItemText(3, _translate("MainWindow", "хорошо(4)"))
                self.cb_4.setItemText(4, _translate("MainWindow", "удовлетворительно(3)"))
                self.cb_4.setItemText(5, _translate("MainWindow", "неудовлетворительно(2)"))
                self.btn_find.setText(_translate("MainWindow", "Найти"))
                self.btn_create.setText(_translate("MainWindow", "Создать"))
                self.btn_update.setText(_translate("MainWindow", "Обновить"))
                self.btn_delete.setText(_translate("MainWindow", "Удалить"))
                self.btn_add.setText(_translate("MainWindow", "Добавить предмет"))
                self.le_name.setText(_translate("MainWindow", "ФИО"))
                self.le_course.setText(_translate("MainWindow", "Курс"))
                self.le_birth.setText(_translate("MainWindow", "Дата рождения"))

                

        def functions(self):
            self.btn_find.clicked.connect(self.find_person)
            self.btn_add.clicked.connect(self.add_lesson)
            self.btn_create.clicked.connect(self.add_person)
            self.btn_delete.clicked.connect(self.delete_person)

        def add_lesson(self):
                _translate = QtCore.QCoreApplication.translate
                if self.nums_of_preds == 0 and self.nums_of_preds != 1:
                        #название предмета 5
                        self.lename_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                        self.lename_5.setStyleSheet("background-color: rgb(93, 111, 132);\n"
                "padding-left: 6px;\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius: 7px;")
                        self.lename_5.setObjectName("lename_5")
                        self.verticalLayout_2.addWidget(self.lename_5)
                        self.lename_5.setText(_translate("MainWindow", "Название предмета"))
                        #часы 5
                        self.len_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                        self.len_5.setStyleSheet("background-color: rgb(93, 111, 132);\n"
                "padding-left: 6px;\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius: 7px;")
                        self.len_5.setObjectName("len_5")
                        self.verticalLayout_2.addWidget(self.len_5)
                        self.len_5.setText(_translate("MainWindow", "Кол-во посещенных часов"))
                        #оценка 5
                        self.cb_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
                        self.cb_5.setStyleSheet("background-color: rgb(93, 111, 132);\n"
                "padding-left: 6px;\n"
                "color: rgb(255, 255, 255);")
                        self.cb_5.setCurrentText("")
                        self.cb_5.setObjectName("cb_5")
                        self.cb_5.addItem("")
                        self.cb_5.addItem("")
                        self.cb_5.addItem("")
                        self.cb_5.addItem("")
                        self.cb_5.addItem("")
                        self.cb_5.addItem("")
                        self.verticalLayout_2.addWidget(self.cb_5)
                        self.cb_5.setCurrentIndex(-1)
                        self.cb_5.setItemText(0, _translate("MainWindow", "зачтено"))
                        self.cb_5.setItemText(1, _translate("MainWindow", "не зачтено"))
                        self.cb_5.setItemText(2, _translate("MainWindow", "отлично(5)"))
                        self.cb_5.setItemText(3, _translate("MainWindow", "хорошо(4)"))
                        self.cb_5.setItemText(4, _translate("MainWindow", "удовлетворительно(3)"))
                        self.cb_5.setItemText(5, _translate("MainWindow", "неудовлетворительно(2)"))
                        #увеличение переменной на единицу
                        self.nums_of_preds += 1
                else:
                        error = QMessageBox()

                        error.setWindowTitle("Ошибка")
                        error.setText("Нельзя добавить больше 5 предметов!")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)

                        error.setDetailedText("В настоящий момент можно добавить только 5 предметов")

                        error.exec_()

        def find_person(self):
                name = self.le_name.text()
                res = cursor.execute(f'SELECT birth, course, lesson, hours, mark FROM users WHERE name="{name}"')
                dat = cursor.fetchall()
                if len(dat) == 0:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Студент не найден!")
                        error.setIcon(QMessageBox.Warning)
                        error.setStandardButtons(QMessageBox.Ok)
                        error.exec_()
                else:
                        for i in dat:
                                self.le_birth.setText(i[0])
                                self.le_course.setText(str(i[1]))
                                self.lename_1.setText(i[2])
                                self.len_1.setText(str(i[3]))
                                self.cb_1.setCurrentText(i[4])
                      
        def delete_person(self):
                name = self.le_name.text()
                cursor.execute(f'DELETE FROM users WHERE name="{name}"')
                db.commit()

                info = QMessageBox()

                info.setWindowTitle("Результат")
                info.setText("Данные о студенте были успешно удалены")
                info.setIcon(QMessageBox.Information)
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()

        def update_person(self):
                pass

        def add_person(self):
                name = self.le_name.text()
                birth = self.le_birth.text()
                course = self.le_course.text()
                less = self.lename_1.text()
                hours = self.len_1.text()
                mark = self.cb_1.currentText()


                cursor.execute(f'SELECT name FROM users WHERE name="{name}"')
                if cursor.fetchone() is None:
                        cursor.execute(f'INSERT INTO users VALUES ("{name}", "{birth}", "{course}", "{less}", "{hours}", "{mark}")')
                        db.commit()

                info = QMessageBox()

                info.setWindowTitle("Результат")
                info.setText("Студент был добавлен в базу!")
                info.setIcon(QMessageBox.Information)
                info.setStandardButtons(QMessageBox.Ok)
                info.exec_()                
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())