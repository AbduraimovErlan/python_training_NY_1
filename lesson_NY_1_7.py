""" lambda, работа с исключениями """

# def is_palindrom(word='hello'):
#     return word == word[::-1]
#     # if word == word[::-1]:
#     #     return True
#     # else:
#     #     return False
#
# print(is_palindrom())

# a = 5
# def f():
#     a = 10
#     print(a)
# print(f())
# print(a)



# def up_letter(word: str): #подсказка чтоб вышло медоты
#     return word.title()
#
#
# def show_words(func, iterable): #если поменять  местами то тоже будеть работать
#     for i in iterable:
#         print(func(i))
#
#
#
# words = ['python', 'bishkek', 'kyrgyzstan']
# show_words(str.upper, words)
# # show_words(len, words)
# # show_words(up_letter, words)


# list_number = [2, 1, 4, 5, 1, 4, 4]
#
# def most_frequence(iterable):
#     most_f = 0
#     for i in iterable:
#         if iterable.count(i) > most_f:
#             most_f = i
#     return f"обьект: {most_f} найдено: {iterable.count(most_f)}" #{most_f: iterable.count(most_f)}
# print(most_frequence(list_number))


# list_number = [2, 1, 4, 5, 1, 4, 4]
#
# def most_frequence(iterable):
#     return sorted(iterable, key=iterable.count)
# print(most_frequence(list_number))


# lambda arguments: expression

# plus = lambda number1, number2: number1 + number2
# print(plus(2, 3))
#
# def plus_d(n1, n2):
#     return n1 + n2
# print(plus_d(2, 3))
#
# print(type(plus))
# print(type(plus_d))



# def show_words(iterable, func): #если поменять  местами то тоже будеть работать
#     for i in iterable:
#         print(func(i))
#
#
#
# # def up_letter(word: str): #подсказка чтоб вышло медоты
# #     return word.title()
#
# words = ['python', 'bishkek', 'kyrgyzstan']
#
# show_words(words, lambda word: word.upper())
#
# # show_words(str.upper, words)
# # show_words(len, words)
# # show_words(up_letter, words)


# map, filter


# numbers = list(range(1, 16))
# print(numbers)
#
#
# # filtered = [i for i in numbers if i > 7]
# # filtered = list(filter(lambda x: x % 2 == 0, numbers))
# # mapped = list(map(lambda x: x**2, numbers))
# # mapped = [i*3 for i in numbers]
# print(filtered)

# dct = {
#     'one': 1,
#     'three': 3,
#     'seven': 7,
#     'two': 2
# }
# print(dct)
# sort_dict = dict(sorted(dct.items(), key=lambda item: item[1]))
# print(sort_dict)



# try:
#     some code
# except:
#     some code
# finally:
#     some code

# name = 'aza'
#
# try:
#     print(name)
# except:
#     print('такой переменной нет')
#     name = 'aza'
# finally:
#     print('проверка завершена')



# word = 'python'
# while True:
#     try:
#         ind = int(input('введите индекс: '))
#         print(word[ind])
#     except IndexError:
#         print("неверный индекс, такого нет")
#     except ValueError:
#         print("вводить только числа")

from random import choice
from time import sleep

students = ['kurmanzhan', 'argen', 'azamat', 'aigerim']

data = {}

while len(students) != 0:
    seconds = 20
    print(students)
    chosen = choice(students)
    name = input(f'отвечает:  {chosen}: ')
    # while seconds != 0:
    #     print(seconds)
    #     sleep(1)
    #     seconds -= 1

    rate = int(input(f'rate for {chosen}'))
    data[chosen] = rate
    students.remove(chosen)
for name, rate in data.items():
    print(name, ":", rate)
print(sum(data.values()) / len(data))