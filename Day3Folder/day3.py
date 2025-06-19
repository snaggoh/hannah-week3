# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task


########################################################################
# Task 1:
# yourname = input("What is your name?")
# print("hello, " + yourname)

# yourage = input("How old are you?")
# newage = int(yourage) + 3 # do math operation
# print("Hey, I am also " + str(newage))
########################################################################
# Task 2:
# name = input("What is your name? ")
# title = input("What is your title?")
# command = input("What is your command to the peasants?")
# print(title  + name  + "commands the peasants to" + command)
########################################################################
# Task 3:
# name = input("What is your name? ")
# pens = input("How many pens would you like to buy?")
# print( name + " bought " + pens + " pens")
########################################################################
# Task 4:
# num1 = input("give me a number: ")
# num2 = input("give me another number: ")
# results = int(num1) + int(num2)
# print("The outcome is " + str(results))
########################################################################
# Task 5:
# answer = input("What do you want ") 
# count = input("How many Ice Cream do you want to buy?")
# price = 1.00
# total =int(count) * int(price)
# print ("Please pay me $" + str(total))
########################################################################
# Task 6:
# num1 = input("How old is grandpa? ")
# num1 = int(num1)
# num2 = input("How old is grandma? ")
# num2 = int(num2)
# if num1 > num2:
#     print("grandpa is older")
# else:
#     print("grandma is older, or same age")


# password = "penguin"
# guess = input("What is the password? ")

# if guess == password:
#     print("Correct!")
# else:
#     print("Password wrong.. Acess Denied!")







########################################################################

# Task 7:)
# for count in range(10):
#     import random
#     random_number = random.randint(1, 100)
#     print(random_number)


########################################################################
# Task 8:
import random
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
answer = num1 + num2
question = "what is " + str(num1) + " + " + str(num2) + "?"
guess = input(question)
if int(guess) == answer:
    print("you are smart! Correct!")
else:
    print("Wrong!")
########################################################################
# Additional exercises: