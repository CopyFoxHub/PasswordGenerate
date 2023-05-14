import sys
import secrets
import webbrowser
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 595)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LabelPass = QtWidgets.QLabel(self.centralwidget)
        self.LabelPass.setGeometry(QtCore.QRect(20, 19, 831, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LabelPass.setFont(font)
        self.LabelPass.setStyleSheet("border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"\n"
"color: rgb(70, 70, 70);\n"
"font: 30pt \"Microsoft Tai Le\";")
        self.LabelPass.setObjectName("LabelPass")
        self.Frame_Settings = QtWidgets.QLabel(self.centralwidget)
        self.Frame_Settings.setGeometry(QtCore.QRect(20, 130, 301, 261))
        self.Frame_Settings.setStyleSheet("border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Frame_Settings.setText("")
        self.Frame_Settings.setObjectName("Frame_Settings")
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_Start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Start.setGeometry(QtCore.QRect(20, 470, 301, 91))
        self.Button_Start.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Button_Start.setObjectName("Button_Start")
        self.Box_LowerPas = QtWidgets.QCheckBox(self.centralwidget)
        self.Box_LowerPas.setGeometry(QtCore.QRect(40, 240, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Box_LowerPas.setFont(font)
        self.Box_LowerPas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Box_LowerPas.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 15pt \"Microsoft Tai Le\";")
        self.Box_LowerPas.setIconSize(QtCore.QSize(16, 16))
        self.Box_LowerPas.setObjectName("Box_LowerPas")
        self.Spin_LenPassword = QtWidgets.QSpinBox(self.centralwidget)
        self.Spin_LenPassword.setGeometry(QtCore.QRect(210, 320, 71, 41))
        self.Spin_LenPassword.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 15pt \"Microsoft Tai Le\";")
        self.Spin_LenPassword.setMinimum(6)
        self.Spin_LenPassword.setMaximum(100)
        self.Spin_LenPassword.setProperty("value", 15)
        self.Spin_LenPassword.setObjectName("Spin_LenPassword")
        self.Label_LenPassword = QtWidgets.QLabel(self.centralwidget)
        self.Label_LenPassword.setGeometry(QtCore.QRect(40, 320, 161, 41))
        self.Label_LenPassword.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 15pt \"Microsoft Tai Le\";")
        self.Label_LenPassword.setObjectName("Label_LenPassword")
        self.Box_OnlyLetter = QtWidgets.QCheckBox(self.centralwidget)
        self.Box_OnlyLetter.setGeometry(QtCore.QRect(40, 280, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Box_OnlyLetter.setFont(font)
        self.Box_OnlyLetter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Box_OnlyLetter.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 15pt \"Microsoft Tai Le\";")
        self.Box_OnlyLetter.setIconSize(QtCore.QSize(16, 16))
        self.Box_OnlyLetter.setObjectName("Box_OnlyLetter")
        self.Label_YourPass = QtWidgets.QLabel(self.centralwidget)
        self.Label_YourPass.setGeometry(QtCore.QRect(350, 130, 481, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Label_YourPass.setFont(font)
        self.Label_YourPass.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Label_YourPass.setObjectName("Label_YourPass")
        self.Frame_Password = QtWidgets.QLabel(self.centralwidget)
        self.Frame_Password.setGeometry(QtCore.QRect(350, 230, 481, 161))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Frame_Password.setFont(font)
        self.Frame_Password.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Frame_Password.setText("")
        self.Frame_Password.setObjectName("Frame_Password")
        self.Text_Password = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text_Password.setGeometry(QtCore.QRect(370, 250, 441, 121))
        self.Text_Password.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Text_Password.setObjectName("Text_Password")
        self.Button_Settings = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Settings.setGeometry(QtCore.QRect(20, 130, 301, 91))
        self.Button_Settings.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Button_Settings.setObjectName("Button_Settings")
        self.Button_GitHub = QtWidgets.QPushButton(self.centralwidget)
        self.Button_GitHub.setGeometry(QtCore.QRect(670, 470, 161, 91))
        self.Button_GitHub.setStyleSheet("color: rgb(70, 70, 70);\n"
"font: 20pt \"Microsoft Tai Le\";\n"
"\n"
"border-color: rgb(70, 70, 70);\n"
"border-radius: 40px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.Button_GitHub.setObjectName("pushButton")
        self.Button_CopyText = QtWidgets.QPushButton(self.centralwidget)
        self.Button_CopyText.setGeometry(QtCore.QRect(330, 470, 181, 91))
        self.Button_CopyText.setStyleSheet("color: rgb(70, 70, 70);\n"
                                           "font: 20pt \"Microsoft Tai Le\";\n"
                                           "\n"
                                           "border-color: rgb(70, 70, 70);\n"
                                           "border-radius: 40px;\n"
                                           "border-style: solid;\n"
                                           "border-width: 2px;")
        self.Button_CopyText.setObjectName("Button_CopyText")
        self.Button_CopyText.setObjectName("Button_CopyText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Окно
        pixmap = QtGui.QPixmap(255, 255)
        pixmap.fill(QtGui.QColor(0, 0, 0, 0))
        MainWindow.setWindowIcon(QtGui.QIcon(pixmap))
        MainWindow.setWindowTitle(" ")

        # Переменные состояния
        self.settings = True
        self.lower_password = False
        self.only_letters_password = False

        # Добавление функций для кнопок
        self.add_settings()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabelPass.setText(_translate("MainWindow", "        •Генератор случайных паролей•"))
        self.Button_Start.setText(_translate("MainWindow", "Сгенерировать"))
        self.Box_LowerPas.setText(_translate("MainWindow", "Только нижний регистр"))
        self.Label_LenPassword.setText(_translate("MainWindow", "• Длина пароля:"))
        self.Box_OnlyLetter.setText(_translate("MainWindow", "Только буквы и цифры"))
        self.Label_YourPass.setText(_translate("MainWindow", "                      Ваш пароль"))
        self.Text_Password.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Tai Le\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Button_Settings.setText(_translate("MainWindow", "Настройки"))
        self.Button_GitHub.setText(_translate("MainWindow", "GitHub"))
        self.Button_CopyText.setText(_translate("MainWindow", "Скопировать"))

    def add_settings(self):
        """Функционал всех элементов"""

        # Генерация пароля
        self.Button_Start.clicked.connect(self.generate_password)

        # Включение и выключение настроек
        self.Button_Settings.clicked.connect(self.show_settings)

        # Ссылка на GitHub
        self.Button_GitHub.clicked.connect(self.show_github)

        # Копирование пароля
        self.Button_CopyText.clicked.connect(self.copy_text)

        # Флажки на кнопках
        self.Box_LowerPas.clicked.connect(self.set_lower)
        self.Box_OnlyLetter.clicked.connect(self.set_only_letters)

    def set_lower(self):
        """Установка регистра"""

        # Инверсия параметра регистра для пароля
        self.lower_password = False if self.lower_password else True

    def set_only_letters(self):
        """Только буквы в пароле"""

        # Инверсия параметра "Только буквы" для пароля
        self.only_letters_password = False if self.only_letters_password else True

    def generate_password(self):
        """Генерация пароля"""

        # Изменение надписи о пароле
        self.Label_YourPass.setText("                      Ваш пароль")

        # Количество символов в пароле
        password_len = self.Spin_LenPassword.value()

        # Алфавит для данных настроек
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        if not self.lower_password:
            alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if not self.only_letters_password:
            alphabet += "!@#$%^&*()-_+=;./?\|~[]{}"

        # Генерация пароля для данных настроек
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(password_len))

            # Если пароль соответствует всем параметрам, то он принимается
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password) != self.lower_password
                    and any(c in "!@#$%^&*()-_+=;./?\|~[]{}" for c in password) != self.only_letters_password
                    and sum(c.isdigit() for c in password) >= 3):
                break

        # Вывод пароля
        self.Text_Password.setText(password)

    def show_settings(self):
        """Включение и выключение плашки"""

        # При включенных виджетах
        if self.settings:

            # Выключение виджетов
            self.Spin_LenPassword.hide()
            self.Label_LenPassword.hide()
            self.Box_OnlyLetter.hide()
            self.Box_LowerPas.hide()
            self.Frame_Settings.hide()

            # Изменение переменной настроек
            self.settings = False

        #  При выключенных виджетах
        else:
            # Включение виджетов
            self.Spin_LenPassword.show()
            self.Label_LenPassword.show()
            self.Box_OnlyLetter.show()
            self.Box_LowerPas.show()
            self.Frame_Settings.show()

            # Изменение переменной настроек
            self.settings = True

    def show_github(self):
        """Ссылка на мой GitHub"""

        webbrowser.open("https://github.com/CopyFoxHub")

    def copy_text(self):
        """Копирование пароля в буфер обмена"""

        # Если пароль сгенерирован
        if self.Text_Password.toPlainText():

            # Новая надпись
            self.Label_YourPass.setText("                     Скопировано")

            # Копирование текста
            pyperclip.copy(self.Text_Password.toPlainText())

        # Если пароля ещё нет
        else:
            self.Label_YourPass.setText("            Пароль ещё не создан")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
