# Round() Function

import  random

def truncate(num):
    return(int(num*1000))/1000

arr = [random.uniform(0.01,0.05) for _ in range(1000000)]
sum_num = 0
sum_truncate = 0

for i in arr:
    sum_num = sum_num + i
    sum_truncate = truncate(sum_truncate + i)
    
print('Testing by using truncating upto 3 decimal places')
print('The original sum is =',sum_num)
print('The total using truncate =',sum_truncate)
print('The difference from original - truncate =',sum_num-sum_truncate)

print('/n/n')
print('Testing by using round() upto 3 decimal places')
sum_num_1 = 0
sum_truncate_1 = 0

for i in arr:
    sum_num_1 = sum_num_1 + i
    sum_truncate_1 = round(sum_truncate_1 + i,3)
    
print('The original sum is =',sum_num_1)
print('The total using round =',sum_truncate_1)
print('The difference from original - round =',sum_num_1-sum_truncate_1)


# testing round() 

float_num1 = 10.60 # here the value will be rounded to 11 as after the decimal point the number is 6 that is >5 

float_num2 = 10.40 # here the value will be rounded to 10 as after the decimal point the number is 4 that is <=5

float_num3 = 10.3456 # here the value will be 10.35 as after the 2 decimal points the value >=5 

float_num4 = 10.3445 #here the value will be 10.34 as after the 2 decimal points the value is <5 

print("The rounded value without num_of_decimals is :", round(float_num1))
print("The rounded value without num_of_decimals is :", round(float_num2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num3, 2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num4, 2))
 
print("The rounded value without num_of_decimals is :", truncate(float_num1))
print("The rounded value without num_of_decimals is :", truncate(float_num2))
print("The rounded value with num_of_decimals as 2 is :", truncate(float_num3))
print("The rounded value with num_of_decimals as 2 is :", truncate(float_num4))
 
import numpy as np

arr_1 = [-0.341111,1.4555098989,4.232323,-0.3432326,7.626632,5.122323]

arr_2 =  np.round(arr,2)

print(arr_2)