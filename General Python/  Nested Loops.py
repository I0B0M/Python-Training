# Nested Loops

persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    
    for restaurant in restaurants:
        
        print(person +  ' loves '  + restaurant)
        

numbers = [1,2,3]
letters = ['a','b','c']

for number in numbers:
    for letter in letters:
        print(f'{number}{letter}')

persons : ['John','Mary','Pete','Dan']

for person in persons:
    for person in persons:
        print(person +' meets '+person)
        
    
