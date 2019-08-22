# Problem 1:
# Create a program that prints the user input until they enter 'q' to quit.

 while 0 == 0: # this is not how to use a while loop
    user = input("Enter Something: ")
    if user == "q":
        break
    else:
        print(user)

# Problem 2:
# Ask the user for their name.
# Then ask the user for a number of times they want their name printed.
# Print the number of times the user want their name printed.
# If they enter a negative or zero, tell them to ask again.

user = input(" What is your name? ")
while 0==0:
    user1 = int(input("How many time you want to print it? "))
    if user1 <= 0:
        print("INVALID ANSWER")
    elif user1 >=1:
        ren = user * user1
        print(ren)
        break
    else:
        print("INVALID ANSWER")


# Problem 3:
# Create a program that takes user input in a while loop.
# If they enter 1, print 1. If they enter 2, print 2.
# If they enter 3 print 3. If they enter ‘q’ or 0 (your choice), quit.
# Else, print “ERROR”.


while 0 == 0: # this is not how to use a while loop
    user = input("Enter 1, 2, 3,\n or 'q' to quit\n")
    if user == "q":
        break
    elif user == "1":
        print(1)
    elif user == "2":
        print(2)
    elif user == "3":
        print(3)
    else:
        print("ERROR")

#
# Problem 4:
# Create a program that takes the user input until they enter 'q'.
# You should store all of their input and separate the input with a comma.
# Once they enter 'q', print all of the comma separated words they entered.

# for some reason this loop doesn't run
total = "0"
while 0 == 0: # this is not how to use a while loop
    user = input("Enter a word\n")
    if user != "q":
        total = total + ", "+user
    elif user == "q":
        print(total)
        break
