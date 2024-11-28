# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# language  = 'Java'

if language == 'Python':
  print('Language is Python')
elif language == 'Java':
  print('Language is Java')
else :
    print('no match')


 

# Else is always used at the end of it statements 
# Elif used for continious if statements


# and 
# or
# not
# "or" "not" can be subsituited with and

user ='Admin'
logged_in = True

if user == 'Admin' and logged_in == True:
    print('Admin Page')

 else :
    print('Wrong Credentials')
    
a=[1,2,3]
b=[1,2,3]

if a == b:
    print('Equal')
    
print(id(a))
print(id(b))
print(a is b)
