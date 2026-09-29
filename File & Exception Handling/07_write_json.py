import json
data={"name":"ballu","age":20,"job":"cook"}
file_path=r"C:\Users\Dell\Desktop\output.json"
try:
    with open(file_path,"w") as file: 
       json.dump(data,file,indent=4)         # dump is used to convert the dictionary data into json string 
    print("data has been written")  # we can also indent or add space by adding another parameter after file
except FileExistsError:
    print("this file already exits")