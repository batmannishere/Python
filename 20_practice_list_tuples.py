# WAP TO ASK THE USER TO ENTER NAMES OF THIER 3 FAV MOVIES AND SOTRE THEM IN A LIST
mov1=input("ENTER YOUR FAVOURITE MOVIE:")
mov2=input("ENTER YOUR FAVOURITE MOVIE:")
mov3=input("ENTER YOUR FAVOURITE MOVIE:")
movies=[]
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#WAP TO CHECK IF A LIST CONTAIN A PALINDROME OF ELEMENTS
el1=input("ENTER YOUR element1:")
el2=input("ENTER YOUR element2:")
el3=input("ENTER YOUR element3:")
list=[]
list.append(el1)
list.append(el2)
list.append(el3)
list2=list.copy()
list2.reverse()
if(list==list2):
    print("is plaindrome")
else:
     print("is not plaindrome")
#WAP TO COUNT THE NUMBER OF STUDENTS WITH THE"A"grade in the following tuple
#["C","D","A","A","B","B","A"]
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
