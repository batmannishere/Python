# Python writing files (.txt, .json, .csv)

import json
import csv

employees = [["Name", "Age", "Job"],             #DOUBLE LIST(2D LIST)
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = r"C:\Users\Dell\Desktop\output.csv"

try:
    with open(file_path, "w", newline="") as file: # the system automat. assign a new line character with space so to remove it we give paramter
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)  # writerow is method 
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")