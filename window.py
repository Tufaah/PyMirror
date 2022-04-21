from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sys import argv, exit
from threading import active_count, Thread
from requests import post
import re
import qdarkstyle


uploaders = 10
main_file_name, main_file_string = '', bytes()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settings/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.resize(401, 672)
        MainWindow.setFixedSize(401, 672)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.path_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.path_textbox.setGeometry(QtCore.QRect(20, 80, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.path_textbox.setFont(font)
        self.path_textbox.setObjectName("path_textbox")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 361, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.done_urls_textbox = QtWidgets.QPlainTextEdit(self.groupBox)
        self.done_urls_textbox.setGeometry(QtCore.QRect(20, 30, 321, 261))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.done_urls_textbox.setFont(font)
        self.done_urls_textbox.setPlainText("")
        self.done_urls_textbox.setObjectName("done_urls_textbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(310, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 120, 361, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.is_custom = QtWidgets.QRadioButton(self.frame)
        self.is_custom.setGeometry(QtCore.QRect(240, 40, 115, 17))
        self.is_custom.setObjectName("is_custom")
        self.custom_textbox = QtWidgets.QTextEdit(self.frame)
        self.custom_textbox.setGeometry(QtCore.QRect(0, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.custom_textbox.setFont(font)
        self.custom_textbox.setObjectName("custom_textbox")
        self.is_auto = QtWidgets.QRadioButton(self.frame)
        self.is_auto.setGeometry(QtCore.QRect(40, 40, 141, 17))
        self.is_auto.setChecked(True)
        self.is_auto.setObjectName("is_auto")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 550, 361, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.done_label = QtWidgets.QLabel(self.frame_2)
        self.done_label.setGeometry(QtCore.QRect(20, 10, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.done_label.setFont(font)
        self.done_label.setObjectName("done_label")
        self.threads_label = QtWidgets.QLabel(self.frame_2)
        self.threads_label.setGeometry(QtCore.QRect(20, 40, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.threads_label.setFont(font)
        self.threads_label.setObjectName("threads_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(20, 190, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(310, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.custom_textbox.setEnabled(False)
        self.start_button.clicked.connect(self.start)
        self.browse_button.clicked.connect(self.browse)
        self.settings_button.clicked.connect(self.settings)

        self.is_custom.clicked.connect(self.show)
        self.is_auto.clicked.connect(self.hide)

    def settings(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Settings tap will be in ( v2.0 )")
        msg.setInformativeText('https://github.com/Tufaah/PyMirror')
        msg.setWindowTitle("Coming soon!")
        msg.exec_()

    def add(self, text):
        self.done_urls_textbox.appendPlainText(text)

    def plus(self, start, end):
        self.done_label.setText(f"Done: ( {start}/{end} )")
        self.done_label.adjustSize()

    def hide(self):
        self.custom_textbox.setEnabled(False)
        self.custom_textbox.clear()

    def show(self):
        self.custom_textbox.setEnabled(True)

    def browse(self):
        file_path = fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select the file', '',)
        self.path_textbox.setText(str(file_path[0]))

    def start(self):
        global main_file_name, main_file_string
        if not self.path_textbox.toPlainText(): print('What')
        else:
            textboxValue = self.path_textbox.toPlainText()
            file = open(textboxValue, 'rb')

            read_file = file.read()
            main_file_string += read_file
            if self.is_custom.isChecked(): main_file_name += self.custom_textbox.toPlainText()
            else: main_file_name += file.name

            file.close()
            self.frame.setEnabled(False)
            self.path_textbox.setEnabled(False)
            self.browse_button.setEnabled(False)
            self.settings_button.setEnabled(False)
            self.start_button.setEnabled(False)

            c = 1
            tasks = [self.anonfiles, self.bayfiles, self.zippyshare, self.usaupload, self.krakenfiles, self.fireload, self.megaup, self.filehost, self.uptobox, self.fileio]
            for i in tasks:
                Thread(target=i, args=(c,)).start()
                self.threads_label.setText(f"Threads: {active_count()}")
                self.threads_label.adjustSize()
                c += 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyMirror"))
        MainWindow.setStatusTip(_translate("MainWindow", "https://github.com/Tufaah/PyMirror"))
        self.path_textbox.setStatusTip(
            _translate("MainWindow", "Enter your file path for example: ( C:\\Users\\Yazan\\Downloads\\test.py )"))
        self.path_textbox.setPlaceholderText(_translate("MainWindow", "File path"))
        self.groupBox.setTitle(_translate("MainWindow", " Links"))
        self.done_urls_textbox.setStatusTip(_translate("MainWindow", "All done urls will pop here"))
        self.done_urls_textbox.setPlaceholderText(_translate("MainWindow", "Done URLs"))
        self.label.setStatusTip(_translate("MainWindow", "https://github.com/Tufaah/PyMirror"))
        self.label.setText(_translate("MainWindow", "PyMirror ( v1.0 )"))
        self.browse_button.setStatusTip(_translate("MainWindow", "Browse button"))
        self.browse_button.setText(_translate("MainWindow", "📁"))
        self.is_custom.setStatusTip(_translate("MainWindow", "Press me if you want a custom name for your file"))
        self.is_custom.setText(_translate("MainWindow", "Custom name"))
        self.custom_textbox.setStatusTip(_translate("MainWindow", "Enter a custom file name ( if you want )"))
        self.custom_textbox.setPlaceholderText(_translate("MainWindow", "Custom name"))
        self.is_auto.setStatusTip(_translate("MainWindow", "Press me if you want me to keep the name of the file"))
        self.is_auto.setText(_translate("MainWindow", "Auto name"))
        self.done_label.setStatusTip(_translate("MainWindow", "Counter for done links"))
        self.done_label.setText(_translate("MainWindow", "Done: ( 0/0 )"))
        self.threads_label.setStatusTip(_translate("MainWindow", "Counter for active threads"))
        self.threads_label.setText(_translate("MainWindow", "Threads: 0"))
        self.start_button.setStatusTip(_translate("MainWindow", "Start button"))
        self.start_button.setText(_translate("MainWindow", "🏃"))
        self.settings_button.setStatusTip(_translate("MainWindow", "Settings button"))
        self.settings_button.setText(_translate("MainWindow", "⚙️"))

    def bayfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://api.bayfiles.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['data']['file']['url']['short'])
        except Exception as ex: self.add(f"Bayfiles upload faild! {ex}")

    def anonfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://api.anonfiles.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['data']['file']['url']['short'])
        except Exception as ex: self.add(f"Anonfiles upload faild! {ex}")

    def zippyshare(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(re.search('(https://[\S]+.zippyshare.com/v/[^"]+)', post('https://www91.zippyshare.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).text).group(1))
        except Exception as ex: self.add(f"Zippyshare upload faild! {ex}")

    def fireload(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://srv5.fireload.com/core/page/ajax/file_upload_handler.ajax.php?r=www.fireload.com&p=https', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.add(f"Fireload upload faild! {ex}")

    def usaupload(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://usaupload.com/ajax/file_upload_handler?r=usaupload.com&p=https', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.add(f"Usaupload upload faild! {ex}")

    def krakenfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add('https://krakenfiles.com' + str(post('https://s3.krakenfiles.com/_uploader/gallery/upload', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()['files'][0]['url']))
        except Exception as ex: self.add(f"Krakenfiles upload faild! {ex}")

    def fileio(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://file.io/', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['link'])
        except Exception as ex: self.add(f"File.io upload faild! {ex}")

    def uptobox(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://www31.uptobox.com/upload', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()['files'][0]['url'])
        except Exception as ex: self.add(f"Uptobox upload faild! {ex}")

    def filehost(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('http://www.filehost.pt/core/page/ajax/file_upload_handler.ajax.php?r=www.filehost.pt', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.add(f"Filehost upload faild! {ex}")

    def megaup(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://f27.megaup.net/core/page/ajax/file_upload_handler.ajax.php?r=megaup.net', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.add(f"Megaup upload faild! {ex}")


if __name__ == "__main__":
    def mainWin():
        app = QtWidgets.QApplication(argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow = QtWidgets.QMainWindow()
        ui = UiMainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        exit(app.exec_())

    mainWin()


