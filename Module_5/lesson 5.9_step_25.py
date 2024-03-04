def limited_hash(left, right, hash_function=hash):
    def wrapper(args):
        result = hash_function(args)
        arr = list(range(left, right + 1))
        if result in arr:
            return result

        while True:
            if result > right:
                return arr[(result - right - 1) % (right - left + 1)]
            if result < left:
                return arr[-((left - result) % (right - left + 1))]

    return wrapper


# Вариант решения.
# def limited_hash(left, right, hash_function=hash):
#     def inner_hash_function(x):
#         return left + (hash_function(x) - left) % (right - left + 1)
#     return inner_hash_function



# hash_function = limited_hash(10, 15)

# print(hash_function(10))
# print(hash_function(11))
# print(hash_function(15))


# hash_function = limited_hash(10, 15)

# print(hash_function(16))
# print(hash_function(17))
# print(hash_function(21))
# print(hash_function(22))
# print(hash_function(23))


# hash_function = limited_hash(10, 15)

# print(hash_function(9))
# print(hash_function(8))
# print(hash_function(4))
# print(hash_function(3))
# print(hash_function(2))


hash_function = limited_hash(2, 3, hash_function=lambda obj: len(str(obj)))

print(hash_function('a'))
print(hash_function('ab'))
print(hash_function('abc'))
print(hash_function('abcd'))
print(hash_function('abcde'))
print(hash_function('abcdef'))
print(hash_function('abcdefg'))
