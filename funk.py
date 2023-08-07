# словарьдын ичинен ар бир элементин текшергиле 
# значениеси ключунон канчага чон мисалы:
d = {1: 10, 2: 20, 3: 30}
# def greater_in(d) функция тузгуло
# функция мындай жооп кайтарат: [9, 18, 28]
def greater_in(d):
    ls = []
    for key, value in d.items():
        a = value - key
        ls.append(a)
    return ls

def sum_of_two_numbers(a, b):
    return a + b

def sub_of_two_numbers(a, b):
    return a - b


def mul_of_two_numbers(a, b):
    return a * b

def div_of_two_numbers(a, b):
    return a / b

# def do_reverse(one_number, second_number):
#     numbers = second_number.split()
#     numbers.reverse()
#     while one_number != 0:
#         n = numbers[0]
#         print(n + " ", end = "")
#         numbers.pop(0)
#         one_number = len(numbers)
        
# def enia(nums):
#     numbers = list(map(int, nums.split()))
#     mult = 1
#     for i in numbers:
#         mult = mult * i
#     return mult * 2

if __name__ == '__main__':
    print(greater_in(d))
    print(sum_of_two_numbers(5, 5))
    print(sub_of_two_numbers(5, 5))
    print(mul_of_two_numbers(5, 5))
    print(div_of_two_numbers(5, 5))
    # one_number = int(input())
    # second_number = input()
    # do_reverse(one_number, second_number)
    # text = input()
    # print(enia(text))

