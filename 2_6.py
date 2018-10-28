import random

def func(num,my_list):
    new_list=[]
    for i in range(0,num):
        r = random.choice(my_list)
        new_list.append(r)
        my_list.remove(r)
    return new_list

print(func(3,list(range(0,10))))