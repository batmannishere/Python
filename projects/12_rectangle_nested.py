rows=int(input("Enter number of rows: "))
column=int(input("Enter number of column: "))
symbol=(input("Enter symbol: "))

for x in range(rows):
    for y in range(column):
        print(symbol,end="")
    print()