#INDEXING
# we can only access the element that are already provided in string we cannot change it after defining it
str="Hello World"
print(str[3]) # we cannot do str[3]="f"
#SLICING
#Accessing parts of a string
#nameofstring[starting index:ending index](and starting index is counted not the end one)
#if we leave the starting index empty it takes it as 0 and for ending the len(name of string)
print(str[1:4])
print(str[:4])
print(str[1:])