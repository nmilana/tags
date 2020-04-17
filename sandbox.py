import os
import random

lst = os.listdir(f'txt')
print(lst)
print(len(lst))

print(random.randint(0, len(lst) - 1))