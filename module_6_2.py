class Vehicle() :
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
        return self.__model
    def get_horsepower(self):
        return self.__engine_power
    def get_color(self):
        return self.__color
    def set_color(self,new_color):
        nc = False
        for i in self.__COLOR_VARIANTS:
            if i == new_color.lower():
               nc=True

        if nc:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на',new_color)

    def print_info(self):
        print('Модель:',self.get_model())
        print('Мощность двигателя:', self.get_horsepower())
        print('Цвет:', self.get_color())
        print('Владелец:', self.owner)


class Sedan(Vehicle):
        __PASSENGERS_LIMIT = 5



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()