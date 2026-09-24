import os
file_path = "File & Exception Handling/test.txt"
if os.path.exists(file_path):
    print(f"the location '{file_path}' exists ")
else:
    print("location does not exists")