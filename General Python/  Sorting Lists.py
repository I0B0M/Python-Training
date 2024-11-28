# Sorting Lists

from operator  import itemgetter
x = [(3,6),(4,7),(5,9),(8,4),(3,1)]

x.sort(key = itemgetter(0))

print(x)

x.sort(key = itemgetter(1))
       
print(x)


