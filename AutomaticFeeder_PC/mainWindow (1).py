import compiled_design.compiledmain
from PyQt5 import QtWidgets, QtGui
import tools
from main import configfile, configapplication
import settingsWindow


class mainWindow(QtWidgets.QMainWindow, compiled_design.compiledmain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        '''
            обработчики кнопок
        '''
        self.calendarWidget.clicked.connect(self.printdayinfo)
        self.changeinfoaboutpet.clicked.connect(self.changeinfoaboutpetfunc)  # обработчик кнопки измен инф о животном
        self.setdefaultsettings.clicked.connect(self.setdefaultsettingsfunc)
        self.savesettings.clicked.connect(self.savesettingfunc)
        self.savenote_button.clicked.connect(self.add_note)

        self.settingswindow = settingsWindow.settingsWindow(self)  # окно настроек для главного окна

        # self.pixmap = None #QtGui.QPixmap('photos/sbk_.png')
        # self.photo.setPixmap(self.pixmap)

        #self.shownotes()


    def shownotes(self):

        with open('notes/note', 'r') as file:
            content = file.read().split(';')

        notes = []

        for i in content:
            notes.append([i.split(':')[0].strip(), i.split(':')[1].strip()])

        for i in notes:
            self.shownotes_txt.setText(self.shownotes_txt.toPlainText() + i[0] + ' : ' + i[1] + '\n\n')


    def add_note(self):
        name = self.notename.text()
        note = self.note_textbox.toPlainText()

        import datetime

        filename = 'notes/note'

        with open(filename, 'a') as file:
            file.write(';' + '\n' + name + ':\n' + note)

        self.shownotes()

    def printdayinfo(self):
        date = tools.reformatQtCalendarDate(self.calendarWidget)
        try:
            with open('logs/daysessions/' + date, 'r') as file:
                text = file.read().split('\n')
        except FileNotFoundError:
            self.daylayout.setText('Нет информации о данном дне')
            return

        nowatercount = 0
        nofeedcount = 0
        wasate = 0
        for i in text:

            if i.split(';')[0] == 'no water':
                nowatercount += 1
                lastwater = (i.split(';')[0], i.split(';')[1])

            if i.split(';')[0] == 'no feed':
                nofeedcount += 1

                lastfeed = (i.split(';')[0], i.split(';')[1])
            if i.split(';')[0] == 'there is water':
                pass
            if i.split(';')[0] == 'feed':
                wasate = int(i.split(';')[1])

        norm = int(tools.createassociativearray('configfiles/applicationconfig')['feedweight'])
        waternorm = int(tools.createassociativearray('configfiles/applicationconfig')['countofwater'])

        currentfood = wasate  # текущее количество еды

        wasate = int(nofeedcount) * 100 + 100 - int(wasate)

        text = 'Вода кончилась ' + str(nowatercount) + ' раз' + \
               '\nЕда кончилась ' + str(nofeedcount) + ' раз' + \
               '\n\nВ поседний раз вода кончилась в ' + lastwater[1].split()[1] + \
               '\n\nВ последний раз еда кончилась в ' + lastfeed[1].split()[1] + \
               '\n\nСъедено от нормы ' + str(wasate) + ' из ' + str(norm) + \
               '\n\nВыпито воды от нормы + ' + str(nowatercount * 100) + ' из ' + str(waternorm)

        print(wasate)
        self.foodProgressBar.setValue(currentfood)
        self.daylayout.setText(text)

    def setdefaultsettingsfunc(self):
        # установить стандартные настройки

        self.feedfrequency.setCurrentText('1')
        self.feedweight.setValue(1)
        self.feedsupply.setCurrentText('1')
        self.showfeed.setChecked(False)
        self.showwater.setChecked(False)
        self.autocontrolling.setChecked(False)

    def savesettingfunc(self):
        feedfrequency = self.feedfrequency.currentText()
        feedweight = str(self.feedweight.value())
        feedsupply = self.feedsupply.currentText()
        showfeed = str(self.showfeed.isChecked()).lower()
        showwater = str(self.showwater.isChecked()).lower()
        autocontrolling = str(self.autocontrolling.isChecked()).lower()
        countofwater = str(self.countofwater.value())

        onrecord = 'feedfrequency:' + feedfrequency + '\n'
        onrecord += 'feedweight:' + feedweight + '\n'
        onrecord += 'feedsupply:' + feedsupply + '\n'
        onrecord += 'showfeed:' + showfeed + '\n'
        onrecord += 'showwater:' + showwater + '\n'
        onrecord += 'autocontrolling:' + autocontrolling + '\n'
        onrecord += 'countofwater:' + countofwater

        file = open(configapplication, 'w').write(onrecord)

        self.setupsettings()

    def changeinfoaboutpetfunc(self):
        # изменение информации о животном

        self.settingswindow.show()
        self.setupsettings()

    def setupsettings(self):
        # установить текущие настройки

        settings = tools.createassociativearray(configfile)
        application = tools.createassociativearray(configapplication)

        # настройки животного
        self.animaltype.setText(settings['animaltype'])
        self.animalbreed.setText(settings['animalbreed'])
        self.animalweight.setText(settings['animalweight'])
        self.animalage.setText(settings['animalage'])
        self.animalsex.setText(settings['animalsex'])

        # фотография животного
        pixmap = QtGui.QPixmap('photos/sbk_.png')
        self.photo.setPixmap(pixmap)

        # настройки приложения
        self.printdayinfo()

        self.countofwater.setValue(int(application['countofwater']))
        self.feedfrequency.setCurrentText(application['feedfrequency'])
        self.feedweight.setValue(int(application['feedweight']))
        self.feedsupply.setCurrentText(application['feedsupply'])
        if application['showfeed'] == 'true':
            self.showfeed.setChecked(True)
        else:
            self.showfeed.setChecked(False)
        if application['showwater'] == 'true':
            self.showwater.setChecked(True)
        else:
            self.showwater.setChecked(False)
        if application['autocontrolling'] == 'true':
            self.autocontrolling.setChecked(True)
        else:
            self.autocontrolling.setChecked(False)
        if application['showwater'] == 'true':
            self.waterProgressBar.show()
            self.waterbarlabel.show()
        else:
            self.waterProgressBar.hide()
            self.waterbarlabel.hide()
        if application['showfeed'] == 'true':
            self.foodProgressBar.show()
            self.foodbarlabel.show()
        else:
            self.foodProgressBar.hide()
            self.foodbarlabel.hide()
