import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

#array[start:end:step]
#print row
print(array[0])
print()
#print want to more than one row
print(array[0:3:1])
print()
#column with row
print(array[:,0:]) # leaving meaning in python start from 0 and go till end
