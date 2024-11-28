# Lambda Functions

main = lambda x,y : x + y

print(main(1,2))

string = 'some kind of useless lambda'

print(lambda string:print(string))

(lambda string : print(string))(string)

#A REGULAR FUNCTION
def guru( funct, *args ):
 funct( *args )
def printer_one( arg ):
 return print (arg)
def printer_two( arg ):
 print(arg)

#CALL A REGULAR FUNCTION 
guru( printer_one, 'printer 1 REGULAR CALL' )
guru( printer_two, 'printer 2 REGULAR CALL \n' )

#CALL A REGULAR FUNCTION THRU A LAMBDA
guru(lambda: printer_one('printer 1 LAMBDA CALL'))
guru(lambda: printer_two('printer 2 LAMBDA CALL'))

(lambda x : x + x)(2)

sequences = [10,2,8,7,5,4,3,11,0,1]

filtered_results = filter(lambda x : x > 4,sequences)

print(list(filtered_results))

filtered_results_2 = map(lambda x: x*x,sequences)

print(list(filtered_results_2))

from functools import reduce

set = [1,2,3,4,5]

product = reduce(lambda x,y : x*y,set)

print((product))