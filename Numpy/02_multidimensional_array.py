import numpy as np

array1=np.array(['A'])      # 0 dimensional array it only has 1 element
array2=np.array(['A','B','C']) # 1 dimensional array it has 1 row  
array3=np.array([['A','B','C'],  # 2 dimensional array it has rows and coloum
                ['D','E','F'],
                ['G','H','I']])

array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']], # 3 dimensional it has layers,rows and column
                [['J','K','L'],['M','N','O'],['P','Q','R']],
                [['S','T','U'],['V','W','X'],['Y','Z','-']]])

print(array[0][0][0]) # this is called chain indexing 

print(array[0,0,0]) # this is called multidimensional indexing it is faster than chain indexing 
                    # here first comes layer,rows,column

# write a word multidimensional indexing in 3d array

word= array[0,0,1]+array[0,0,0]+array[2,0,0]+array[1,0,1]+array[0,1,1]+array[2,0,1]+array[0,0,1]+array[0,0,0]+array[1,0,2]+array[1,0,2]# BASKETBALL
print(word)