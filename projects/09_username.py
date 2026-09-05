username=input("Enter your username: ")
if username.isdigit() or username.find(" ") != -1 or len(username)>12:
    print(f"{username} is invalid")
else:
    print(f"Welcome {username}")