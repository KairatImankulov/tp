# # *тапшырма-1:*
# # Напишите скрипт Python для объединения следующих словарей для создания нового.

# # Берилет :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# # жыйынтык : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# merget_dict = {**dic1, **dic2, **dic3}
# print(merget_dict)


# # тапшырма-2
# # Напишите скрипт Python, чтобы проверить, существует ли данный ключ в словаре.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# # is_key_in_dict(x) деген функция тузгуло ушул функцияны чакырганда d ичинен издейсинер барбы же жокпу
# key = int(input('key: '))
# def is_key_in_dict(key):
#     if key in d:
#         print('yes')
#     else:
#         print('no')
# is_key_in_dict(key)


# # тапшырма-3
# # словарьдын ичинен ар бир элементин текшергиле значениеси ключунон канчага чон мисалы:
# d = {1: 10, 2: 20, 3: 30}
# # def greater_in(d) функция тузгуло
# # функция мындай жооп кайтарат: [9, 18, 28]
# def greater_in(d):
#     ls = []
#     for key, value in d.items():
#         a = value - key
#         ls.append(a)
#     return ls
# print(greater_in(d))


# # тапшырма-4
# # эки сан берилет a, b
# # a дан b га чейинки сандарды ключу сан өзу значениеси анын квадраты кылып чыгар. мисалы:
# a = int(input('a: '))
# b = int(input('b: '))
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# def value_exponentiation(a, b):
#     dict = {}
#     for i in range(a, b):
#         dict[i] = i ** 2
#     return dict
# print(value_exponentiation(a, b))


# # тапшырма-5
# # Напишите скрипт Python для объединения двух словарей Python.
# merget_dict = {**dict, **dict}
# print(merget_dict)


# # тапщырма-6
# my_dict = {1: 2, 2: 3, 3: 4}
# print(sum(my_dict.values()) + sum(my_dict.keys()))


# # тапшырма-7
# myDict = {'a':1,'b':2,'c':3,'d':4}
# # функция туз бир аргумент кабыл алат, словарьдын ключу
# # myDict ощол элементин очуруш керек
# # мисалы:
# # delete_elem(“b”)
# # result —>  {'a':1,'c':3,'d':4}
# def delete_elem(myDict):
#     dell = myDict.pop('b')
#     print(myDict)
# delete_elem(myDict)


# # тапшырма-8
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# # эки лист берилет словарь туз! функция эки лист кабыл алат, 
# # чакырганда словарь кайтарат мисалы 
# # {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
# def two_list_dict(keys, values):
#     dict = {}
#     for i in range(len(keys)):
#         dict[keys[i]] = values[i]
#     return dict
# print(two_list_dict(keys, values))


# # тапшырма-9
# # словарьдын бир элементин очургон функция тузгуло
# # мисалы:
# myDict = {'a':1,'b':2,'c':3,'d':4}
# # def remove_emt(‘a’) —> myDict = {'b':2,'c':3,'d':4}\
# def remove_emt(myDict):
#     del myDict['a']
#     print(myDict)
# remove_emt(myDict)


# # тапшырма-10
# # словарьдын маанилеринин max жана min тапкан функция туз
# my_dict = {'x':500, 'y':5874, 'z': 560}
# # max = 5874
# # min=500
# def max_min(my_dict):
#     max_val = max(my_dict.values())
#     min_val = min(my_dict.values())
#     print(max_val)
#     print(min_val)
# max_min(my_dict)
