file_path=r"C:\Users\Dell\Desktop\test1.txt"
try:
 with open(file_path,"r") as file:
    content = file.read()
    print(content)
except FileNotFoundError:
    print("That file was not found")