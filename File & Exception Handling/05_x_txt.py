data="I LOVE PIZZA"
file_path=r"C:\Users\Dell\Desktop\output.txt"
try:
    with open(file_path,"x") as file: # x is also used to write but the file should not be made earlier or it would give error
     file.write(data)    
     print("data has been written")
except FileExistsError:
    print("this file already exits")