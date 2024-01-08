
import collections
from collections import Counter
# from collections import namedtuple
from collections import deque

from icecream import ic

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

d = deque('hello', maxlen=5)
ic(d)
ic(d.maxlen)

d.append(1)
ic(d)

d.extend([1, 2, 3])
ic(d)


#
# d.append('4')
# d.append(5)
#
# d.appendleft(15)
# ic(d)
#
# d.pop()
# ic(d)
#
# d.popleft()
# ic(d)
#
# d.clear()
# ic(d)
#
# d.extend('456')
# d.extend('hello')
# d.extend([1,2,3])
# d.extendleft('hey')
#
# d.rotate(-2)
#
# ic(d)
#


