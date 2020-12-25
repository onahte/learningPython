# This program tests the length of the input (name) for min and max legnth.

name = input("What is your name: ")
if len(name) < 3:
    print("Please enter a name that is at least 3 characters in length.")
elif len(name) > 50:
    print("Please enter a nmae that is shorter than 50 characters in length.")
else:
    print("Name looks good!")