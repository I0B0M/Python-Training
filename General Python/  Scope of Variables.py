# Scope of Variables

balance = 100

def add_amount(x):
    global balance
    
    balance = balance + x
    
add_amount(5)
print(balance)

def reduce_amount(y):
    global balance
    
    balance = balance - y
    
reduce_amount(5)
print(balance)