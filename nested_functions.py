def functionA(a, b, c):
    value = a
    value = value + functionB(b, c) + functionC(y = b, x = a)
    return value

#function B does not care what the arguments are called, but it does care about the order. 
def functionB(x, y): 
	value = x * y    
	return value

#function C does care -- this is the difference between args and kwargs
def functionC(x = 'a', y = 'b'):
	return x + y

# Oops, we forgot to pass any arguments :(
result = functionA(1,1,1)
print(result)


""" 
Function B and C only exist LOCALLY within function A, it's not a global function
"""