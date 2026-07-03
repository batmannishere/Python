'''
FUNCTIONS
Block of statements that performs a specific task
There are two types of function
1)BUILT-IN       2) USER DEFINED
SYNTAX

def nameoffunction(param1,param2):
    some work
nameoffunction(arg1,arg2)

'''
def sum(a,b):
    s=a+b
    return s
summ=sum(2,3)
print(summ)
#WAF TO PRINT AVG OF THREE NO
n1=float(input("Enter the number 1:"))
n2=float(input("Enter the number 2:"))
n3=float(input("Enter the number 3:"))

def calc_avg(a,b,c):
    avge= (a+b+c)/3
    return avge
average =calc_avg(n1,n2,n3)
print(average)