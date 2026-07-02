'''
DICTIONARY
Dictionaries are used to store data values in key:values pairs
they are unordered, mutable(Changeable)and dont't allow duplicates key
SYNTAX
nameofdic={"key":"value","key":"value","key":"value"}
acesses nameofdic["key"]="value" or nameofdic.get["key"]
NESTED DICTIONARY

'''

student ={
  "name":"pulkit",
"score":{
   "chem":34,
   "phy":45,
   "math":45,
}
}
print(student["score"]["phy"])
'''
DICTIONARY METHODS
clear(): Removes all elements from the dictionary. 
copy(): Returns a shallow copy of the dictionary. 
fromkeys(seq, value): Creates a new dictionary with keys from seq and values set to value. 
get(key, default): Returns the value for key if it exists; otherwise returns default (or None). 
items(): Returns a view object of all key-value pairs as tuples. 
keys(): Returns a view object of all keys in the dictionary. 
values(): Returns a view object of all values in the dictionary. 
update(other): Updates the dictionary with elements from another dictionary or iterable.
pop(key, default): Removes the specified key and returns its value; raises KeyError if key is missing (unless default is provided). 
popitem(): Removes and returns the last inserted key-value pair as a tuple. 
setdefault(key, default): Returns the value for key if it exists; if not, inserts key with default value and returns it.
'''