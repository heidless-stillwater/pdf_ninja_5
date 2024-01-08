from icecream import ic

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def func(x):
#     func2 = lambda x: x + 5
#     return func2(x) + 85
#
#
# func3 = lambda x, y: x + y

newList = list(map(lambda x: x + 100, a))

newList1 = list(filter(lambda x: x % 2 == 0, a))

ic(newList)
ic(newList1)
# ic(func2(9))
# ic(func(2))
# ic(func3(10, 20))

