from typing import Any
from functools import total_ordering


@total_ordering
class anything:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __eq__(self, __value: object) -> bool:
        return True

    def __ne__(self, __value: object) -> bool:
        return True

    def __lt__(self, _value):
        return True

    def __ge__(self, _value):
        return True

    def __gt__(self, _value):
        return True

# class AlwaysTrue:
#     def __eq__(self, other):
#         return True

#     __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


# def anything():
#     return AlwaysTrue()



# INPUT DATA:

# TEST_1:
import math, re

print(anything() != [])
print(anything() < "World")
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)

# TEST_2:
print(anything() != set())
print(anything() < {})
print(anything() > ())
print(anything() >= True)
print(anything() <= False)
print(anything() == id)

# TEST_3:
print(anything() != (1, 2, 3))
print(anything() < {4, 5, 6})
print(anything() > range(180))
print(anything() >= {1: "one"})
print(anything() <= ["", [], (), set])
print(anything() == any)
print(anything() != any)
print(anything() > any)
print(anything() < all)
print(anything() <= all)
print(anything() >= all)

# TEST_4:
print(anything() == filter)
print(anything() != filter)
print(anything() < filter)
print(anything() > filter)
print(anything() >= filter)
print(anything() <= filter)
print(anything() == anything())
print(anything() != anything())
print(anything() < anything())
print(anything() > anything())
print(anything() >= anything())
print(anything() <= anything())
