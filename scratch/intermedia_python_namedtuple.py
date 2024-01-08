
import collections
from collections import Counter
from collections import namedtuple

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

Point = namedtuple('Point', 'x y z')
Point1 = namedtuple('Point', ['x', 'y', 'z'])
Point2 = namedtuple('Point', {'x': 0, 'y': 0, 'z': 0})

newP = Point(3, 4, 5)
newP1 = Point1(3, 4, 5)
newP2 = Point2(3, 4, 5)

p2 = Point._make(['a', 'b', 'c'])
ic(p2)

ic(newP.x, newP.y, newP.z)
ic(newP[0])
ic(newP._asdict())
ic(newP._fields)
ic(newP._replace(y=6))

# ic(newP1)
# ic(newP2)
