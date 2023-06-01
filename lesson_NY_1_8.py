# ten = list(range(1, 11))
#
# def get_object(lst=ten):
#     while True:
#         ind = input('введите индекс: ')
#         if ind == 'q':
#             break
#
#         try:
#             print(lst[int(ind)])
#         except:
#             print(f'введите индекс от 0 до {len(lst) -1}')
#
#
# words = ['python', 'bishkek', 'geektech']
# get_object()

""" работа с файлами"""
# w -write (перезапись)
# a - add  (дозапись)
# x - бесконфликтный режим записи
# r - чтение

#
# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()


# with open('file2.txt', 'x') as file:
#     file.write('\nтретья стока')

import time

# with open('file.txt', 'r') as file:
#
#     print(file.readlines()[2])
    # for i in file.readlines():
    #     time.sleep(2)
    #     print(i)

    # for i in file.read():
    #     time.sleep(0.01)
    #     print(i, end='')

    # file.readline() #пропустить строчку
    # file.readline()
    # print(file.read())
    # print(file.read())

    # print(file.readline())
    # print(file.readlines()[:2])

from random import choice

with open('students.txt', 'r') as students:
    students_list = students.readlines()
    students_list = [i.rstrip() for i in students_list]
    with open('materials.txt') as materials:
        materials_list = materials.readlines()
        materials_list = [i.rstrip() for i in materials_list]
        with open('results.txt', 'a') as results:
            while len(students_list) > 0:
                print("осталос студентов", len(students_list))
                chosen_students = choice(students_list)
                chosen_material = choice(materials_list)
                rate = int(input(
                    f'{chosen_students}\n'
                    f' тема: {chosen_material}:\n'
                    f'оценка: '))
                results.write(
                    f'имя: {chosen_students} тема: {chosen_material}: '
                    f'оценка: {rate}\n')
                students_list.remove(chosen_students)





