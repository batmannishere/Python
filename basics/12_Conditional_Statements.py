''' 
we generally use three:
1)if(if a condtion is in this it will run this condition always)
2)elif(in this if a condtion is not done by if then it will execute)
3)else(if not is excuted then else will be excuted)
SYNTAX
if(condition):
  statement 1 
elif(condition):
  statement 2
else:
  statement 3
  '''
age=int(input("Enter age of voter applicant:"))
if(age>=18):
    print("applicant is eligible for voting")
else:
    print(" under age of 18 cannot vote ")
