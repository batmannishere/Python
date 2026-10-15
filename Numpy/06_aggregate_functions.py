import numpy as np
array=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# to get sum of array
print(np.sum(array))
print()
# to get the mean 
print(np.mean(array))
print()
# to get the standard deviation
print(np.std(array))
print()
# to get the variance
print(np.var(array))
print()
# to get the min value in the array
print(np.min(array))
print()
# to get the max value in the array
print(np.max(array))
print()
# to get the index min value in the array
print(np.argmin(array))
print()
# to get the index max value in the array
print(np.argmax(array))
print()
# if we want to get the sum of the columns
print(np.sum(array,axis=0))
print()
# if we want to get the sum of the row
print(np.sum(array,axis=1))
print()