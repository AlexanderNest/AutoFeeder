# глобальные переменные ------------------

configfile = 'configfiles/aboutpet' # конфигурационный файл для домашнего животного
configapplication = 'configfiles/applicationconfig' # конфигурационный файл для приложения

# ----------------------------------------


import sys
import settingsWindow  # окно настроек
import mainWindow  # главное окно
import tools  # мои функции
from PyQt5 import QtWidgets
from threading import Thread
import time
import os
from datetime import date


def secondarytasks(mainwindow):
    def writesession():  # записывает информацию о сессии
        lastrequest = str()
        request = str()

        with open('logs/waterlog.txt', 'r') as fromserver, open('logs/daysessions/' + str(date.today()), 'w') as tolog:
            tolog.write(fromserver.read())

        os.system('cd logs && rm waterlog.txt')

    def checkfilling():  # проверяет наполнение еды и воды

        with open('logs/daysessions/' + str(date.today()), 'r') as file:
            text = file.read().strip().split('\n')[-1]  # запомнили последнюю строку файла, чтобы узнать о наполнении воды
            text = text.split(';')[0]  # беру значение лога, чтобы узнать о состоянии воды
            if text == 'no water':
                mainwindow.waterProgressBar.setValue(0)
            else:
                mainwindow.waterProgressBar.setValue(100)

    while True:
        command = 'cd logs && wget https://raw.githubusercontent.com/AlexanderNest/AutomaticFeeder/master/waterlog.txt'
        os.system(command)
        writesession()
        checkfilling()
        time.sleep(5)

def main():



    application = QtWidgets.QApplication(sys.argv)

    mainwindow = mainWindow.mainWindow()

    if not tools.settingsisfilled(configfile):  # проверка на наличие заполненных данных
        settingswindow = settingsWindow.settingsWindow(mainwindow)
        settingswindow.show()
    else:
        mainwindow.setupsettings()
        mainwindow.show()

    logmanagerThread = Thread(target=secondarytasks, daemon=True, args=[mainwindow])
    logmanagerThread.start()

    application.exec_()




if __name__ == '__main__':
    #logmanager()
    main()




