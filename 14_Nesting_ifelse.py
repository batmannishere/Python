age=int(input("Enter age of driver :"))
if(age>=18):
    if(age>=70):
        print("applicant is eligible for driving but cannot drive due to safety reason")
    else:
        print("applicant is eligible for driving")
else:
    print(" under age of 18 cannot vote ")
