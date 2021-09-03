import matplotlib.pyplot as plt
import numpy as np

data = np.linspace(-10,10,100)
fn = (1/10)*(data**3)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')

ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.title('$f(x) = (1/10)x^3$')
plt.plot(data,fn,'r')
plt.show()

