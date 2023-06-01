# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#
#     def info(self):
#         return f'Name: {self.name} age: {self.age} birth year: {self.calculate_birth_year()}'
#
#     def calculate_birth_year(self):
#         return 2023 - self.age
#
# animal = Animal('My animal', 3)
# # animal.age = 4
# print(animal.info())
#

class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age attribute it must be a positive number')
        if isinstance(address, Address):
            self.__address = address
        else:
            raise ValueError('Wrong value for address attribute it must be of Address data number')
        self.__was_born()
        self.__address = address




    def __was_born(self):
        print(f'Animal {self.__name} was born!')

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if isinstance(value, int) and value > 0:
            self.__age = value
        else:
            raise ValueError('Wrong value for age attribute it must be a positive number')

    def info(self):
        return f'Name: {self.__name} age: {self.__age} birth year: {self.calculate_birth_year()}\n' \
               f'Address Info: {self.__address.city}, {self.__address.street}, {self.__address.number}'

    def calculate_birth_year(self):
        return 2023 - self.__age

    def speak(self):
        raise NotImplementedError('Method not realized')

class Cat(Animal):
    def __init__(self, name, age, address):
        super(Cat, self).__init__(name, age, address)


    def speak(self):
        print('Myayuu')




class Dog(Animal):
    def __init__(self, name, age, commands, address):
        super(Dog, self).__init__(name, age, address)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def speak(self):
        print("Gaaav")



    def info(self):
        return super(Dog, self).info() + f'\ncommands: {self.__commands} '


class Parrot(Animal):
    def __init__(self, name, age, address):
        super(Parrot, self).__init__(name, age, address)

    def speak(self):
        print('Rrrroman')


class Fish(Animal):
    def __init__(self, name, age, address):
        super(Fish, self).__init__(name, age, address)

    def speak(self):  
        print("Fish says nothing")




store_address = Address('Bishkek', 'Sovetskaya', 5)

animal = Animal('My animal', 3, Address('LA', 'Walk street', 23))
animal.set_age(7)
print(animal.info())
# animal.__was_born()

dog = Dog('Snoppy', 1, 'Sit, Run', store_address)
dog.commands = 'Sit, Run, Bark'
print(dog.commands)
# print(dog.info())

cat = Cat('Tom', 2, store_address)
# print(cat.info())

fish = Fish('Nemo', 5, store_address)

parrot = Parrot('Roman', 10, store_address)
# print(parrot.info())

# store_address.number = 8
# print(cat.info())
# print(dog.info())

animals_list = [dog, cat, fish, parrot] #полиморфно даем каманду /// пишем один раз для всех
for animal in animals_list:
    print(animal.info())
    animal.speak()