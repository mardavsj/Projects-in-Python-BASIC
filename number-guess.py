import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
 
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower+1, 2)),"chances to guess the integer!\n")
 
count = 0
 
while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
 
    if x == guess:
        print("Congratulations! You did it.",count, " try")
        break
    elif x > guess:
        print("You guessed small number!")
    elif x < guess:
        print("You guessed high number!")
 
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
