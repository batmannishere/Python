# ---------------------------------------------
# WAF to print the length of a list
# (List is the parameter)
# ---------------------------------------------

food = ["apple", "pizza", "burger", "momos"]

def length_calculator(lst):
    print(len(lst))

length_calculator(food)


# ---------------------------------------------
# WAF to print the elements of a list
# in a single line (List is the parameter)
# ---------------------------------------------

movies = ["Inception", "Interstellar", "The Dark Knight", "Avengers", "3 Idiots"]

def element(lst):
    for x in lst:
        print(x, end=" ")

element(movies)


# ---------------------------------------------
# WAF to find the factorial of n
# (n is the parameter)
# ---------------------------------------------

x = int(input("\n\nEnter a number: "))

def factorial(n):
    product = 1

    for i in range(1, n + 1):
        product = product * i

    print(product)

factorial(x)


# ---------------------------------------------
# WAF to convert USD to INR
# ---------------------------------------------

USD = int(input("\nEnter the amount in USD: $"))

def converter(usd):
    INR = usd * 95.53
    print("INR =", INR)

converter(USD)