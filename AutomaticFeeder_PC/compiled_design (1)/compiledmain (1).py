# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/maindesign.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 801, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.line = QtWidgets.QFrame(self.tab_info)
        self.line.setGeometry(QtCore.QRect(0, 390, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.tab_info)
        self.label_9.setGeometry(QtCore.QRect(300, 410, 211, 17))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.tab_info)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 440, 211, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.foodbarlabel = QtWidgets.QLabel(self.layoutWidget)
        self.foodbarlabel.setObjectName("foodbarlabel")
        self.horizontalLayout_7.addWidget(self.foodbarlabel)
        self.foodProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.foodProgressBar.setProperty("value", 24)
        self.foodProgressBar.setObjectName("foodProgressBar")
        self.horizontalLayout_7.addWidget(self.foodProgressBar)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_info)
        self.layoutWidget1.setGeometry(QtCore.QRect(290, 470, 211, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.waterbarlabel = QtWidgets.QLabel(self.layoutWidget1)
        self.waterbarlabel.setObjectName("waterbarlabel")
        self.horizontalLayout_8.addWidget(self.waterbarlabel)
        self.waterProgressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.waterProgressBar.setProperty("value", 100)
        self.waterProgressBar.setObjectName("waterProgressBar")
        self.horizontalLayout_8.addWidget(self.waterProgressBar)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_info)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.daylayout = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.daylayout.setUndoRedoEnabled(True)
        self.daylayout.setReadOnly(True)
        self.daylayout.setObjectName("daylayout")
        self.horizontalLayout_12.addWidget(self.daylayout)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_12.addWidget(self.calendarWidget)
        self.tabWidget.addTab(self.tab_info, "")
        self.tab_petinfo = QtWidgets.QWidget()
        self.tab_petinfo.setObjectName("tab_petinfo")
        self.photo = QtWidgets.QLabel(self.tab_petinfo)
        self.photo.setGeometry(QtCore.QRect(250, 10, 531, 531))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_petinfo)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 10, 175, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.animaltype = QtWidgets.QLineEdit(self.layoutWidget2)
        self.animaltype.setReadOnly(True)
        self.animaltype.setObjectName("animaltype")
        self.horizontalLayout_3.addWidget(self.animaltype)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.animalbreed = QtWidgets.QLineEdit(self.layoutWidget2)
        self.animalbreed.setReadOnly(True)
        self.animalbreed.setObjectName("animalbreed")
        self.horizontalLayout_4.addWidget(self.animalbreed)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.animalweight = QtWidgets.QLineEdit(self.layoutWidget2)
        self.animalweight.setReadOnly(True)
        self.animalweight.setObjectName("animalweight")
        self.horizontalLayout_9.addWidget(self.animalweight)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.animalage = QtWidgets.QLineEdit(self.layoutWidget2)
        self.animalage.setReadOnly(True)
        self.animalage.setObjectName("animalage")
        self.horizontalLayout_10.addWidget(self.animalage)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.animalsex = QtWidgets.QLineEdit(self.layoutWidget2)
        self.animalsex.setReadOnly(True)
        self.animalsex.setObjectName("animalsex")
        self.horizontalLayout_11.addWidget(self.animalsex)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_petinfo, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.shownotes_txt = QtWidgets.QTextBrowser(self.tab_2)
        self.shownotes_txt.setGeometry(QtCore.QRect(0, 10, 781, 491))
        self.shownotes_txt.setObjectName("shownotes_txt")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.note_textbox = QtWidgets.QTextEdit(self.tab_3)
        self.note_textbox.setGeometry(QtCore.QRect(20, 60, 721, 311))
        self.note_textbox.setObjectName("note_textbox")
        self.savenote_button = QtWidgets.QPushButton(self.tab_3)
        self.savenote_button.setGeometry(QtCore.QRect(330, 400, 87, 29))
        self.savenote_button.setObjectName("savenote_button")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 10, 184, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_29.addWidget(self.label_21)
        self.notename = QtWidgets.QLineEdit(self.layoutWidget3)
        self.notename.setObjectName("notename")
        self.horizontalLayout_29.addWidget(self.notename)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.widget = QtWidgets.QWidget(self.tab_settings)
        self.widget.setGeometry(QtCore.QRect(10, 140, 281, 221))
        self.widget.setObjectName("widget")
        self.layoutWidget4 = QtWidgets.QWidget(self.widget)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 278, 230))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_21 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout_2.addWidget(self.checkBox_21)
        self.checkBox_22 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout_2.addWidget(self.checkBox_22)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_3.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_3.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_3.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_3.addWidget(self.checkBox_13)
        self.checkBox_24 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout_3.addWidget(self.checkBox_24)
        self.checkBox_23 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout_3.addWidget(self.checkBox_23)
        self.checkBox_14 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_3.addWidget(self.checkBox_14)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_15 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_4.addWidget(self.checkBox_15)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_4.addWidget(self.checkBox_16)
        self.checkBox_17 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout_4.addWidget(self.checkBox_17)
        self.checkBox_18 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_4.addWidget(self.checkBox_18)
        self.checkBox_26 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout_4.addWidget(self.checkBox_26)
        self.checkBox_25 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout_4.addWidget(self.checkBox_25)
        self.checkBox_19 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_4.addWidget(self.checkBox_19)
        self.checkBox_20 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_4.addWidget(self.checkBox_20)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_settings)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 60, 272, 29))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget5)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.feedweight = QtWidgets.QSpinBox(self.layoutWidget5)
        self.feedweight.setMaximum(200)
        self.feedweight.setSingleStep(5)
        self.feedweight.setObjectName("feedweight")
        self.horizontalLayout_2.addWidget(self.feedweight)
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_settings)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 20, 176, 27))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.feedfrequency = QtWidgets.QComboBox(self.layoutWidget6)
        self.feedfrequency.setObjectName("feedfrequency")
        self.feedfrequency.addItem("")
        self.feedfrequency.setItemText(0, "1")
        self.feedfrequency.addItem("")
        self.feedfrequency.addItem("")
        self.feedfrequency.addItem("")
        self.feedfrequency.addItem("")
        self.feedfrequency.addItem("")
        self.feedfrequency.setItemText(5, "6")
        self.horizontalLayout.addWidget(self.feedfrequency)
        self.layoutWidget7 = QtWidgets.QWidget(self.tab_settings)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 100, 327, 27))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.feedsupply = QtWidgets.QComboBox(self.layoutWidget7)
        self.feedsupply.setObjectName("feedsupply")
        self.feedsupply.addItem("")
        self.feedsupply.addItem("")
        self.horizontalLayout_5.addWidget(self.feedsupply)
        self.layoutWidget8 = QtWidgets.QWidget(self.tab_settings)
        self.layoutWidget8.setGeometry(QtCore.QRect(480, 0, 366, 83))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.showfeed = QtWidgets.QCheckBox(self.layoutWidget8)
        self.showfeed.setObjectName("showfeed")
        self.verticalLayout_5.addWidget(self.showfeed)
        self.showwater = QtWidgets.QCheckBox(self.layoutWidget8)
        self.showwater.setObjectName("showwater")
        self.verticalLayout_5.addWidget(self.showwater)
        self.autocontrolling = QtWidgets.QCheckBox(self.layoutWidget8)
        self.autocontrolling.setObjectName("autocontrolling")
        self.verticalLayout_5.addWidget(self.autocontrolling)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_settings)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 450, 708, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.savesettings = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.savesettings.setObjectName("savesettings")
        self.horizontalLayout_13.addWidget(self.savesettings)
        self.setdefaultsettings = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.setdefaultsettings.setObjectName("setdefaultsettings")
        self.horizontalLayout_13.addWidget(self.setdefaultsettings)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_13.addWidget(self.pushButton)
        self.changeinfoaboutpet = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.changeinfoaboutpet.setObjectName("changeinfoaboutpet")
        self.horizontalLayout_13.addWidget(self.changeinfoaboutpet)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_settings)
        self.layoutWidget_2.setGeometry(QtCore.QRect(480, 90, 272, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        self.countofwater = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.countofwater.setMaximum(500)
        self.countofwater.setSingleStep(5)
        self.countofwater.setObjectName("countofwater")
        self.horizontalLayout_14.addWidget(self.countofwater)
        self.tabWidget.addTab(self.tab_settings, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Информация о наличии корма"))
        self.foodbarlabel.setText(_translate("MainWindow", "Корм"))
        self.waterbarlabel.setText(_translate("MainWindow", "Вода"))
        self.daylayout.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("MainWindow", "Информация о питании"))
        self.label_10.setText(_translate("MainWindow", "Вид"))
        self.label_11.setText(_translate("MainWindow", "Порода"))
        self.label_12.setText(_translate("MainWindow", "Вес"))
        self.label_13.setText(_translate("MainWindow", "Возраст"))
        self.label_15.setText(_translate("MainWindow", "Пол"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_petinfo), _translate("MainWindow", "Информация о животном"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Просмотр"))
        self.savenote_button.setText(_translate("MainWindow", "Сохранить"))
        self.label_21.setText(_translate("MainWindow", "Название"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Заметки"))
        self.checkBox_3.setText(_translate("MainWindow", "00"))
        self.checkBox_4.setText(_translate("MainWindow", "01"))
        self.checkBox_5.setText(_translate("MainWindow", "02"))
        self.checkBox_6.setText(_translate("MainWindow", "03"))
        self.checkBox_7.setText(_translate("MainWindow", "04"))
        self.checkBox_21.setText(_translate("MainWindow", "05"))
        self.checkBox_22.setText(_translate("MainWindow", "05"))
        self.checkBox_8.setText(_translate("MainWindow", "07"))
        self.checkBox_9.setText(_translate("MainWindow", "08"))
        self.checkBox_10.setText(_translate("MainWindow", "09"))
        self.checkBox_11.setText(_translate("MainWindow", "10"))
        self.checkBox_12.setText(_translate("MainWindow", "11"))
        self.checkBox_13.setText(_translate("MainWindow", "12"))
        self.checkBox_24.setText(_translate("MainWindow", "13"))
        self.checkBox_23.setText(_translate("MainWindow", "14"))
        self.checkBox_14.setText(_translate("MainWindow", "15"))
        self.checkBox_15.setText(_translate("MainWindow", "16"))
        self.checkBox_16.setText(_translate("MainWindow", "17"))
        self.checkBox_17.setText(_translate("MainWindow", "18"))
        self.checkBox_18.setText(_translate("MainWindow", "19"))
        self.checkBox_26.setText(_translate("MainWindow", "20"))
        self.checkBox_25.setText(_translate("MainWindow", "21"))
        self.checkBox_19.setText(_translate("MainWindow", "22"))
        self.checkBox_20.setText(_translate("MainWindow", "23"))
        self.label.setText(_translate("MainWindow", "Дневная норма"))
        self.label_2.setText(_translate("MainWindow", "Частота питания"))
        self.feedfrequency.setItemText(1, _translate("MainWindow", "2"))
        self.feedfrequency.setItemText(2, _translate("MainWindow", "3"))
        self.feedfrequency.setItemText(3, _translate("MainWindow", "4"))
        self.feedfrequency.setItemText(4, _translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Подача корма"))
        self.feedsupply.setCurrentText(_translate("MainWindow", "По времени"))
        self.feedsupply.setItemText(0, _translate("MainWindow", "По времени"))
        self.feedsupply.setItemText(1, _translate("MainWindow", "Сразу после употребления"))
        self.showfeed.setText(_translate("MainWindow", "Отображать количество корма"))
        self.showwater.setText(_translate("MainWindow", "Отоборажать уровень воды "))
        self.autocontrolling.setText(_translate("MainWindow", "Включить автоматический контроль за кормом"))
        self.savesettings.setText(_translate("MainWindow", "Сохранить настройки"))
        self.setdefaultsettings.setText(_translate("MainWindow", "Сбросить настройки"))
        self.pushButton.setText(_translate("MainWindow", "Обновить информацию"))
        self.changeinfoaboutpet.setText(_translate("MainWindow", "Изменить информацию о животном"))
        self.label_3.setText(_translate("MainWindow", "Объем воды"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Настройки"))


