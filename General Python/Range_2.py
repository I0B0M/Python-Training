# Range()

def first_function():
     for f in range(10):
        print(f,end =' ')
    
def second_function():
    for i in range(2,11,1):
        print(i,end = ' ')
    

def third_function():
    for j in range(3,28,3):
        print(j,end= ' ')
        
def fourth_function():
    for k in range(15,5,-1):
        print(k,end = ' ')
        
import random

def fifth_function():
    for h in [random.uniform(1.5,10.5) for _ in range (100)]:
        print(h,end = ' ')
    
arr_list =  ['Mysql','Mongodb','PostgreSQL','Firebase']

for m in range(len(arr_list)):
    print(arr_list[m],end=' ')
    
print(m)

print(list(range(11)))

def get_alphabets(start_letter,end_letter,step):
    for c in range(ord(start_letter.lower()),ord(end_letter.lower()),step):
        yield chr(c)

print(list(get_alphabets('i','z',1)))

start_value = range(5)[0]
print('The first element in range is =',start_value)

second_value = range(5)[1]
print('The second element in range is =',second_value)

last_value = range(5)[-1]
print('The first element in range is =',last_value)

print(list(range(10)))

from inertools import chain

print('Merging two range into one')
frange  = chain(range(10), range(10,20,1))

for a in range:
    print(a,end =' ')
    
import numpy as np

for i in np.arange(10):
    print(i,end = ' ')
    
for a in np.arange(0.5,1.5,0.2):
    print(a,end = ' ')