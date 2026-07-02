'''
SET
Set is the collection of the unordered items 
each element in the set must be unique and immutable
imp- set is mutable but not the elements
SYNTAX
nameofset={1,2,3,4,}
nullset=set()
SET METHODS
add(element): Adds a single element to the set. 
update(*iterables): Adds elements from one or more iterables (lists, tuples, etc.) to the set. 
clear(): Removes all elements from the set, leaving it empty. 
pop(): Removes and returns an arbitrary element; raises a KeyError if the set is empty. 
remove(element): Removes a specific element; raises a KeyError if the element is not present. 
discard(element): Removes a specific element if present; does nothing if the element is missing. 
difference_update(*iterables): Removes elements found in the specified iterables from the set. 
intersection_update(*iterables): Keeps only elements found in both the set and the specified iterables. 
symmetric_difference_update(other): Updates the set to keep only elements found in either the set or the other, but not both. 
Set Operation Methods These methods return a new set without modifying the original:

union(*iterables): Returns a new set containing all unique elements from the set and iterables. 
intersection(*iterables): Returns a new set containing elements common to the set and iterables. 
difference(*iterables): Returns a new set with elements in the set but not in the iterables. 
symmetric_difference(other): Returns a new set with elements in either the set or the other, but not both. 
copy(): Returns a shallow copy of the set.
Relationship Methods These methods return boolean values (True/False) to compare sets:

isdisjoint(other): Returns True if the set has no elements in common with the other. 
issubset(other): Returns True if all elements of the set are in the other. 
issuperset(other): Returns True if all elements of the other are in the set.
'''