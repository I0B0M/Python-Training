#Calculator

print("Welcome")

first_input = float(input("Input Your First Value:" ))

operator_input = input("Input Your Operator:" )

second_input = float(input("Input Your Second Value:" ))


if operator_input == '+''add' :
    result = first_input + second_input
    
elif operator_input == '-''subtract' :
    result = first_input - second_input
    

elif operator_input == 'x'or'*' :
    result = first_input * second_input
    
elif operator_input == '/' :
    result = first_input / second_input
    
else: result  = "Invalid Operator"

if isinstance(result,float) and result.is_integer():
    result = int(result)

print("The result is:", result)
