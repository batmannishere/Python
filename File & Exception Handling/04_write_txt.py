data="I LOVE PIZZA!"
file_path=r"C:\Users\Dell\Desktop\output.txt"
try:
    with open(file_path,"w") as file: # w is used to overwrite txt file
     file.write(data)    
     print("data has been written")
except FileExistsError:
    print("this file already exits")