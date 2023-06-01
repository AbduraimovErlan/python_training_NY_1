# bool - boolean (логический)
# print(type(True))
# print(bool())

"""операторы сравнения"""
# print(2 == 3)
# print(2 != 4)
# print(2 > 3)
# print(2 < 3)
# print(2 >= 2)
# print(2 > 2 or 2 == 2)
# print(2 > 1 and 2 < 4)
# print(4 > 2 > 1)
#
# print(not True)
#
"""операторы назначения"""
#
# a = 10
# a = a + 7
# a += 7
# print(a)

# time = 'в'
# temperature = 13
#
# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print("Hello, I don't know time!")
#     if temperature < 10:
#         print('одевайся теплее')
#     elif 10 < temperature < 20:
#         print('на улице прохладно')
#     else:
#         print('тепло')

# [start:stop:step]
# word = '123456789'
# first = int(word[:2])
# sliced = int(word[-2:])
# [-3] [5:]
# [::2] шаг
# [2:6] отрезок
# [3:] до конца


# print(first + sliced)
# print(word[0])
# print(word[4])

# print(word.startswith('1'))
# print(word.isalpha())
# print(word.isnumeric())


# word = input('введите слова').lower()
# reversed_word = word[::-1]
# if word == reversed_word:
#     print(True)
# else:
#     print(
#         f'слова {word} на равно обратному слову {reversed_word}'
#     )



# login = 'aza@mail.com'
# password = 'qwer12'
#
# input_login = input('укажите логин: ')
#
# if input_login == login:
#     input_password = input(f'логин верный \n укажите пароль для {input_login}: ')
#     if input_password == password:
#         input_password2 = input('подвердите пароль: ')
#         if input_password == input_password2:
#             print(f'уважаемый {input_login}, вы успешно авторизовались!')
#         else:
#             print('пароли не совпадают!')
#     else:
#         print("неверный пароль!")
# else:
#     print(f'логин "{input_login}" не сушествует! ')