from PyQt5 import QtWidgets
import compiled_design.compiledsettings
import tools
from main import configfile
from PyQt5 import QtGui



class settingsWindow(QtWidgets.QMainWindow, compiled_design.compiledsettings.Ui_MainWindow):
    def __init__(self, mainwindow):


        super().__init__()
        self.setupUi(self)
        self.saveButton.clicked.connect(self.saveclicked)
        self.mainwindow = mainwindow
        self.downloadButton.clicked.connect(self.loadimage)

        # установка текущих значений, если уже заполнены
        file = open('configfiles/aboutpet')
        if len(file.read()) > 0:
            settings = tools.createassociativearray('configfiles/aboutpet')
            self.animalage.setValue(int(settings['animalage']))
            self.animalbreed.setText(settings['animalbreed'])
            self.animaltype.setText(settings['animaltype'])
            self.animalweight.setValue(int(settings['animalweight']))
            self.animalsex.setCurrentText(settings['animalsex'])
        file.close()
        ######





    def loadimage(self):  # подогнать размер фотографии при необходимости
        self.photopath = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите фото', '/home/alexander/PycharmProjects/AutomaticFeeder/photos', '*.png')[0]
        tools.loadimage(self.photopath)
        self.mainwindow.pixmap = QtGui.QPixmap('photos/sbk_.png')



    def saveclicked(self):

        if len(self.animaltype.text()) > 0 and len(self.animalbreed.text()) > 0:
            file = open(configfile, 'w')

            file.write('animaltype:' + self.animaltype.text() + '\n')
            file.write('animalbreed:' + self.animalbreed.text() + '\n')
            file.write('animalweight:' + self.animalweight.text() + '\n')
            file.write('animalage:' + self.animalage.text() + '\n')
            file.write('animalsex:' + self.animalsex.currentText())
            file.close()

            self.hide()
            if not self.mainwindow.isActiveWindow():
                self.mainwindow.show()
            self.mainwindow.setupsettings()
