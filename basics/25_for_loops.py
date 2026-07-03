'''
SYNTAX
for iterator in list:
    #some work
for iterator in range(starts,stops,increament)

'''
nums=[1,2,3,4,5,6,7,8]

for val in nums:
    print(val)
    #OR
#RANGE- Range func returns a seq of no. , st from 0 by default, increments by 1 by defaults , stops before a specified number
for val in range(len(nums)):
   print(val)

#PRINT THE ELEMENT OF THE FOLLOWING LIST USING A LOOP
#[1,4,9,16,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]

for el in num:
    print(el,end=" ")

#WAP TO FIND THE SUM OF FIRST N NUMBERS
n=int(input("Enter the number:"))
sum=0
for n in range(n):
    sum=sum+n
print(sum)
