import json
data={"name":"ballu","age":20,"job":"cook"}
data2={"name":"sallu","age":21,"job":"cook"}
file_path=r"C:\Users\Dell\Desktop\output.json"
try:
    with open(file_path,"x") as file: 
       json.dump(data2,file,indent=4)        
    print("data has been written")  
except FileExistsError:
    print("this file already exits")