# num = [1,2,3,4,5]

# list =[25,24,23,22,21]

# def f (numbers):
#   return len(numbers),sum(numbers)

# print(f(list))


states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

m_state = []

for state in states:
    if state.startswith('M'):
        m_state.append(state)
        

print(m_state)
    
   