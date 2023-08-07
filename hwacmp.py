# разворот
# one_number = int(input())
# second_number = input()

# def do_reverse(one_number, second_number):
#     numbers = second_number.split()
#     numbers.reverse()
#     while one_number != 0:
#         n = numbers[0]
#         print((n + " "), end="")
#         numbers.pop(0)
#         one_number = len(numbers)

# do_reverse(one_number, second_number)




# автобусная экскурсия
# BUS_HEIGHT = 437
 
# def mainn():
#     _ = int(input())
#     a = map(int, input().split())
#     for index, bridge_height in enumerate(a):
#         if bridge_height <= BUS_HEIGHT:
#             print(f"Crash {index + 1}")
#             return
#     print("No crash")

# if __name__ == "__main__":
#     mainn()




# a = input()
# if a[::-1] == a[::1]:
#     print('YES')
# else:
#     print('NO')



# k = int(input())
# v = ['VGC', 'CVG', 'GCV']

# if k % 3 == 1:
#     print(v[0])
# elif k % 3 == 2:
#     print(v[1])
# else:
#     k % 3 == 0
#     print(v[2])





# m1, m2, m3 = map(int, input().split())
# if min(m1, m2, m3) > 94 and max(m1, m2, m3) < 727:
#     if m1 > m2:
#         if m1 > m3:
#             print(m1)
#         else:
#             print(m3)
#     else:
#         if m2 > m1:
#             if m2 > m3:
#                 print(m2)
#             else:
#                 print(m3)
# else:
#     print('Error')

# numbers = list(map(int, input(). split()))
# maximum = max(numbers[0], numbers[1], numbers[2])
# minimum = min(numbers[0], numbers[1], numbers[2])
# if minimum < 94 or maximum > 727:
#     print('Error')
# else:
#     print(maximum)

# ls = [[7, 6, 8], [5, 4, 3]]
# s = 0
# for i in range(len(ls)):
#     for j in range(len(ls[i])):
#         if ls[i][j] > s:
#             s = ls[i()][j]
# print(s)

# d = {
#     1: [1, 4, 7],
#     2: [8, 7, 12],
#     3: [24, 67, 13]
# }
# s = []
# for i in d.values():
#     s.append(max(i))
# print(max(s))

# dt = {'a': 35, 'b': 55, 'c': 75}

# for i in dt.keys():
#     dt[i] += 5 
# print(dt)



# import random
# alfa = 'abcdefghijklmnopqrstuvwxyz'
# dt = {}
# for k, v in enumerate(alfa):
#     dt[k] = v
# print(dt)
# # numbers = []
# for i in range(10):
#     numbers.append(random.randrange(1, 25))

# def create_word(nums):
#     word = ''
#     for i in nums:
#         word = word + alfa[i]
#     return word
# print(create_word(numbers))




# сбор землянки
# x, y, z = map(int, input().split())

# a = x + y - z

# print('Impossible' if a < 0 else a)


# Время года
# a=int(input())

# if a > 12:
#     print('Error')

# elif a == 1 or a == 2 or a == 12:
#     print('Winter')

# elif a == 3 or a == 4 or a == 5:
#     print('Spring')

# elif a == 6 or a == 7 or a == 8:
#     print('Summer')

# else: 
#     a == 9 or a == 10 or a == 11
#     print('Autumn')


# От перестановки чисел что то меняется
# a1, a2, a3 = map(int, input(). split())
# answer = 'NO'
 
# if a1 + a2 == a3 or a1 + a3 == a2 or a2 + a3 == a1:
#     answer = 'YES'
 
# print(answer)




# a = {'first': 34, 'second': 74, 'third': 15}
# key = ''
# min = a.values()[0]
# for i, value in a:
#     if value < min:
#         min = value
#         key = i
# print(key)



# alfa = 'abcdefghijklmnopqrstuvwxyz'

# a = 'munar'
# letter = {}
# for i ,item in enumerate(a):
#     letter[item] = alfa.index(item)
# print(letter)


# import random
# numbers = []
# for i in range(10):
#     numbers.append(random.randrange(1, 10))
# print(numbers)


# users = { 
#     'ids': [9, 4, 5, 4], 
#     'numbers': [10, 34, 34, 92],  
#     'sizes': [52, 3, 23, 54] 
# } 

# minimum = []
# for i in users.values():
#     minimum.append(min(i))
# print(min(minimum))

# us = {}
# for k, v in users.items():
#     us[k] = list(set(v))
# print(us)

# ids = [9, 4, 5, 4]
# m = ids[0]
# for i in ids:
#     if i > m:
#         m = i
# print(m)

# a = ['five', 'six', 'seven']
# b = [5, 6, 7]
# di = {}
# for i in range(len(a)):
#     di[a[i]] = b[i]
# print(di)


