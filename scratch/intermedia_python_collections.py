
# import collections
from collections import Counter
from icecream import ic

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Containers
    # list
    # set
    # dict
    # tuple - immutable

# Types
    # counter
    # deque
    # namedTuple
    # orderDict
    # defaultDict

# learn #1
# c = Counter('gallad')
# ic(c)
#
# c = Counter(['a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd'])
# ic(c)
#
# e = Counter({'a': 1, 'b': 2})
# ic(e)
#
# d = Counter(cats=1, dogs=2)
#
# ic(list(c.elements()))
# ic(c.most_common(2))
#
#
#
# # learn #2
# c = Counter(a=4, b=2, c=0, d=-2)
# d = ['a', 'b', 'b', 'c']
#
# ic(c)
#
# c.subtract(d)
# ic(c)
#
# c.update(d)
# ic(c)
#
# c.clear()
# ic(c)


# learn 3
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

ic(c + d)
ic(c - d)
ic(c & d)
ic(c | d)


