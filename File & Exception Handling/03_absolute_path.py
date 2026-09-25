import os
file_path = "C:/Users/Dell/Desktop/test1.txt"
if os.path.exists(file_path):
    print(f"the location '{file_path}' exists ")
else:
    print("location does not exists")

