fn = input("input function: ")
fn = eval("lambda x: " + fn)
val = float(input("value: "))

def derivative(f):
    h = 0.00001
    return lambda x: (f(x + h) - f(x - h))/(2*h)

print(derivative(fn)(val))