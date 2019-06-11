import RPi.GPIO as GPIO
import time
from datetime import timedelta, datetime, date
import random
from threading import Thread


# глобальные переменные
FEEDLEVEL = 20  # уровень воды
UPDATE = 1  # интервал обновления
WATERPIN = 22  # пин датчика воды
cTIME = 0

def gpiosetup():
    GPIO.setmode(GPIO.BOARD)  # чтение по номеру порта на плате
    GPIO.setup(WATERPIN, GPIO.IN)  # 
    '''питание кнопки через 3в
        питание платы через 5в
        
    '''
    GPIO.setup(15, GPIO.IN)  #  чтение кнопки
    GPIO.setup(11, GPIO.OUT)  # включить подачу еды
    GPIO.output(11, False)
    GPIO.setup(12, GPIO.OUT)  # включить подачу воды
    
def gettime():
    now = datetime.now()
    return str(now)

def writewaterfile():
    
    import subprocess
    import os
    
    now = datetime.now()  # текущие дата и время
    date_ = str(date.today())  # текущая дата
    
    lastday = str()  # день последней записи в логи
    with open('currentday', 'r') as cd:  # чтение дня последней записи
        lastday = cd.read()
    
    if date_ != lastday:  # проверка файла. в файл должны записываться только логи с одинаковой датой
        with open('currentday', 'w') as currentday:
            currentday.write(str(date_))
            
        with open('waterlog.txt', 'w') as currentdate:  # используется для того, чтобы очистить файл
            currentdate.close()
    
    with open('waterlog.txt', 'a') as file:
        if not GPIO.input(WATERPIN):
            file.write('no water; ' + str(now) + '\n')
        #else:
            #file.write('there is water; ' + str(now) + '\n')
        global cTIME
        cTIME = str(now)
        
            
    
    subprocess.call('./script.sh')  # запуск скрипта, отправляющего файлы на сервер 
    print('it was pushed')

def writefeed(time):
    with open('waterlog.txt', 'a') as file:
        file.write('no feed; ' + str(time) + '\n')
        
def addwater():
    GPIO.output(12, True)
    GPIO.setmode(GPIO.BOARD)
    while not GPIO.input(WATERPIN):
        print('добавляю воду')
        time.sleep(1)
    GPIO.output(12, False)
        

def addfeed():
    global FEEDLEVEL
    
    GPIO.output(11, True)  # включаем подачу корма
    
    while FEEDLEVEL < 100:
        FEEDLEVEL += random.randint(20, 35)
        time.sleep(1)
        print('добавляю еду')
        
    GPIO.output(11, False)  # выключаем подачу корма
        
    FEEDLEVEL = 100
    
    writefeed(gettime())

def animalsimulator():
    GPIO.setmode(GPIO.BOARD)
    while True:
        if not GPIO.input(15):
            global FEEDLEVEL
            FEEDLEVEL -= random.randint(5, 15)
            print(FEEDLEVEL)
        time.sleep(0.5)
        #print(GPIO.input(15))
    
def main():

    while True:
    
        if not GPIO.input(WATERPIN):  # добавляем воду, если она кончилась
            thread = Thread(target=addwater)
            thread.start()
            
            
        if FEEDLEVEL <= 0:  # тут будет добавляться еда, если ее нет
            thread = Thread(target=addfeed)
            thread.start()
        
            
        print(GPIO.input(WATERPIN), 'water') # текущее значение на порте
        currenttime = datetime.now()
        #writewaterfile()
        
        time.sleep(UPDATE)
        
def test():
    gpiosetup()
    g = False
    while True:
        print('z\ya tutu')
        if not GPIO.input(15):
            GPIO.output(11, g)
            g = not g
            time.sleep(0.5)
            
def starttest():
    try:
        test()
    except KeyboardInterrupt:
        print("Выход из системы")
    except SystemExit:
        print('Stopped')
    finally:
         GPIO.cleanup()  # сброс портов
         print('gpio cleaned')

def startmain():
    
    
    gpiosetup()  # инициализация портов gpio
    simulator =Thread(target=animalsimulator, daemon=True)
    simulator.start()
    
    try:
        main()
    except KeyboardInterrupt:
        print("Выход из системы")
    except SystemExit:
        print('Stopped')
    finally:
         GPIO.cleanup()  # сброс портов
         print('gpio cleaned')
         
if __name__ == '__main__':
    startmain()
    #starttest()
