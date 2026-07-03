'''
LOOPS
Loops are used to repeat instructions
WHILE LOOPS
A while loop is a control flow statement that executes a block of code repeatedly as long as a specified condition evaluates to true.
SYNTAX
while condition:
    #some work

'''
#PRINT THE NUMBERS FROM n TO 100
n=int(input("Enter the number u want to start counting from:"))

while n<=100:
    print(n)
    n=n+1
#PRINT THE NUMBERS FROM 100 TO n
n=int(input("Enter the number u want to start reverse counting:"))

while (n>=0):
    print(n)
    n=n-1
# PRINT THE MULTIPLICATION TABLE OF A NUMBER N
    n=int(input("Enter the number:"))
    x =int(input("Table till:"))
    i=1
    while i<=x:
     table=n*i
     i=i+1
     print(table)
#PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP
nums[1,4,9,16,25,36,49,64,81,100]
i=0
while(i<len(nums)):
    print(nums[i])
    i=i+1
