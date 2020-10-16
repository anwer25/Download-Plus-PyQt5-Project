# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 442)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-download-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QColorDialog {\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTextEdit {\n"
"    background-color:#1e1d23;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPlainTextEdit {\n"
"    selection-background-color:#007b50;\n"
"    background-color:#1e1d23;\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"}\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: read;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: inset;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-width: 1px;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-bottom: 2px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #37efba;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #37efba;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #808086;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding-bottom: 1px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: #a9b7c6;\n"
"    background:#1e1d23;\n"
"    selection-background-color:#007b50;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"QLabel {\n"
"    color: #a9b7c6;\n"
"}\n"
"QLCDNumber {\n"
"    color: #37e6b4;\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:#1e1d23;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #04b97f;\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #a9b7c6;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"      background: #1e1d23;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background:#1e1d23;\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: #04b97f;\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #FFFFFF;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #a9b7c6;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QMenu{\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:#1e1d23;\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: #808086;\n"
"    padding: 3px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: #04b97f;\n"
"    border-bottom-width: 2px;\n"
"    border-style: solid;\n"
"    color: #FFFFFF;\n"
"    padding-left: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-left:3px;\n"
"    background-color: #1e1d23;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a9b7c6;\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:#1e1d23;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QRadioButton {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"    padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: #04b97f;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    border-style:solid;\n"
"    border-radius:5px;\n"
"    border-width: 1px;\n"
"    border-color: #04b97f;\n"
"    color: #a9b7c6;\n"
"    background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDoubleSpinBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateTimeEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QDateEdit {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QComboBox {\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    combobox-popup: 0;\n"
"}\n"
"QComboBox:editable {\n"
"    background: #1e1d23;\n"
"    color: #a9b7c6;\n"
"    selection-background-color: #04b97f;\n"
"}\n"
"QComboBox QAbstractItemView { /* i changed color from #a9b7c6 to #FFF and selection-color:#FFF*/\n"
"    color: #a9b7c6;    \n"
"    background: #1e1d23;\n"
"    selection-color: #FFF;\n"
"    selection-background-color: #04b97f;\n"
"}\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: #04b97f;    \n"
"    background: #1e1d23;\n"
"}\n"
"QFontComboBox {\n"
"    color: #a9b7c6;    \n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color: #1e1d23;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 14px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 14px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #04b97f;\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: #04b97f;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.UrlDownload = QtWidgets.QWidget()
        self.UrlDownload.setEnabled(True)
        self.UrlDownload.setObjectName("UrlDownload")
        self.currentDownloadsFileLabel = QtWidgets.QLabel(self.UrlDownload)
        self.currentDownloadsFileLabel.setGeometry(QtCore.QRect(50, 220, 171, 17))
        self.currentDownloadsFileLabel.setObjectName("currentDownloadsFileLabel")
        self.urlPlace = QtWidgets.QLineEdit(self.UrlDownload)
        self.urlPlace.setGeometry(QtCore.QRect(190, 50, 421, 25))
        self.urlPlace.setObjectName("urlPlace")
        self.currentDownladsFile = QtWidgets.QLCDNumber(self.UrlDownload)
        self.currentDownladsFile.setGeometry(QtCore.QRect(250, 220, 64, 23))
        self.currentDownladsFile.setObjectName("currentDownladsFile")
        self.utlLabel = QtWidgets.QLabel(self.UrlDownload)
        self.utlLabel.setGeometry(QtCore.QRect(50, 50, 91, 25))
        self.utlLabel.setObjectName("utlLabel")
        self.progressBar = QtWidgets.QProgressBar(self.UrlDownload)
        self.progressBar.setGeometry(QtCore.QRect(50, 280, 691, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.downloadButton = QtWidgets.QPushButton(self.UrlDownload)
        self.downloadButton.setGeometry(QtCore.QRect(320, 330, 151, 25))
        self.downloadButton.setStyleSheet("")
        self.downloadButton.setObjectName("downloadButton")
        self.savelocationPlace = QtWidgets.QLineEdit(self.UrlDownload)
        self.savelocationPlace.setGeometry(QtCore.QRect(190, 150, 421, 25))
        self.savelocationPlace.setObjectName("savelocationPlace")
        self.openFileLocationSaver = QtWidgets.QPushButton(self.UrlDownload)
        self.openFileLocationSaver.setGeometry(QtCore.QRect(660, 150, 80, 25))
        self.openFileLocationSaver.setObjectName("openFileLocationSaver")
        self.saveLocatintext = QtWidgets.QLabel(self.UrlDownload)
        self.saveLocatintext.setGeometry(QtCore.QRect(50, 150, 91, 25))
        self.saveLocatintext.setObjectName("saveLocatintext")
        self.fileLabel = QtWidgets.QLabel(self.UrlDownload)
        self.fileLabel.setGeometry(QtCore.QRect(50, 100, 91, 25))
        self.fileLabel.setObjectName("fileLabel")
        self.filePlace = QtWidgets.QLineEdit(self.UrlDownload)
        self.filePlace.setGeometry(QtCore.QRect(190, 100, 421, 25))
        self.filePlace.setObjectName("filePlace")
        self.openFileBrowser_2 = QtWidgets.QPushButton(self.UrlDownload)
        self.openFileBrowser_2.setGeometry(QtCore.QRect(660, 100, 80, 25))
        self.openFileBrowser_2.setObjectName("openFileBrowser_2")
        self.tabWidget.addTab(self.UrlDownload, "")
        self.YouTube = QtWidgets.QWidget()
        self.YouTube.setObjectName("YouTube")
        self.currentDownloadFileLabel_2 = QtWidgets.QLabel(self.YouTube)
        self.currentDownloadFileLabel_2.setGeometry(QtCore.QRect(50, 210, 171, 17))
        self.currentDownloadFileLabel_2.setObjectName("currentDownloadFileLabel_2")
        self.downloadButton_2 = QtWidgets.QPushButton(self.YouTube)
        self.downloadButton_2.setGeometry(QtCore.QRect(320, 320, 151, 25))
        self.downloadButton_2.setStyleSheet("")
        self.downloadButton_2.setObjectName("downloadButton_2")
        self.search = QtWidgets.QPushButton(self.YouTube)
        self.search.setGeometry(QtCore.QRect(660, 50, 80, 25))
        self.search.setObjectName("search")
        self.qualityLabel_2 = QtWidgets.QLabel(self.YouTube)
        self.qualityLabel_2.setGeometry(QtCore.QRect(50, 150, 91, 25))
        self.qualityLabel_2.setObjectName("qualityLabel_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.YouTube)
        self.progressBar_2.setGeometry(QtCore.QRect(50, 270, 691, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.currentDownladFile_2 = QtWidgets.QLCDNumber(self.YouTube)
        self.currentDownladFile_2.setGeometry(QtCore.QRect(250, 210, 64, 23))
        self.currentDownladFile_2.setObjectName("currentDownladFile_2")
        self.youtub_url = QtWidgets.QLineEdit(self.YouTube)
        self.youtub_url.setGeometry(QtCore.QRect(190, 50, 421, 25))
        self.youtub_url.setObjectName("youtub_url")
        self.qualityBox_2 = QtWidgets.QComboBox(self.YouTube)
        self.qualityBox_2.setGeometry(QtCore.QRect(170, 150, 331, 25))
        self.qualityBox_2.setObjectName("qualityBox_2")
        self.utlLabel_2 = QtWidgets.QLabel(self.YouTube)
        self.utlLabel_2.setGeometry(QtCore.QRect(50, 50, 91, 25))
        self.utlLabel_2.setObjectName("utlLabel_2")
        self.locationPlace = QtWidgets.QLineEdit(self.YouTube)
        self.locationPlace.setGeometry(QtCore.QRect(190, 100, 421, 25))
        self.locationPlace.setObjectName("locationPlace")
        self.saveLocationText = QtWidgets.QLabel(self.YouTube)
        self.saveLocationText.setGeometry(QtCore.QRect(50, 100, 91, 25))
        self.saveLocationText.setObjectName("saveLocationText")
        self.openSaveLocation = QtWidgets.QPushButton(self.YouTube)
        self.openSaveLocation.setGeometry(QtCore.QRect(660, 100, 80, 25))
        self.openSaveLocation.setObjectName("openSaveLocation")
        self.tabWidget.addTab(self.YouTube, "")
        self.convert = QtWidgets.QWidget()
        self.convert.setObjectName("convert")
        self.savemp3LocationText_3 = QtWidgets.QLabel(self.convert)
        self.savemp3LocationText_3.setGeometry(QtCore.QRect(50, 110, 91, 25))
        self.savemp3LocationText_3.setObjectName("savemp3LocationText_3")
        self.downloadButton_4 = QtWidgets.QPushButton(self.convert)
        self.downloadButton_4.setGeometry(QtCore.QRect(320, 230, 151, 25))
        self.downloadButton_4.setStyleSheet("")
        self.downloadButton_4.setObjectName("downloadButton_4")
        self.mp4fileLAbel = QtWidgets.QLabel(self.convert)
        self.mp4fileLAbel.setGeometry(QtCore.QRect(50, 60, 91, 25))
        self.mp4fileLAbel.setObjectName("mp4fileLAbel")
        self.currentconvertFileLabel_4 = QtWidgets.QLabel(self.convert)
        self.currentconvertFileLabel_4.setGeometry(QtCore.QRect(50, 180, 171, 17))
        self.currentconvertFileLabel_4.setObjectName("currentconvertFileLabel_4")
        self.currentConvertedFile = QtWidgets.QLCDNumber(self.convert)
        self.currentConvertedFile.setGeometry(QtCore.QRect(250, 180, 64, 23))
        self.currentConvertedFile.setObjectName("currentConvertedFile")
        self.openmp4file = QtWidgets.QPushButton(self.convert)
        self.openmp4file.setGeometry(QtCore.QRect(660, 60, 80, 25))
        self.openmp4file.setObjectName("openmp4file")
        self.mp3savelcation = QtWidgets.QPushButton(self.convert)
        self.mp3savelcation.setGeometry(QtCore.QRect(660, 110, 80, 25))
        self.mp3savelcation.setObjectName("mp3savelcation")
        self.mp4filename = QtWidgets.QLineEdit(self.convert)
        self.mp4filename.setGeometry(QtCore.QRect(190, 60, 421, 25))
        self.mp4filename.setObjectName("mp4filename")
        self.mp3location = QtWidgets.QLineEdit(self.convert)
        self.mp3location.setGeometry(QtCore.QRect(190, 110, 421, 25))
        self.mp3location.setObjectName("mp3location")
        self.tabWidget.addTab(self.convert, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 19))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menufile.addAction(self.actionExit)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Plus"))
        self.currentDownloadsFileLabel.setText(_translate("MainWindow", "Current downloads file"))
        self.utlLabel.setText(_translate("MainWindow", "URL"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.openFileLocationSaver.setText(_translate("MainWindow", "Browser"))
        self.saveLocatintext.setText(_translate("MainWindow", "Save location"))
        self.fileLabel.setText(_translate("MainWindow", "File"))
        self.openFileBrowser_2.setText(_translate("MainWindow", "Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UrlDownload), _translate("MainWindow", "URL Download"))
        self.currentDownloadFileLabel_2.setText(_translate("MainWindow", "Current download file"))
        self.downloadButton_2.setText(_translate("MainWindow", "Download"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.qualityLabel_2.setText(_translate("MainWindow", "Quality"))
        self.utlLabel_2.setText(_translate("MainWindow", "URL"))
        self.saveLocationText.setText(_translate("MainWindow", "Save location"))
        self.openSaveLocation.setText(_translate("MainWindow", "Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YouTube), _translate("MainWindow", "YouTube Download"))
        self.savemp3LocationText_3.setText(_translate("MainWindow", "Save location"))
        self.downloadButton_4.setText(_translate("MainWindow", "Convert"))
        self.mp4fileLAbel.setText(_translate("MainWindow", "Fiel"))
        self.currentconvertFileLabel_4.setText(_translate("MainWindow", "Current Converted files"))
        self.openmp4file.setText(_translate("MainWindow", "Browser"))
        self.mp3savelcation.setText(_translate("MainWindow", "Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.convert), _translate("MainWindow", "mp4 to mp3"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
