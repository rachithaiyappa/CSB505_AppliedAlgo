fn = lambda x: (x**3)/10

def der2(f):
    h = 0.00001
    return lambda x: (f(x + h) - 2*f(x) + f(x - h))/(h**2)

val = 2.5
print(der2(fn)(val))