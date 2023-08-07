# a = [7, 2, 1, 13, 9]


# target = 10 

# el_dict = {}
# for i, item in enumerate(a):
#     diff = target - item
#     if diff in el_dict:
#         print([el_dict[diff], i])
#         break
#     el_dict[item] = i


# # quicksort
# def quicksort(ls):
#     if len(ls) < 2:
#         return ls
#     else:
#         pivot = ls[0]
#         less = [i for i in ls[1:] if i <= pivot]
#         greeter = [i for i in ls[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greeter)

# print(quicksort(a))






# # Тапшырма:
# # Текст берилет text =input()
# # Ичиндеги тамгалардын канча жолу кезиккенин санаш керек
# # Мисалы : menin atym asan ---> a -2
# # S-1
# # N-3
# # E-1
# # I-1
# # Y-1
# # T-1
# def count_of_l(text):
#     count_of_letter = {}
#     count_of_vowel = ['a', 'o', 'u', 'i', 'y', 'e']
#     for i in text:
#         if i in count_of_vowel:
#             if i in count_of_letter:
#                 count_of_letter[i] = count_of_letter[i] + 1
#             else:
#                 count_of_letter[i] = 1
#     return count_of_letter
# text = input()
# print(count_of_l(text))



# # Спсисок берилет ичинде сандар 2 так бөлүнгөндөрдү чыгар мисалы:
# # [3,4,9,5,6,2,46,84,7]--->[4,6,2,46,84]
# ls = [3,4,9,5,6,2,46,84,7]
# def delit(ls):
#     new_ls = []
#     for l in ls:
#         if l % 2 == 0:
#             new_ls.append(l)
#     return new_ls
# print(delit(ls))



# # Список берилет ичиндеги сандардын квадратын чыгар 
# # [2,5,1,4,3] ----> [4,25,1,16,9]
# ls = [2,5,1,4,3] 
# def kvadrat(ls):
#     for l in ls:
#         print(l ** 2)
# kvadrat(ls)



# # Список берилет 2 жана 3 так бөлүнгөн жана 30 кичине болгон сандарды чыгар мисалы :
# # [66, 12, 24, 96, 6, 7] ---> [12,24,6]
# ls = [66, 12, 24, 96, 6, 7]
# def list(ls):
#     for l in ls:
#         if l % 2 == 0:
#             if l % 3 == 0 and l < 30:
#                 print(l)
# list(ls)



# random модулу аркылуу 20 чейин сан алабыз случайно анан ошол санга чейин список тузуп чыгарабыз мисалы :
# random 3 деген сан кайтарса анда программа [1,2,3] деген жооп чыгарыш керек
# from random import *








import csv

data = [['hostname', 'vendor', 'model', 'location'],
       ['sw1', 'Cisco', '3750', 'London, Best str'],
       ['sw2', 'Cisco', '3850', 'liverpooi, Beeter str'],
       ['sw3', 'Cisco', '3650', 'liverpooi, Beeter str'],
       ['sw4', 'Cisco', '3650', 'London, Best str']]
          
with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open ('sw_data_new.csv') as f:
    print(f.read())



from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d"))

# twent_two =_may