""" функции, аргументы: *args,  **kwargs. """
# DRY - don't repeat yourself
# def - definite (определить)

# width = 6
# length = 8
# square_2 = width * length
# print(square_2)
#
#
# width = 12
# length = 18
# square_hall = width * length
# print(square_hall)

# def show_objects():
#     print("Hello")
#
#
# show_objects()
# show_objects()
# show_objects()


# def show_objects(name, surname):# name - required positional argument
#     print("Hello", name, surname)
#
#
# show_objects('peter', 'perker')# peter - required positional argument


# def show_objects(name, surname='unknown'):# name - required positional argument
#     print("name:", name, "surname:", surname) # surname - not required positional argument
#
#
# show_objects('peter', 'perker')# peter - required positional argument
# show_objects(surname='lee', name='bruce')# keyword argument прописали явным оброзом

#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# print(len('123') + 7)
# print(len1('123') + 7)

# max = 0
# [23, 56, 12, 34, 75, 91, 26, 0.5]


# def max1(iterable):
#     iterable = sorted(iterable)
#     return iterable[-1]
# print(max1([11, 4, 7, 9]))

# def get_square(width, length):
#     return width * length
#
# square_2 = get_square(6, 8)
# square_hall = get_square(12, 18)
#
# print(square_2, square_hall, sep='\n')

# def get_square(width, length):
#     return width * length
#
# square_2 = get_square(int(input('width: ')), int(input('length: ')))
# square_hall = get_square(12, 18)
#
# print(square_2, square_hall, sep='\n')

# def get_square(width, length):
#     return width * length
#
# n1 = int(input('width: '))
# n2 = int(input('lenght: '))
#
# square_2 = get_square(n1, n2)
# square_hall = get_square(12, 18)
#
# print(square_2, square_hall, sep='\n')


# def max1(iterable):
#     max_value = 0
#     for i in iterable:
#         if i > max_value:
#             max_value = i
#     return max_value
# print(max1([3, 76, 1, 4, 9, 2, 6, 8, ])) # максимальное число в списке с помощю фуекции


# print(help(len))
# print(len.__doc__)


# def get_square(width: int, length: int) -> int:
#     """ принимает 2 числа (ширина и длина )
#     вазврашает площадь прямоугольника"""
#     return width * length
#
# print(help(get_square))
# print(get_square.__doc__)


# def plus(*args):
#     print(type(args))
#     # return args
#     return sum(args)
#
# print(plus(2, 4, 5, 8, 78, 45, 12))

# def plus(a, *args, b=90):
#     print(a, b, args)
#     # return args
#     return sum(args)
#
# print(plus(2, 4, 5, 8, 78, 45, 12))



# def menu(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     return kwargs
#
# menu(eat='pizza', drink='tea', one=1, book='lutz')
#
# contacts = {
#     'sam': '0500100200',
#     'aza': '0700223311',
#     'uri': '0555788877',
#
# }
#
# def new_cantact(name, phone):
#     if name not in contacts.keys():
#         contacts[name] = phone
#     else:
#         contacts[name] = {contacts[name]}
#         contacts[name].add(phone)
#
# def delete(value):
#     command = input('выберите удаление: 1) по имени 2) по  номеру')
#     if command == '1':
#         if value in contacts.keys():
#             del contacts[value]
#         else:
#             print(f'нет такаго контакта {value}')
#     if command == '2':
#         for name, phone in contacts.items():
#             if value == phone:
#                 del_contact = name
#         del contacts[del_contact]
#
# delete('0700223311')
#
# print(contacts)


# a = [1, 2, 3, 4]
# for i in a:
#     if i == 3:
#         a.remove(i)
#     print(i)

