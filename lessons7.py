# fruits = {'alma': 5, 'almurut': 10, 'banan': 12}
# # power_of_price() деген функция туз, бааларынын квадратын list кылып чыгарып бер. мисалы:
# # power_of_price(fruits) ---> [25, 100, 144]
# fruits = {
# 'alma': {'sale': 10, 'price': 5},
# 'almurut': {'sale': 55, 'price': 10}, 
# 'banan': {'sale': 40, 'price': 12}
# }
# # price_of_fruit() деген функция туз,  скидкасы 30 дан жогору болгон жемиштердин атын list кылып чыгарып бер. мисалы:
# # power_of_price(fruits) ---> [“almurut”, “banan”]
# def power_of_price(fruits):
#     f = fruits.values()
    
#     list[f]
#     print(list)

# def price_of_fruit(fruits):
#     ls = []
#     for i in fruits:
#         if fruits[i]['sale'] > 30:
#             ls.append(i)
#     return ls

# power_of_price(fruits)





# fruits = {
# 'alma': {'sale': 10, 'price': 5, 'size': {'text': ['M', 'L', 'XL'], 'num': [44, 46, 48]}},
# 'almurut': {'sale': 55, 'price': 10, "size": {"text": ["XS", "S", "M"], "num": [42, 44, 46]}}, 
# 'banan': {'sale': 40, 'price': 12, "size": {"text": ["x", "XL", "XXL"], "num": [54, 56, 58]}}
# }
# def power_of_price(fruits):
#     dict = {}
#     for i in fruits:
#         dict[i] = fruits[i]['size']['num']
#     return dict
# print(power_of_price(fruits))
