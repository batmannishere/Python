#RECURSION-when a function calls itself repeatedly.
#print n to 1 backwards

n=int(input("Enter the number:"))
def count(x):
    if x==0: # base case(when it has to stop)
        return 
    print(x) # calling fucntion again 
    count(x-1)
count(n)
# CALL STACK- when u call a fucntion again and again after last case u start printing
#In call stack something is printed after call
n=int(input("Enter the number:"))
def count(x):
    if x==0: # base case(when it has to stop)
        return 
    count(x-1)
    print(x)
count(n)