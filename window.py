from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sys import argv, exit
from threading import active_count, Thread
from requests import post, get
import re
import qdarkstyle


uploaders = 16
main_file_name, main_file_string, main_tasks = '', bytes(), []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settings/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.resize(401, 723)
        MainWindow.setFixedSize(401, 723)
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
        self.is_custom.setGeometry(QtCore.QRect(240, 40, 101, 17))
        self.is_custom.setObjectName("is_custom")
        self.custom_textbox = QtWidgets.QTextEdit(self.frame)
        self.custom_textbox.setGeometry(QtCore.QRect(0, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.custom_textbox.setFont(font)
        self.custom_textbox.setObjectName("custom_textbox")
        self.is_auto = QtWidgets.QRadioButton(self.frame)
        self.is_auto.setGeometry(QtCore.QRect(110, 40, 111, 17))
        self.is_auto.setChecked(True)
        self.is_auto.setObjectName("is_auto")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 37, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 570, 361, 101))
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
        self.files_label = QtWidgets.QLabel(self.frame_2)
        self.files_label.setGeometry(QtCore.QRect(20, 70, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.files_label.setFont(font)
        self.files_label.setObjectName("files_label")
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
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(210, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(20, 230, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.refresh_button.setFont(font)
        self.refresh_button.setObjectName("refresh_button")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 270, 361, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.done_urls_textbox = QtWidgets.QPlainTextEdit(self.groupBox)
        self.done_urls_textbox.setGeometry(QtCore.QRect(10, 30, 311, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.done_urls_textbox.setFont(font)
        self.done_urls_textbox.setPlainText("")
        self.done_urls_textbox.setObjectName("done_urls_textbox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 331, 251))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.error_urls_textbox = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.error_urls_textbox.setGeometry(QtCore.QRect(10, 30, 311, 211))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(10)
        self.error_urls_textbox.setFont(font)
        self.error_urls_textbox.setPlainText("")
        self.error_urls_textbox.setObjectName("error_urls_textbox")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.custom_textbox.setEnabled(False)
        self.label.adjustSize()
        self.start_button.clicked.connect(self.start)
        self.browse_button.clicked.connect(self.browse)
        self.settings_button.clicked.connect(self.settings_window)
        self.refresh_button.clicked.connect(self.refresh)
        self.save_button.clicked.connect(self.save_it)

        self.is_custom.clicked.connect(self.show)
        self.is_auto.clicked.connect(self.hide)

    def refresh(self):
        self.error_urls_textbox.clear()
        self.done_urls_textbox.clear()
        self.path_textbox.clear()
        self.custom_textbox.clear()
        self.threads_label.setText("Threads: 1")
        self.threads_label.adjustSize()
        self.done_label.setText(f"Done: ( 0/{uploaders} )")
        self.done_label.adjustSize()
        self.frame.setEnabled(True)
        self.path_textbox.setEnabled(True)
        self.browse_button.setEnabled(True)
        self.settings_button.setEnabled(True)
        self.start_button.setEnabled(True)
        self.save_button.setEnabled(True)

    def save_it(self):
        global main_file_name
        to_save = self.done_urls_textbox.toPlainText()
        save_name = main_file_name.rsplit('/')[-1].replace('.', '_').replace('-', '_')
        with open(f'save-{save_name}.txt', 'w') as save_file:
            save_file.write(to_save)

        save_file.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Saved on: ( save-{save_name}.txt )")
        msg.setWindowTitle("Saved")
        msg.exec_()

    def settings(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Settings tap will be in ( v2.0 )")
        msg.setInformativeText('https://github.com/Tufaah/PyMirror')
        msg.setWindowTitle("Coming soon!")
        msg.exec_()

    def error(self, text):
        self.error_urls_textbox.appendPlainText(text)

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
            tasks = []
            if not main_tasks:
                tasks = [self.anonfiles, self.bayfiles, self.zippyshare, self.usaupload, self.krakenfiles,
                         self.fireload, self.megaup, self.filehost, self.uptobox, self.fileio, self.sendcm,
                         self.mixdrop, self.up00, self.uploadac, self.nofile, self.filesend]

            else:
                for task in main_tasks:
                    if task == 'anonfiles': tasks.append(self.anonfiles)
                    elif task == 'bayfiles': tasks.append(self.bayfiles)
                    elif task == 'bayfiles': tasks.append(self.zippyshare)
                    elif task == 'usaupload': tasks.append(self.usaupload)
                    elif task == 'krakenfiles': tasks.append(self.krakenfiles)
                    elif task == 'fireload': tasks.append(self.fireload)
                    elif task == 'megaup': tasks.append(self.megaup)
                    elif task == 'filehost': tasks.append(self.filehost)
                    elif task == 'uptobox': tasks.append(self.uptobox)
                    elif task == 'uptobox_2': tasks.append(self.uploadac)
                    elif task == 'fileio': tasks.append(self.fileio)
                    elif task == 'sendcm': tasks.append(self.sendcm)
                    elif task == 'Mixdrop': tasks.append(self.mixdrop)
                    elif task == 'up_00': tasks.append(self.up00)
                    elif task == 'nofile': tasks.append(self.nofile)
                    elif task == 'filesend': tasks.append(self.filesend)

            for i in tasks:
                Thread(target=i, args=(c,)).start()
                self.threads_label.setText(f"Threads: {active_count()}")
                self.threads_label.adjustSize()
                c += 1

    def settings_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SettingsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyMirror"))
        MainWindow.setStatusTip(_translate("MainWindow", "https://github.com/Tufaah/PyMirror"))
        self.path_textbox.setStatusTip(
            _translate("MainWindow", "Enter your file path for example: ( C:\\Users\\Yazan\\Downloads\\test.py )"))
        self.path_textbox.setPlaceholderText(_translate("MainWindow", "File path"))
        self.label.setStatusTip(_translate("MainWindow", "https://github.com/Tufaah/PyMirror"))
        self.label.setText(_translate("MainWindow", "PyMirror ( v2.0 )"))
        self.browse_button.setStatusTip(_translate("MainWindow", "Browse button"))
        self.browse_button.setText(_translate("MainWindow", "📁"))
        self.is_custom.setStatusTip(_translate("MainWindow", "Press me if you want a custom name for your file"))
        self.is_custom.setText(_translate("MainWindow", "Custom"))
        self.custom_textbox.setStatusTip(_translate("MainWindow", "Enter a custom file name ( if you want )"))
        self.custom_textbox.setPlaceholderText(_translate("MainWindow", "Custom name"))
        self.is_auto.setStatusTip(_translate("MainWindow", "Press me if you want me to keep the name of the file"))
        self.is_auto.setText(_translate("MainWindow", "Auto detect"))
        self.label_2.setStatusTip(_translate("MainWindow", "Counter for done links"))
        self.label_2.setText(_translate("MainWindow", "File name:"))
        self.done_label.setStatusTip(_translate("MainWindow", "Counter for done links"))
        self.done_label.setText(_translate("MainWindow", f"Done: ( 0/{uploaders} )"))
        self.threads_label.setStatusTip(_translate("MainWindow", "Counter for active threads"))
        self.threads_label.setText(_translate("MainWindow", "Threads: 0"))
        self.files_label.setStatusTip(_translate("MainWindow", "Counter for uploaded files"))
        self.files_label.setText(_translate("MainWindow", "Files: 0"))
        self.start_button.setStatusTip(_translate("MainWindow", "Start button"))
        self.start_button.setText(_translate("MainWindow", "🏃"))
        self.settings_button.setStatusTip(_translate("MainWindow", "Settings button"))
        self.settings_button.setText(_translate("MainWindow", "⚙"))
        self.save_button.setStatusTip(
            _translate("MainWindow", "Save button ( Press me if you want to save the links in .txt file )"))
        self.save_button.setText(_translate("MainWindow", "💾"))
        self.refresh_button.setStatusTip(
            _translate("MainWindow", "Refresh button ( Press me if you want to upload another file )"))
        self.refresh_button.setText(_translate("MainWindow", "🔄"))
        self.groupBox.setTitle(_translate("MainWindow", " Links "))
        self.done_urls_textbox.setStatusTip(_translate("MainWindow", "All done urls will pop here"))
        self.done_urls_textbox.setPlaceholderText(_translate("MainWindow", "Done URLs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Good Links"))
        self.groupBox_2.setTitle(_translate("MainWindow", " Errors "))
        self.error_urls_textbox.setStatusTip(_translate("MainWindow", "All error urls will pop here"))
        self.error_urls_textbox.setPlaceholderText(_translate("MainWindow", "Done URLs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Errors"))

    def bayfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://api.bayfiles.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['data']['file']['url']['short'])
        except Exception as ex: self.error(f"Bayfiles upload faild! {ex}")

    def anonfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://api.anonfiles.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['data']['file']['url']['short'])
        except Exception as ex: self.error(f"Anonfiles upload faild! {ex}")

    def zippyshare(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(re.search('(https://[\S]+.zippyshare.com/v/[^"]+)', post('https://www91.zippyshare.com/upload', files={'file': (main_file_name, main_file_string)}, headers=headers).text).group(1))
        except Exception as ex: self.error(f"Zippyshare upload faild! {ex}")

    def fireload(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://srv5.fireload.com/core/page/ajax/file_upload_handler.ajax.php?r=www.fireload.com&p=https', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.error(f"Fireload upload faild! {ex}")

    def usaupload(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://usaupload.com/ajax/file_upload_handler?r=usaupload.com&p=https', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.error(f"Usaupload upload faild! {ex}")

    def krakenfiles(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add('https://krakenfiles.com' + str(post('https://s3.krakenfiles.com/_uploader/gallery/upload', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()['files'][0]['url']))
        except Exception as ex: self.error(f"Krakenfiles upload faild! {ex}")

    def fileio(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://file.io/', files={'file': (main_file_name, main_file_string)}, headers=headers).json()['link'])
        except Exception as ex: self.error(f"File.io upload faild! {ex}")

    def uptobox(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://www31.uptobox.com/upload', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()['files'][0]['url'])
        except Exception as ex: self.error(f"Uptobox upload faild! {ex}")

    def filehost(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('http://www.filehost.pt/core/page/ajax/file_upload_handler.ajax.php?r=www.filehost.pt', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.error(f"Filehost upload faild! {ex}")

    def megaup(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://f27.megaup.net/core/page/ajax/file_upload_handler.ajax.php?r=megaup.net', files={'files[]': (main_file_name, main_file_string)}, headers=headers).json()[0]['url'])
        except Exception as ex: self.error(f"Megaup upload faild! {ex}")

    def filesend(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(post('https://filesend.io/ajax/file_upload_handler?r=filesend.io', files={'files[]': (main_file_name, main_file_string)}).json()[0]['url'])
        except Exception as ex: self.error(f"Filesend upload faild! {ex}")

    def nofile(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(re.search(r"(https://nofile.org/v/[^']+)", post('https://ns6.zipcluster.com/upload.php', data={'upload': 'Upload'}, files={'file[]': (main_file_name, main_file_string)}).text).group(1))
        except Exception as ex: self.error(f"Nofile upload faild! {ex}")

    def uploadac(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add('https://upload.ac/' + str(post('https://n1.upload.ac/cgi-bin/upload.cgi?upload_type=file&utype=anon', verify=False, files={'file_0': (main_file_name, main_file_string)}).json()[0]['file_code']))
        except Exception as ex:
            self.error(f"uploadac upload faild! {ex}")

    def up00(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add('https://www.up-00.com/' + str(post('https://www.up-00.com/cgi-bin/upload.cgi?upload_type=file&utype=anon', files={'file_0': (main_file_name, main_file_string)}).json()[0]['file_code']))
        except Exception as ex:
            self.error(f"Up-00 upload faild! {ex}")

    def mixdrop(self, counter):
        try:
            self.plus(counter, uploaders)
            self.add(('https://mixdrop.co/f/' + str(post('https://ul.mixdrop.co/up', data={'upload': 1}, files={'files': (main_file_name, main_file_string)}).json()['file']['ref'])))
        except Exception as ex:
            self.error(f"Mixdrop upload faild! {ex}")

    def sendcm(self, counter):
        try:
            self.plus(counter, uploaders)
            code = (str(post('https://cloud12.send.cm/cgi-bin/upload.cgi?upload_type=file&utype=anon', data={'upload': 1}, files={'file_0': (main_file_name, main_file_string)}).json()[0]['file_code']))
            self.add(re.search(r"(https://send.cm/d/[\S]+)", get(f'https://send.cm/?op=upload_result&st=OK&fn={code}').text).group(1))
        except Exception as ex:
            self.error(f"Sendcm upload faild! {ex}")


class SettingsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settings/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        MainWindow.resize(289, 371)
        MainWindow.setFixedSize(289, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_box = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_box.setGeometry(QtCore.QRect(20, 10, 251, 271))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.settings_box.setFont(font)
        self.settings_box.setObjectName("settings_box")
        self.anonfiles = QtWidgets.QCheckBox(self.settings_box)
        self.anonfiles.setGeometry(QtCore.QRect(20, 30, 81, 17))
        self.anonfiles.setObjectName("anonfiles")
        self.bayfiles = QtWidgets.QCheckBox(self.settings_box)
        self.bayfiles.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.bayfiles.setObjectName("bayfiles")
        self.zippyshare = QtWidgets.QCheckBox(self.settings_box)
        self.zippyshare.setGeometry(QtCore.QRect(20, 90, 91, 17))
        self.zippyshare.setObjectName("zippyshare")
        self.filehost = QtWidgets.QCheckBox(self.settings_box)
        self.filehost.setGeometry(QtCore.QRect(20, 210, 81, 17))
        self.filehost.setObjectName("filehost")
        self.usaupload = QtWidgets.QCheckBox(self.settings_box)
        self.usaupload.setGeometry(QtCore.QRect(20, 120, 91, 17))
        self.usaupload.setObjectName("usaupload")
        self.krakenfiles = QtWidgets.QCheckBox(self.settings_box)
        self.krakenfiles.setGeometry(QtCore.QRect(20, 150, 91, 17))
        self.krakenfiles.setObjectName("krakenfiles")
        self.megaup = QtWidgets.QCheckBox(self.settings_box)
        self.megaup.setGeometry(QtCore.QRect(150, 90, 81, 17))
        self.megaup.setObjectName("megaup")
        self.uptobox = QtWidgets.QCheckBox(self.settings_box)
        self.uptobox.setGeometry(QtCore.QRect(150, 120, 81, 21))
        self.uptobox.setObjectName("uptobox")
        self.fireload = QtWidgets.QCheckBox(self.settings_box)
        self.fireload.setGeometry(QtCore.QRect(20, 180, 81, 17))
        self.fireload.setObjectName("fireload")
        self.fileio = QtWidgets.QCheckBox(self.settings_box)
        self.fileio.setGeometry(QtCore.QRect(20, 240, 81, 17))
        self.fileio.setObjectName("fileio")
        self.filesend = QtWidgets.QCheckBox(self.settings_box)
        self.filesend.setGeometry(QtCore.QRect(150, 30, 81, 17))
        self.filesend.setObjectName("filesend")
        self.nofile = QtWidgets.QCheckBox(self.settings_box)
        self.nofile.setGeometry(QtCore.QRect(150, 60, 81, 21))
        self.nofile.setObjectName("nofile")
        self.uptobox_2 = QtWidgets.QCheckBox(self.settings_box)
        self.uptobox_2.setGeometry(QtCore.QRect(150, 150, 81, 21))
        self.uptobox_2.setObjectName("uptobox_2")
        self.up_00 = QtWidgets.QCheckBox(self.settings_box)
        self.up_00.setGeometry(QtCore.QRect(150, 180, 81, 21))
        self.up_00.setObjectName("up_00")
        self.Mixdrop = QtWidgets.QCheckBox(self.settings_box)
        self.Mixdrop.setGeometry(QtCore.QRect(150, 210, 81, 21))
        self.Mixdrop.setObjectName("Mixdrop")
        self.sendcm = QtWidgets.QCheckBox(self.settings_box)
        self.sendcm.setGeometry(QtCore.QRect(150, 240, 81, 21))
        self.sendcm.setObjectName("sendcm")
        self.update_settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_settings_button.setGeometry(QtCore.QRect(20, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.update_settings_button.setFont(font)
        self.update_settings_button.setObjectName("update_settings_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(200, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.anonfiles.setChecked(True)
        self.bayfiles.setChecked(True)
        self.zippyshare.setChecked(True)
        self.filesend.setChecked(True)
        self.fileio.setChecked(True)
        self.filehost.setChecked(True)
        self.fireload.setChecked(True)
        self.krakenfiles.setChecked(True)
        self.nofile.setChecked(True)
        self.usaupload.setChecked(True)
        self.megaup.setChecked(True)
        self.uptobox.setChecked(True)
        self.uptobox_2.setChecked(True)
        self.up_00.setChecked(True)
        self.sendcm.setChecked(True)
        self.Mixdrop.setChecked(True)
        self.update_settings_button.clicked.connect(self.update_click)
        self.save_button.clicked.connect(self.soon)

    def soon(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"Sorry cache save will be in v3.0!")
        msg.setWindowTitle("Coming soon")
        msg.exec_()

    def update_click(self):
        main_tasks.clear()
        if self.anonfiles.isChecked(): main_tasks.append('anonfiles')
        if self.bayfiles.isChecked(): main_tasks.append('bayfiles')
        if self.zippyshare.isChecked(): main_tasks.append('zippyshare')
        if self.filesend.isChecked(): main_tasks.append('filesend')
        if self.fileio.isChecked(): main_tasks.append('fileio')
        if self.filehost.isChecked(): main_tasks.append('filehost')
        if self.fireload.isChecked(): main_tasks.append('fireload')
        if self.krakenfiles.isChecked(): main_tasks.append('krakenfiles')
        if self.nofile.isChecked(): main_tasks.append('nofile')
        if self.usaupload.isChecked(): main_tasks.append('usaupload')
        if self.megaup.isChecked(): main_tasks.append('megaup')
        if self.uptobox.isChecked(): main_tasks.append('uptobox')
        if self.uptobox_2.isChecked(): main_tasks.append('uptobox_2')
        if self.up_00.isChecked(): main_tasks.append('up_00')
        if self.sendcm.isChecked(): main_tasks.append('sendcm')
        if self.Mixdrop.isChecked(): main_tasks.append('Mixdrop')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.settings_box.setTitle(_translate("MainWindow", " Settings "))
        self.anonfiles.setText(_translate("MainWindow", "Anonfiles"))
        self.bayfiles.setText(_translate("MainWindow", "Bayfiles"))
        self.zippyshare.setText(_translate("MainWindow", "Zippyshare"))
        self.filehost.setText(_translate("MainWindow", "Filehost"))
        self.usaupload.setText(_translate("MainWindow", "Usaupload"))
        self.krakenfiles.setText(_translate("MainWindow", "Krakenfiles"))
        self.megaup.setText(_translate("MainWindow", "Megaup"))
        self.uptobox.setText(_translate("MainWindow", "Uptobox"))
        self.fireload.setText(_translate("MainWindow", "Fireload"))
        self.fileio.setText(_translate("MainWindow", "Fileio"))
        self.filesend.setText(_translate("MainWindow", "Filesend"))
        self.nofile.setText(_translate("MainWindow", "Nofile"))
        self.uptobox_2.setText(_translate("MainWindow", "uploadAC"))
        self.up_00.setText(_translate("MainWindow", "Up-00"))
        self.Mixdrop.setText(_translate("MainWindow", "Mixdrop"))
        self.sendcm.setText(_translate("MainWindow", "Sendcm"))
        self.update_settings_button.setStatusTip(_translate("MainWindow", "Update settings button"))
        self.update_settings_button.setText(_translate("MainWindow", "⬆️"))
        self.save_button.setStatusTip(_translate("MainWindow", "Save settings button"))
        self.save_button.setText(_translate("MainWindow", "💾"))


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
