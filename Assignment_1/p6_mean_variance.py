import numpy as np

data = np.random.randint(low=0,high=100+1, size=100, dtype=int)

print(type(data))
print(data)

def mean_of_array(arr):
    sum_of_elements = 0
    for element in arr:
        sum_of_elements += element
    return sum_of_elements/arr.size

print("mean", mean_of_array(data))

def varaince_of_arr(arr):
    mean_data = mean_of_array(data)
    sum_of_sq_differences = 0 
    for element in arr:
        sum_of_sq_differences += (element-mean_data)**2
    return sum_of_sq_differences/arr.size

print("variance", varaince_of_arr(data))