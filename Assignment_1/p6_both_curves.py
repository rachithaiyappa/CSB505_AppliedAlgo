import matplotlib.pyplot as plt
import numpy as np

def derivative(f):
    h = 0.00001
    return lambda x: (f(x + h) - f(x - h))/(2*h)

data = np.linspace(-10,10,100)
f1 = lambda x : (1/10)*(x**3)

# f1_values = (1/10)*(data**3)

#explicitly creating arrays
f1_values = np.array([f1(d) for d in data])
f2_values = np.array([derivative(f1)(d) for d in data])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')

ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.title('$f(x) = (1/10)x^3$ \n $f\'(x) = (3/10)x^2$')

plt.plot(data,f1_values,'r',label = 'function f(x)')
plt.plot(data,f2_values,'b', label = 'derivative f\'(x)')
plt.legend()
plt.show()

