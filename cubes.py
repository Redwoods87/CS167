"""
This program is an example about how return works.
"""

def cube1(x):
    val = x ** 3
    print(val)  # Does not return a value.
    
def cube2(x):
    val = x ** 3
    return(val)     # Returns the value.
    
x = 4
y = cube1(x)
z = cube2(x)

print('y is ' + str(y))
print('z is ' + str(z))