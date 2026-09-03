import time
n=int(input("Enter the end time of stopwatch: "))
for t in reversed(range(1,n+1)):
    second=t%60
    minute=int(t/60)%60
    hour=int(t/3600)%60
    print(f"{hour:02}hours: {minute:02}minutes: {second:02}seconds")
    time.sleep(1)
print("Time's Up")