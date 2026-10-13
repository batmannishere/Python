import numpy as np

array=np.array([1,2,3,4])
# operation on whole array
print(array+1)
print(array-1)
print(array*1)
print(array/2)
print(array**1)
#vectoriszed math function
np.sqrt(array)
np.round(array)
np.floor(array)
np.ceil(array)
np.pi
#element wise btw two array
array1=np.array([2,4,6,8])
array2=np.array([1,2,3,4])
print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

#comparison
scores=np.array([95,60,32,45,66,10,12,43])

scores[scores<=30]=0
print(scores)
   
