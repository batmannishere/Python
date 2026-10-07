import csv

file_path=r"C:\Users\Dell\Desktop\output.csv"
try:
 with open(file_path,"r") as file:
    content = csv.reader(file)
    for line in content:
      print(line[0])    # we can access column by indexing
except FileNotFoundError:
    print("That file was not found")