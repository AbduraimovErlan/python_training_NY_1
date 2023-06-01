"""структуры данных список срезы кортежи"""
# tuple - кортеж


# numbers = ((1, 2), (4, 7))
# numbers = list(numbers)
# numbers.append(34)
# numbers = tuple(numbers)
# print(numbers)





# weekend_days = ('sunday', 'saturday', 'monday')
#
# for i in weekend_days:
#     if i == 'monday':
#         break
#     print(i)
# else:
#     print('цикле завершон')

# new = tuple('23')
# new = tuple([int(i) for i in new])
# print(new)


# new = (23,)
# print(new)



# new = tuple('oop')
# print(new)

# weekend_days = ('sunday', 'saturday')#картеж не изменяется
#
# print(weekend_days)
# print(type(weekend_days))


# numbers = ['qwe', 23, 'sdf', 45, 2.5, True, 8.5]
# # numbers = [i for i in numbers if type(i) not in [int, float]] #лист компрехеншин
# # numbers = [i for i in numbers if type(i) == int] #лист компрехеншин
# numbers = [i*2 for i in numbers] #умножить
# print(numbers)


# for i in numbers:
#     print(type(i))

# data = [['hello', 3, 2], ['привет', 4, 2]]
# for i in data:
#     print(f'word: {i[0]} cons: {i[1]} vow:{i[2]}')
#

# sogl = "qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьб"
# glas = "aieouyёнеыаоэяию"
#
# while True:
#     vowels = 0
#     consonants = 0
#     word = input('Введите слова: ').lower()
#     if word == 'exit':
#         break
#     for letter in word:
#         if letter in glas:
#             vowels += 1
#         else:
#             consonants += 1
#     data.append([word, consonants, vowels])
#     print(
#         f'слова: {word}\n'
#         f'количество букв: {len(word)}\n'
#         f'гласных: {vowels} \nсогласных: {consonants}'
#     )
# print(data)





# list = список ( изменение тип данных)
# print(type(object))

# new = list(range(1, 6))



# objects = ['бегайм', 'арген', 'эльхан', 'азамат']
# new = objects.copy()
# # new[0] = 'amir'
# print(objects == new)
# print(objects is new)
# print(id(objects))
# print(id(new))
# print(objects)
# print(new)






# objects = [24, 13, 2.7, 1.38]
""" изменение """


# new_sorted= []
# new_sorted = sorted(objects)
#
# print(objects)
# print(new_sorted)

# objects.sort(key=len, reverse=True) #сортировать по длине слов и переаернуть их

# objects.sort(reverse=True) #переаернуть сортировку

# objects.sort() # сортировка

# objects[objects.index(13)] = [23, 45, 6] # аоставить список на место индекса

# objects[3:5] = ['php', 'c++']# поставить на место по индексу оптом

# objects[-3] += 3 # изменить определенно

# objects = objects[::-1]

# objects[3], objects[4] = objects[4], objects[3] # заменяет место





""" добавление """

# objects += new

# objects.extend(new)  # заливается в список
# objects.insert(4, new) #вставит в определенные место

# objects.append(new) # вставит в коноец
# print(objects)


""" удаление """


# del objects[1:-1] #удаление текста
# print(objects)

# # objects.pop(1)   # удаление по индекс
# deleted = objects.pop(1)
# print(deleted)
# objects.remove(24)    # удаление по значение
# objects.remove('python')
# print(objects)
# objects.clear() #удулить полностью
# print(objects[3:6])

# print(objects, new, sep='\n')