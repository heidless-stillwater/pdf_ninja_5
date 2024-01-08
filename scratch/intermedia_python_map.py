from icecream import ic

# map
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x**x

#
# newList = []
# for x in li:
#     newList.append(func(x))
#
# ic(newList)


ic(list(map(func, li)))
ic(map(func, li))


# comprehension example
ic([func(x) for x in li if x % 2 == 0])
