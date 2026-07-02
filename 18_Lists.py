'''
LISTS
A built in data type that stores set of values
It can store elements of different data types(integers,float,string)
SYNTAX
nameoflist=["element1",23,43.55]
'''
marks=[94,54,33,45,29]
print(marks[0])
marks[0]=66
print(marks[0]) # we can mutitate lists unlike in strings
print(marks)
'''
LIST SLICING
similar to strings
list name=[st index:end index]
'''
'''
LIST METHODS
1)listname.append(x): Adds an element to the end of a list. 
2)listname.extend(iterable): Adds all items from an iterable to the end.
3)listname.insert(i, x): Inserts an element at a specific index.
4)listname.remove(x): Removes the first occurrence of a value.
5)listname.pop([i]): Removes and returns an element at a given index (or the last one).
6)listname.sort(): Sorts the list in place (ascending). 
7)listname.reverse(): Reverses the order of elements in the list.
8)listname.count(x): Returns the number of times a value appears.
9)listname.sort(reverse=True): Sorts the list in place descending). 

'''
