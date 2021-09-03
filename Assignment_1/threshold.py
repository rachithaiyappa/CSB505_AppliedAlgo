import neuron
import random as rn

for _ in range(5):
    data = rn.randint(-10,10)
    print("{0:>4} {1:>4}".format(data, neuron.f(data)))