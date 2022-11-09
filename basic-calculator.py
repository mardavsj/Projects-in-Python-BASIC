def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

(print("Options available: add,subtract,multiply,divide"))
choice=(input("Select any one option from above: "))

if choice in ("add","subtract","multiply","divide"):
    m=float(input("Enter the 1st number:"))
    n=float(input("Enter the 2nd number:"))

if choice == "add":
    print(add(m,n))
elif choice == "subtract":
    print(subtract(m,n))
elif choice == "multiply":
    print(multiply(m,n))
elif choice == "divide":
    print(divide(m,n))
else:
    print("WARNING: Invalid")
