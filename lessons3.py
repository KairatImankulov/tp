# class Counter():
#     def __init__(self):
#         self.value = 0

#     def inc(self):
#         self.value += 1

#     def dec(self):
#         self.value -= 1

# class NewCounter(Counter):
#     def dec(self):
#         pass

# a = NewCounter()
# print(a.value)
# a.inc
# a.inc
# a.dec
# print
# (a.value)

# class Person():
#     name = "Asan"

#     def working():
#         print('men ui kuram')

# class Architect(Person):
#     pass

# class Programmerr(Person):
#     pass

# print(Programmerr.name)




# class Soda():
    
#     def __init__(self, dobavka = None):
#         self.dobavka = dobavka

#     def show_my_drink(self):
#         if self.dobavka :
#             print(f'gazirovka i {a.dobavka}')
#         else:
#             print('obychna')

# a = Soda()
# a.show_my_drink()


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg

#     def to_pounds(self):
#         return self.__kg * 2.205
    
#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')

#     def get_kg(self):
#         return self.__kg
    
#     kg = property(set_kg, get_kg)

# c = KgToPounds(22) 
# c = KgToPounds() == 10
# c.to_pounds()
# print(c.to_pounds())


# class TriangleChecer():

#     def __init__(self, ls):
#         self.ls = ls
    
#     def is_triangle(self):
#         ls = []
#         for i in ls:
#             if i < 0:
#                 return "С отрицательнымы числоми не выйдет"
#         ls.sort()
#         if ls[0] + ls[1] > ls[2]:
#             return "Можно"
#         else:
#             return "Нельзя"

# a = TriangleChecer([1, 2, 3])
# print(a.is_triangle())
