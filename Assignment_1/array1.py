import numpy as np
import random as rn

def search1(v, d_array):
    for i in range(0,d_array.shape[0]):
        if v == d_array[i]:
            print("found {0} at {1}".format(v,i))

def search2(v, d_array):
    for i,j in enumerate(d_array):
        if v == j:
            print("found {0} at {1}".format(v,i))

def search3(v, d_array):
    if np.any(d_array[:] == v):
        print("found")

data = [0,1,10,2,1,23,1]

da1 = np.array(data)
da2 = np.empty(7)
da3 = np.empty((2,3))

print(data)
print(da2)
da2 = da1
print(da2)
da2[0] = -1000
print(da1)
print(da3)

for i in range(da3.shape[0]):
    for j in range(da3.shape[1]):
        da3[i][j] = rn.randint(-5,5)
        print(da3)
        search1(23,da1)
        search2(23,da1)
        search3(23,da1)