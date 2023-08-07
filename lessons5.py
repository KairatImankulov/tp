# ls = [[1, 2, ['Ok!', 3]], ['list', 4], 5]
# print(ls[0][2][0])

# ls = ['Санкт', '+', 'Петербург']
# ls[1] = '-'
# print(ls[0], ls[1], ls[2])

# ls = ['a', '1', 'b', '2', 'c', '3']

# l = ls[0], ls[2], ls[4]
# s = ls[1], ls[3], ls[5]
# del ls
# print(l)
# print(s)

# a = [1, 2, 3, 4, 5]
# b = a[0] + a[1] + a[2]
# a = [b, b, b, + a[3], a[4]]
# a.append(7)
# print(a)




# dict = {'1': 1.29, '2': 0.43}
# d = dict['1']
# i = dict['2']
# print(d * i)

# d = {'a': 1, 'b': 2, 'c': 3}
# d.pop('c')
# print(d)
# d.__delitem__('a')
# print(d)
# d.clear()
# print(d)


# l = ['Pn', 'Vt', 'Sr', 'Cht', 'Pt', 'Sb', 'Vs']
# d = {
#     'd2': 'Pn',
#     'd2': 'Vt',
#     'd3': 'Sr',
#     'd4': 'Cht',
#     'd5': 'Pt',
#     'd6': 'Sb',
#     'd7': 'Vs',
# }
# print(d)

# Дан словарь с товарами. 
# Выведите на экран все товары, 
# цена которых не превышает 100 рублей, 
# а текущий остаток не менее 10 кг. 
# goods = {
#      "apple": {"name": "Яблоки", "cost": 25, "kg": 30},
#      "pear": {"name": "Груши", "cost": 50, "kg": 5},
#      "plum": {"name": "Сливы", "cost": 55, "kg": 25},
#      "cherry": {"name": "Вишни", "cost": 110, "kg": 15}
# }
# n = goods["apple"]
# p = goods["pear"]
# l = goods["plum"]
# c = goods["cherry"]
# print(n)
# print(p)
# print(l)
# print(c)
# print(n.values())

# Поменяйте в словаре 
# d = {1: '1', 2: '2', 3: '3', 4: '4'} 
# ключи и значения местами. Выведите итоговый словарь на экран.

# for i in range(1, 100):
#     i = i + 1
# print(i)

# n = int(input())
# s = 0
# i = 1
# while s <= n:
#     s = s + i
#     i = i + 1
# print(s)

# from math import *
# print(pow(2, 5))
# print(sqrt(25))
# print(ceil(5.3))
# print(floor(5.8))


# letter = input()
# key = 'qwertyuiopasdfghjklzxcvbnm'
# index = key.find(letter)
# if letter == 'm':
#     print('q')
# else:
#     print(key[index + 1])





# a, b = map(int, input().split())
# c = a ** b
# print(c[-1])