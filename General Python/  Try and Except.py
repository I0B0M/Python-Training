# Try and Except 

(dir(__builtins__))

try :
    1/0

except ZeroDivisionError:
    print('Divided by Zero')
    
print('Should Reach Here')

try :
    open(fantasy.txt)
    
except:
    print('File not present')
    
print('Should Reach Here')


try :
    x = int(input('Enter Number:'))
    x = x + 1
    print(x)
    
except :
    print('Invalid Input')
    
    
def fail():
    1/0
    
try :
    fail()
    
except :
    print('Exception Occured')
    
finally :
    print('Program Continues')
    
    
try:
    f = open('test.txt','r')
    
except:
    print('File Not Valid')
    
finally:
   if f:
       f.close()
       print('Program Continues')
        
   print('Program Continues')
    

def lunch():
    print('Do You Want Lunch')


try:
    lunch()
  
except SyntaxError:
  print('Fix your syntax')
except TypeError:
  print('Oh no! A TypeError has occured')
except ValueError:
  print('A ValueError occured!')
except ZeroDivisionError:
  print('Did by zero?')
else:
  print('No exception')
finally:
  print('Ok then')
  
raise MemoryError('Out Of Memory')

raise SyntaxError('Invalid Input')

class LunchError(Exception):
    pass

raise LunchError('Programmer went to Lunch')

class NoMoneyException(Exception):
    pass

class OutOfBudget(Exception):
    pass

balance =  int(input('Enter A Balance : '))

if balance <= 1000:
    raise NoMoneyException

elif balance >= 10000:
    raise OutOfBudget


