# class MusicPlayable:#миксины не имеет конструктор
#
#     def play_music(self, song):
#         print(f'Now is playing {song}')
#
#     def stop_music(self):
#         print(f'Music stopped')
#
# class Drawable:
#     def draw(self, emoji):
#         print(emoji)
#
#
# class SmartPhone(MusicPlayable, Drawable):
#     pass
#
#
#
# class Car(MusicPlayable, Drawable):
#     def __init__(self, model, year):
#         self.__model = model
#         self.__year = year
#
#
#     @property
#     def model(self):
#         return self.__model
#
#     @property
#     def year(self):
#         return self.__year
#
#
#     def drive(self):
#         print('I can drive')
#
#     def __str__(self):
#         return f'Model: {self.__model} year: {self.__year}'
#
#
# class FueCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self, model, year)
#         self.__fuel_bank = fuel_bank
#
#
#     @property
#     def fuel_bank(self):
#         return self.__fuel_bank
#
#     def drive(self):
#         print('I can drive by using fuel')
#
#
#     def __str__(self):
#         return super().__str__() + f' fuel bank: {self.__fuel_bank}'
#
# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year)
#         self.__battery = battery
#
#
#
#     @property
#     def battery(self):
#         return self.__battery
#
#     @battery.setter
#     def battery(self, value):
#         self.__battery = value
#
#     def drive(self):
#         print('I can drive by using electricity')
#
#     def __str__(self):
#         return super().__str__() + f' battery: {self.__battery}'
#
#
# class HybridCar(FueCar, ElectricCar): #тот кто стоить первым имеет приоритет
#     def __init__(self, model, year, fuel_bank, battery):
#         FueCar.__init__(self, model, year, fuel_bank)
#         ElectricCar.__init__(self, model, year, battery)
#
#
#
# my_car = Car("BMW X7", 2020)
# print(my_car)
#
# toyota_car = FueCar('Toyota Camry', 2019, 80)
# print(toyota_car)
#
#
# tesla_car = ElectricCar('Tesla Model S', 2023, 45000)
# print(tesla_car)
#
#
# prius_car = HybridCar('Toyota Prius', 2021, 45, 20000)
# print(prius_car)
# prius_car.drive()
# print(HybridCar.mro())
# print(HybridCar.__mro__)
#
# prius_car.play_music('Morgenstein')
# samsung_phone = SmartPhone()
# samsung_phone.play_music('Morzart')
# samsung_phone.stop_music()
# samsung_phone.draw("📱")
# prius_car.draw("🚗")

import enum
class Color(enum.Enum):
    WHITE = 1
    BLACK = 2
    PINK = 3
    PURPLE = 4



class MusicPlayable:#миксины не имеет конструктор

    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print(f'Music stopped')

class Drawable:
    def draw(self, emoji):
        print(emoji)


class SmartPhone(MusicPlayable, Drawable):
    pass



class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if isinstance(color, Color):
            self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year


    def drive(self):
        print('I can drive')

    def __str__(self):
        return f'Model: {self.__model} year: {self.__year} color: {self.__color}'

    def __gt__(self, other): #сравнение
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year




class FueCar(Car):
    __total_fuel = 1000

    @classmethod#не зваимодействует
    def get_total_fuel(cls):
        return cls.__total_fuel

    @staticmethod
    def get_fuel_type():
        return "AI - 95"

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FueCar.__total_fuel -= self.__fuel_bank


    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'I can drive by using fuel {self.model}')


    def __str__(self):
        return super().__str__() + f' fuel bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank

class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery



    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print('I can drive by using electricity')

    def __str__(self):
        return super().__str__() + f' battery: {self.__battery}'


class HybridCar(FueCar, ElectricCar): #тот кто стоить первым имеет приоритет
    def __init__(self, model, year, color, fuel_bank, battery):
        FueCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)



my_car = Car("BMW X7", 2020, Color.BLACK)
print(my_car)

toyota_car = FueCar('Toyota Camry', 2019, Color.PURPLE, 80)
print(toyota_car)


tesla_car = ElectricCar('Tesla Model S', 2023, Color.PINK, 45000)
print(tesla_car)


prius_car = HybridCar('Toyota Prius', 2021, Color.WHITE, 45, 20000)
print(prius_car)
prius_car.drive()
print(HybridCar.mro())
print(HybridCar.__mro__)

prius_car.play_music('Morgenstein')
samsung_phone = SmartPhone()
samsung_phone.play_music('Morzart')
samsung_phone.stop_music()
samsung_phone.draw("📱")
prius_car.draw("🚗")


number_1 = 9
number_2 = 7
print(f'Is Number one bigger than Number two: {number_1 > number_2}')
print(f'Is Camry fresher than Prius: {toyota_car > prius_car}')
print(f'Is Camry older than Prius: {toyota_car < prius_car}')
print(f"Is Camry's year the same with Prius's year: {toyota_car == prius_car}")
print(toyota_car + prius_car)

print(str(FueCar.get_total_fuel()) + '' + FueCar.get_fuel_type())


if tesla_car.color == Color.PINK:
    print("Car is beautiful")
    
if prius_car.model == "Prius":
    print('Nice choice')
# FueCar.__total_fuel -= 100
# print(FueCar.__total_fuel)