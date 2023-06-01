
""" Циклы for, while """
# c = 0
#
# while c != 100:
#     c += 1
#     if c % 2 != 0:
#         print('мы прорустили!')
#         continue
#     print('hello', c)

# amount = int(input('сколько раз будем повторять код?'))
# while amount != 0:
#     time = input(f'введите время суток: \n остталось попыток {amount}: ')
#
#     if time == 'morning' or time == 'утро':
#         print('good morning!')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print("hello, I don't know time!")
#     amount -= 1

# from time import sleep
# amount = 3
# while amount != 0:
#     time = input(f'введите время суток: \n остталось попыток {amount}: ')
#
#     if time == 'morning' or time == 'утро':
#         print('good morning!')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print("hello, I don't know time!")
#         amount -= 1
#         if amount == 0:
#             seconds = 20
#             while seconds != 0:
#                 print(seconds)
#                 sleep(1)
#                 seconds -= 1
#             amount = 3



# rounds = 0
# while rounds != 5:
#     rounds += 1
#     if rounds == 3:
#         continue
#     print(f'круг: {rounds}')


# word = "трактор синий"
# c = 0
# while c != len(word):
#     print(word[c])
#     c += 1


# i - item, iterable

# word = "geektech"
# for letter in word:
#     if letter == 't':
#         continue
#     print(letter)

#
# for number in range(1, 11):
#     if number % 2 != 0:
#         print(number)

# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             print(i, j, k)


# cash = 100
# years = 5
# percents = 0.05
#
# for years in range(years):
#     cash += cash * percents
#     print(f'год: {years} {cash}')
#
# print(cash)



eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. "
rus = "йцукенгшщзхъфывапролджэячсмитьбю "

while True:
    word = input('\nвведите слова: ').lower()
    if word == 'exit':
        break
    for letter in word:
        if letter in eng:
            print(rus[eng.index(letter)], end='')
        else:
            print(eng[rus.index(letter)], end='')


