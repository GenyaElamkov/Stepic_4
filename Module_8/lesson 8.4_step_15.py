import functools


class ignore_exception:
    def __init__(self, *type_exp) -> None:
        self.type_exp = type_exp

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exp:
                if not type(exp) in self.type_exp:
                    raise exp    
                print(f"Исключение {type(exp).__name__} обработано")

            # try:
            #     return func(*args, **kwargs)
            # except self.exceptions as e:
            #     print(f'Исключение {e.__class__.__name__} обработано')

        return wrapper


# INPUT DATA:

# TEST_1:
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x
    
func(0)

# TEST_2:
min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))

# TEST_3:
@ignore_exception()
def func():
    raise ValueError
  
try:    
    func()
except Exception as error:
    print(type(error))

# TEST_4:
@ignore_exception(TypeError)
def func():
    raise ValueError
  
try:    
    func()
except Exception as error:
    print(type(error))

# TEST_5:
@ignore_exception(ValueError, TypeError, NameError)
def func():
    raise NameError
 
try:    
    func()
except Exception as error:
    print(type(error))

# TEST_6:
@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def func():
    raise ZeroDivisionError
 
try:    
    func()
except Exception as error:
    print(type(error))

# TEST_7:
@ignore_exception(ValueError, NameError, ZeroDivisionError, TypeError)
def func(a, b, c):
    raise NameError
 
try:    
    func(1, 2, c=10)
except Exception as error:
    print(type(error))

# TEST_8:
@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    """beegeek"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())