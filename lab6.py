class Lamp:
    def __init__(self, red, green, blue, light):
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__isOn = False
        self.__light = light

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, value):
        if value < 0 or value > 255:
            print('Неверное значениe')
        self.__red = value

    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, value):
        if value < 0 or value > 255:
            print('Неверное значениe')
        self.__green = value

    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, value):
        if value < 0 or value > 255:
            print('Неверное значениe')
        self.__blue = value
    @property
    def isOn(self):
        return self.__isOn

    def turn_on(self):
        print('Включение лампы...')
        self.__isOn = True

    def turn_of(self):
        print('Выключение лампы...')
        self.__isOn = False

    @property
    def light(self):
        return self.__light

    @light.setter
    def light(self, value):
        if value >= 1 and value <= 100:
            self.__light = value
        else:
            print('Значение яркости может быть только от 1% до 100%')

    def check_status(self):
        lamp_state = 'Включена' if self.isOn else 'Выключена'
        print(f'Состояние лампы: {lamp_state}')




lamp = Lamp(255, 255, 255, 100)
lamp.check_status()
lamp.turn_on()
lamp.check_status()

class ColorizedLamp(Lamp):
    def colorized_lamp(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        print('Цвет лампы изменён!')

    def check_status(self):
        lamp_state = 'Включена' if self.isOn else 'Выключена'
        print(f'Состояние лампы: {lamp_state} \n Яркость лампы: {self.light} \n Цвет лампы: {self.red}, {self.green}, {self.blue}')


new_lamp = ColorizedLamp(255, 255, 255, 100)
new_lamp.turn_on()
new_lamp.check_status()
new_lamp.colorized_lamp(255, 0, 0)
new_lamp.light = 80
new_lamp.turn_of()
new_lamp.check_status()
new_lamp.light = 101