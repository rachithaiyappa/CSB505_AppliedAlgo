def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def f1(n, acc=1):
    if n == 0:
        return acc
    else:
        return f1(n-1, acc*n)

def f3(n):
    v = 1
    for i in range(n,0,-1):
        v *= i
    return v

print(f(5), f1(5), f3(5))

print(f3(2021))