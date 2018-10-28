import random


def func(x):
    r = random.randint(1, 1001)
    # print("r = {}".format(r))
    return 0 if r > x else r

print(func(100))
