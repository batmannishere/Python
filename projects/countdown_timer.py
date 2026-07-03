import time
mytime = int(input("enter time:"))

for x in range(mytime,0,-1):
    seconds = x%60
    minutes = (x//60)%60
    hours=(x//3600)%60
    print(hours, "hours", minutes, "minutes", seconds, "seconds")
    time.sleep(1)


print("TIME's UP")