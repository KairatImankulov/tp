# import random
# random = random.randint(1, 15)
# while True:
#     n = int(input('Введите число: '))
#     if n < random:
#         print('Число меньше')
#     elif n > random:
#         print('Число больше')
#     else:
#         n == random
#         print('Вы угадали')
#         break

# text = input('type a text: ')
# ls = text.split()
# count_of_word = len(ls)
# count_of_sentence = text.count('.')
# print(count_of_word, count_of_sentence)

# import random
# type_of_password = int(input('type: '))
# password = ''
# alfa = 'abcdefghijklmnopqrstuwxyz'
# if type_of_password == 1:
#     for i in range(8):
#         password = password + alfa[random.randrange(1, 26)]
# else:
#     type_of_password == 2
#     for i in range(8):
#         password = password + str(random.randrange(0, 10))
# print(password)

# name = input()
# if name[::-1] == name[::1]:
#     print('True')
# else:
#     print('False')

# name = input()
# s = ''
# dict = {}
# for i in name:
#     if i not in s:
#         dict[i] = name.count(i)
#         s += i
# print(dict)
# for i in name:
#     if i in dict:
#         dict[i] + dict[i] + 1
#     else:
#         dict[i] = 1
# print(dict)    

name = input()
p = len(name)
print(p)
t = False
for i in name:
    if i == "a":
        t = True
        break
print(t)
