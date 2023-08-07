#name = "Kairat"
#age = "17"
#print("Menin atym {} men {} jashtamyn".format(name , age))

#print("Как вас зовут?")
#name = input()
#print("Здраствуйте, " + name + "!")


#a = int(input('Биринчи сан: '))
#b = int(input('Экинчи сан: '))
#c = int(input('Учунчу сан: '))

#print(a + b + c)

#a = int(input("Биринчи сан: "))
#b = int(input("Экинчи сан: "))
#print(a * b * 0.5)

#n = int(input("Окучуулар: "))
#k = int(input("Алмалар: "))
#print(k // n)
# print(k % n)

#n = int(input("Убакыт: "))
#print(n // 60, n % 60)


#name = input("Как вас зовут? ")
#print("Здраствуйте, " + name + "!")

#a = int(input("Число: "))
#b = a + 1
#print("Следующее число: ", b)
#c = a - 1
#print("Предыдущее число число: ", c)

#a = int(input())
#b = int(input())
#c = int(input())
#d = a + b + c
#print(d / 2)


#for l in [["Tom", 39, 45, 37], ["Alise", 33], ["Bob", 27]]:
#    for item in l:
#        print(item, end=", ")
#    print()


#ls = [1, 2, 3, 4, 5, 9, 7]
#for l in range(0, len(ls), 2):
#    print(ls[l])

#for l in  [1, 5, 3, 8, 4, 6, 7]:
#    if l % 2 == 0:
#        print(l)

#for l in  [1, 5, 3, 8, 4, 6, 7]:
#    if l % 2 != 0:
#        print(l)

#for l in  [1, 5, 3, 8, 4, 6, 7]:
#    print(l ** 2)

#for l in  [1, 5, 3, 8, 4, 6, 7, 4]:
#    if l == 4:
#        print(l)

#a = ("abrakadabra")
#print(a[2])
#print(a[9])
#print(a[-1:-2])
#print(a[-1:-2])
#print(a[::2])
#print(a[1::2])
#print(a[::-1])
#print(a[::2],-1)
#print(len[a])

#s = 'abcdefg'
#print(s[1])
#print(s[-1])
#print(s[1:3])
#print(s[1:-1])
#print(s[:3])
#print(s[2:])
#print(s[:-1])
#print(s[::2])
#print(s[1::2])
#print(s[::-1])


#my_list = [2, 4, 8]
#print(my_list[::-1])

#my_list = [1, 2, 3]
#my_list2 = my_list[0]
#my_list[-1] = my_list2
#my_list[0] = my_list1
#print(my_list)

#a = int(input())
#b = int(input())
#c = int(input())
#if a > b:
#    if a > c:
#        print(a)
#    else:
#        print(c)
#else:
#    if b > a:
#        if b > c:
#            print(b)
#        else:
#            print(c)


#n = int(input("chislo: "))
#for i in range(n):
#    print(i ** 2)


#ans = True
#ls = ["Bekbolsun", "Kairat", "Magdixan", "Munar", "Altynai"]
#a = input("slovo: ")
#for i in range(len(ls)):
#    if ls(i) == a:
#        ans = True
#print(ans)



#Задача 1
#Есть список 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Выведите все элементы, которые меньше 5.ответ: a=[1, 1, 2, 3]
# for i in a:
#     if i < 5:
#         print(i)

#Задача 2
#Даны списки:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
#ответ: [1, 2, 3, 5, 8, 13]

#Задача 3
#Посчитайте, сколько раз символ встречается в строке.
#a = "Python Software Foundation" 
#--> input менен
#symvol = "o" --> input менен
#ответ ----> 4

# london = {
#     'id': 1,
#     'name': 'London',
#     'it': 320,
#     'number': 99,
#     'to_name': None,
#     'about': {
#         'population': 2343,
#         'gradus': 35,
#         'code': 1212,
#     }
# }
# #ключ аркылуу маанилерин алуу
# id = london["id"]
# name = london.get("name")
# new_dict = london["about"]
# print(id, name, new_dict)

# london["number"] = 200
# print(london.items())
# print(london.keys())
# print(london.values())

# del london['name']
# print(london)

# r1 = {'name': 'London', 'location': 'London Str'}
# r1. update({"model": "apple", "ios": 15})

# resume = {
#     'name': 'Kairat',
#     'age': 17,
#     'skills': ['run', 'swim', 'sport'],
#     'fav_thing': {'sport': 'спорт', 'food': 'еда'},
#     'purposeful': True
# }
# a = resume["age"]
# print(a + 7)
# resume['age'] = 24 #print(a + 7)

# p = resume['purposeful']
# if p == True:
#     print('Отлично! я верю в тебя!')
# else:
#     print('Просто ты еще не нашел(нашла) свою мечту')

# s = resume['skills']
# f = resume['fav_thing']
# print(f, s[1], s[2])


# Ex1 Скрабл
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R - 1 очко;
# D, G - 2 очка;
# B, C, M, P - 3 очка;
# F, H, V, W, Y - 4 очка;
# K - 5 очков;
# J, X - 8 очков;
# Q, Z - 10 очков.

# e = 'qwertyuiopasdfghjklzxcvbnm'
# ls = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                  4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# word = input('Введите слово : ')
# if word[0].lower() in e:
#     summa = 0
#     for letter in word:
#         for key, value in ls.items():
#             if letter.upper() in value:
#                 summa += key
#     print(f'{summa}')

# Ex2 email
# Нужно дополнить код таким образом, 
# чтобы он вывел все адреса в формате имя_пользователя@домен.
# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#       	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#       	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#       	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#       	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#       	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

# n = int(input("chislo: "))
# summa = 1
# summ = 0
# s = 0
# for i in range(1, n):
#    summa = summa * i
#    summ = summ + i ** 2
#    s = s + i
# print(summa)
# print(summ)
# print(s)

# fruits = {
#     "apple": 45,
#     "cherry": 65,
#     "orange": 786,
#     "strawberery": 897,
# }
# o = fruits["orange"]
# print(o)

# f = fruits["apple"] = 80
#  print(f)

# fruits.update({"banan": 215,})
# print(fruits)

# (fruits.keys()
# print(fruits.values())

# fruits.pop("cherry")
# print(fruits)



# st = set((input()).split())
# st_2 = set((input()).split())
# print(st & st_2)


# nums = [n for n in range(10) if n < 5]
# print(nums)

# n = [i for i in range(5, 50, 5)]
# print(n)

# fruits = {
#     'orange': 55,
#     'apple': 45,
#     'banana': 35,
# }
# d = {k: v + 100 for k, v in (fruits.items())}
# print(d)

# a = [i + j for i in [1, 2] for j in [10, 20]]
# print(a)

# a = [i + j if j > 15 else i for i in [1, 2] for j in [10, 20]]
# print(a)

# a = [i for i in range(-100, 100) if i  5 and 3 ]
# print(a)

# a = [f"{i} * {j} = {i * j}" for i in range(1, 6) for j in range(1, 11)]
# print(a)

# sl = input("slovo: ")
# di = {}
# for i in sl:
#     if i != ' ':
#         if i in di:
#             di[i] = di[i] + 1
#         else:
#             di[i] = 1
#     else:
#         continue
# print(di)

# def countFood():
#     a = int(input())
#     b = int(input())
#     print('всего', a + b, 'шт')
# print('сколько бананов и ананасов для обезьян?')
# countFood()


# password = ("gwerty", "keykey")
# pas = input()
# def check_password(pas):
#     if pas in password:
#         print('razreshon')
#     else:
#         print('zapreshon')
# check_password(pas)

# dlina = int(input())
# vertical = int(input())
# ravno = 0
# def kvadrat(d, v):
#     dlina * vertical == ravno
# kvadrat(dlina, vertical)



# 1 задача
# sum_of_numbers(start, end) деген функция тузгуло эки аргумент кабыл алат, 
# start дан баштап end ге чейинки сандардын суммасын чыгаргыла end озун кошуп(включительно). 
# Эгер start, end ден чон болуп калса анда экобун орун алмаштырып койгула. Мисалы:
# sum_of_numbers(1, 3) -->  6
# sum_of_numbers(3, 5) --> 12
# sum_of_numbers(5, 10) --> 45

# def sum_of_numbers(start, end):
#     print(sum(range(start, end+1)))
# a = int(input())
# b = int(input())
# if a > b:
#     c = a
#     a = b
#     b = c
# sum_of_numbers(a, b)


# 2 задача
# 3 аргумент кабыл алган арифметикалык функцияны жазыңыз: 
# биринчи экобу сандар, үчүнчүсү алар менен аткарыла турган операция. 
# Үчүнчү аргумент + болсо, аларды кошуңуз; эгерде -, анда кемитүү; * көбөйтүү; /  бөлүү (биринчини экинчиге). 
# Болбосо, "Белгисиз операция" сабын кайтаргыла. мисалы:
# ariphmetic(5, 3, "*") --> 15
# ariphmetic(5, 3, "+") --> 8
# ariphmetic(5, 3, "-") --> 2
# ariphmetic(5, 3, "/") --> 1.6
# ariphmetic(3, 5, "#") --> Белгисиз операция

# def arifmetic(a, b, oper):
#     rezult = 0
#     if oper == '+':
#         rezult = a + b
#     elif oper == '-':
#         rezult = a - b
#     elif oper == '*':
#         rezult = a *b
#     elif oper == '/':
#         rezult = a / b
#     else:
#         print('tuura emes operation')
#     print(rezult)
# bir = int(input())
# eki = int(input())
# oper = input('operation ')
# arifmetic(bir, eki, oper)


# 3
# 1 аргументти кабыл алган мезгил функциясын жазыңыз - айдын санын (1ден 12ге чейин) 
# жана бул ай таандык болгон жылдын убактысын (кыш, жаз, жай же күз) кайтарат. Мисалы
# is_season(2) --> "кыш"
# is_season(4) --> "жаз"
# is_season(6) --> "жай"
# is_season(9) --> "куз"

# def is_season(n):
#     rezult = ' '
#     if 2 < n < 6:
#         rezult = 'Jaz'
#     elif 5 < n < 9:
#         rezult = 'Jay'
#     elif 8 < n < 12:
#         rezult = 'Kuz'
#     elif n == 12 or 1 <= n < 3:
#         rezult = 'Kysh'
#     else:
#         rezult = 'tuura emes ai berildi'
#     return rezult
# ai = int(input('ai: '))
# ans = is_season(ai)
# print(ans)


# def printScores(student, *scores):
#     print(f"student name: {student}")
#     print("student name: " + {student})
#     for score in scores:
#         print(score)
# printScores("Jonathan", 100, 95, 90, 88)

# def printPetNames(owner, **pets):
#     print(f"Owner Name: {owner}")
#     for pet,name in pets.items():
#         print(f"{pet}: {name}")
# printPetNames("Jonathan", dog = "Brock", fish = ["Larry", "Curly"], turtle = "sherly")

# elements = ['aidana', 'Bekbolsun', 'kairat']
# el = sorted(elements)
# print(el)

# def factorial(n):
#     if n == 0:
#         return 1 
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))
# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
# print(factorial(5))

# def factorial(n):
#     if n == 0:
#         return 0 
#     else:
#         return n + factorial(n - 1)
# print(factorial(3))

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(10))

# name = 'Tom'
# def say_hi():
#     global name
#     name = 'Bob'
#     print('Hello', name)
# def say_bye():
#     print('Good bye', name)
# say_hi()
# say_bye()

# list_of_words = ['one', 'two', 'list', ' ', 'dict']
# map(str.upper, list_of_words)
# my_list = list(map(str.upper, list_of_words))
# print(my_list)

# nums = list(map(int, input().split()))
# rezult = []
# for i in nums:
#     rezult.append(i ** 2)
# print(rezult)

# nums = list(map(int, input().split()))
# rezult = []
# for i in nums:
#     if i % 2 == 0:
#         rezult.append(i)
# print(rezult)

# nums = []
# nums2 = []
# list(map(lambda x, y: x * y, nums, nums2))

# a = int(input())
# b = int(input())
# if a % b == 0:
#     print('bolunot')
# else:
#     print('bolunboit')

# ip = [111, 112, 113, 114, 115]
# n = list(map(lambda x: "ip ={} ".format(x) , ip))
# print(n)

# a, b = map(int, input().split())
# print(a + b)


# 1. үч аргумент кабыл алган функция түзгүлө, 
# үчөөнүн эн чоңун кайтарган. Мисалы
# greater(3, 6, 1) ---> 6
# def greater(a, b, c):
#     if a > b:
#         print(a) if a > c else print(c)
#     else:
#         print(b) if b > c else print(c)
# bir = int(input('Birinchi san: ')) 
# eki = int(input('Ekinchi san: '))
# uch = int(input('Uchunchu san: '))
# greater(bir, eki, uch)

# 2. төрт аргумент кабыл алган функция түзгүлө, 
# өсүү тартибинде(по возрастанию) список кылып чыгаргыла. Мисалы
# sorting(2,6,5,9) ---> [2, 5, 6, 9]
# n = list(map(int, input().split()))
# def sorting(*args):
#     new=args[0]
#     new.sort()
#     print(new)
# sorting(n)

# # 3. беш аргумент кабыл алган функция түзгүлө, 
# # кемүү  тартибинде(по убыванию) список кылып чыгаргыла. Мисалы
# # sorting(2,6,5,9, 8) ---> [9, 8, 6, 5, 2]
# n = list(map(int, input().split()))
# def sortingg(*args):
#     news = args[0]
#     news.sort(reverse=True)
#     print(news)
# sortingg(n)


# n = input()
# cifra = input()
# suma = 0
 
# # while n > 0:
# #     i = n % 10
# #     suma = suma + i
# #     n = n // 10
 
# # print("Сумма:", suma)

# for i in n:
#     if cifra == i:
#         suma += 1
# print(suma)

# nums = input()
# sum = " "

# # for i in range(1, nums + 1):
# #     sum += i
# # print(sum)

# for i in nums:
#     sum += str(int(i) + 1) 
# print(sum)