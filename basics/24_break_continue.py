''' 
break and continue are control flow statements used to alter the execution of loops (for and while).  
The break statement immediately terminates the entire loop and transfers control to the code following 
the loop.In contrast, the continue statement skips the remainder of the current iteration and jumps 
directly to the next iteration of the loop
'''
 #WAP to print all odd number till 100 using break and contiue 
i = 0

while i <= 100:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1