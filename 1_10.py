import functools


def checkNumber(x, num):  # checks whether num is divisible by x and x!=num
    if num % x == 0 and num != x:
        return True
    return False


def isPerfectNumber(num):
    return True if functools.reduce(lambda x, y: x + y,
                                    [x for x in list(range(1, num + 1, 1)) if checkNumber(x, num)]) == num else False

print(isPerfectNumber(4)) # expected: False
print(isPerfectNumber(6)) # expected: True
print(isPerfectNumber(25)) # expected: False
print(isPerfectNumber(28)) # expected: True
print(isPerfectNumber(492)) # expected: False
print(isPerfectNumber(496)) # expected: True
print(isPerfectNumber(8127)) # expected: False
print(isPerfectNumber(8128)) # expected: True



