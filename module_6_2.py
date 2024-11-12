class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = str(new_color)
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def get_model(self, __model):
        self.__model = __model

    def get_horsepower(self, __engine_power):
        self.__engine_power = __engine_power

    def get_color(self, __color):
        self.__color = __color

    def print_info(self):
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')




class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
