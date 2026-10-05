import json

file_path=r"C:\Users\Dell\Desktop\output.json"
try:
 with open(file_path,"r") as file:
    content = json.load(file)
    print(content["name"])    # we can access it like dictionary
except FileNotFoundError:
    print("That file was not found")