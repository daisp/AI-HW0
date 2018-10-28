import functools


def mySum(my_list):
    return functools.reduce(lambda x, y: x + y, my_list)


print(mySum(list(range(1, 5))))  # expected: 1+2+3+4=10
