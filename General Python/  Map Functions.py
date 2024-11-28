# Map Function

def f(n):
   return n*n

list_1 = [2,3,4,5,6,7,8,9]
list_2 = [2,3,4,5,6,7,8,9,10,11,12]

updated_list_1 = map(f,list_1)

print(updated_list_1)
print(list(updated_list_1))

from itertools import zip_longest

