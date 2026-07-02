# String is a data type that stores a sequence of characters
# if we want to make two string in different lines we use /n
str1="this is a string./nwe are creating it in python."
#if we want to give gap we use /t
str2="this is a string./twe are creating it in python."
# some operation of string
# 1)Concatenation(add two strings)
str3="hello"
str4="world"
finalstr = str3+str4
print(finalstr)
# 2)lenght of a string
print(len(finalstr))
# 3)capitalize(capitalize first letter of string)
print(finalstr.capitalize())
# 4)Upper( make all in capital)
print(finalstr.upper())
# 5)Lower(make all in lower)
print(finalstr.lower())
# 6)isupper(checks if all the letter are upper case acc to it gives true or false)
print(finalstr.isupper())
# 7)islower(checks if all the letter are lower case acc to it gives true or false)
print(finalstr.islower())
# 8)count(occurrences of a given letter)
print(finalstr.count("l"))
# 9)find(the index of first occurence adn other occurence too if we want to know that occ put comma and that occ)
print(finalstr.find("l"))
print(finalstr.find("l",2))
# 10) startswith and 11)endswith
print(finalstr.startswith("l"))
print(finalstr.endswith("l"))
#12)replace(replace thing with that letter or string )
print(finalstr.replace("world","Pulkit"))
#13)split(split the string acc to input)
print(finalstr.split("l"))

