from PIL import Image


def settingsisfilled(configure):  # проверка на заполнение настроек
    # configure - путь к файлу настроек
    file = open(configure, 'r')
    if len(file.read()) > 0:
        return True

    return False


def createassociativearray(path):
    # создать ассоциативный массив на основе файла в формате ключ:значение

    file = open(path, 'r').read().split('\n')
    array = {}

    for x in file:
        x = x.split(':')
        array[x[0]] = x[1]

    return array


def loadimage(path):
    # уменьшить картинку до нужного размера

    def scale_image(input_image_path=path,
                    output_image_path='photos/sbk_.png',
                    width=531,
                    height=501
                    ):
        original_image = Image.open(input_image_path)
        w, h = original_image.size
        print('The original image size is {wide} wide x {height} '
              'high'.format(wide=w, height=h))

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)
        else:
            # No width or height specified
            raise RuntimeError('Width or height required!')

        original_image.thumbnail(max_size, Image.ANTIALIAS)
        original_image.save(output_image_path)

        scaled_image = Image.open(output_image_path)
        width, height = scaled_image.size
        print('The scaled image size is {wide} wide x {height} '
              'high'.format(wide=width, height=height))
    scale_image()


def writetolog(path):
    file = open('logs/water', 'w')
    file.write(open(path, 'r').read() + '\n')
    file.close()


def reformatQtCalendarDate(calendar):

    date = str(calendar.selectedDate().year()) + '-'
    if len(str(calendar.selectedDate().month())) == 1:
        date += '0' + str(calendar.selectedDate().month()) + '-'
    else:
        date += str(calendar.selectedDate().month()) + '-'

    if len(str(calendar.selectedDate().day())) == 1:
        date += '0' + str(calendar.selectedDate().day())
    else:
        date += str(calendar.selectedDate().day())

    return date





