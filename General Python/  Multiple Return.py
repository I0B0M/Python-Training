# Multiple Return

def complex_function(a,b):
    
    sum = a + b
    
    return sum

def get_person():
    name = 'John'
    age = 32
    country = 'UK'
    
    return name,age,country

name,age,country = get_person()

print(name)
print(age)
print(country)

def f(a,b):
    
    sum = a+b
    cords = a,b
    
    return sum,cords
    
a=5
b=3

sum,cords = f(a,b)

print(sum)
print(cords)


def info():
    name = 'Sam'
    age = 22
    height = 173
    weight = 84
    IQ = 120
    
    return name,age,height,weight,IQ


name,age,height,weight,IQ = info()

print(name)
print(age)
print(height)
print(weight)
print(IQ)


