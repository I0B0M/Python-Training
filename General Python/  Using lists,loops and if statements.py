# Using lists,loops and if statements

states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

start_m_state = []
any_m_state = []
end_m_state = []

for state in states:
    if state.startswith('M'):
        start_m_state.append(state)
        
print(start_m_state)

for state in states :
    if 'm' in state.lower() :
        any_m_state.append(state)
        
print(any_m_state)

for  state in states:
    if state.endswith('m'):
        end_m_state.append(state)
    