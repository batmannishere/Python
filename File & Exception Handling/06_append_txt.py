data="I LOVE PIZZA!"
students=["Pulkit","akhil","eklavya"]
file_path=r"C:\Users\Dell\Desktop\output.txt"
try:
    with open(file_path,"a") as file: # a is used to add new data to txt file
        for student in students:
         file.write("\n" +student)    # we can append a new line before adding our data
    print("data has been written")
except FileExistsError:
    print("this file already exits")