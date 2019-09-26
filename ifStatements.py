# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to for")
#     print("Please put an X in the box")
# else:
#     print("Go away come back in {0} years".format(18 - age))

# Guess the number game
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time")
#     print("You are great {0}".format(name))

# More advanced if operator
# And operator if both conditions are true then it's true if not then false
# if (age >= 16) and (age <= 65):
#     print("Have a good day at work")
#
# if 15 < age < 66:
#     print("Have a bad day")

# when both conditions are false then it's false otherwise true
# if age < 16 or age > 65:
#     print("Enjoy your day")
# else:
#     print("Have a good damn day")

# x = "false"
# if x:
#     print("x is true")
#
# This doesn't work , just saying
# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({{}})))

# check if you have entered some text
# x = input("Please enter some text: ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

print(not False)
print(not True)

age = int(input("How old are you"))
if not (age < 18):
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")
if letter not in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")
