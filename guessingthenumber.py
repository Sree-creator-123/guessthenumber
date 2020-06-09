# Importing the random library
import random

# Creating a list called numbers with numbers from 1-20
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Asking the computer to select a random number from the list numbers
random_comp = random.choice(numbers)

# Asking the user what's your name
name = input("What's your name? ")

# Taking the user's input from above and printing hello with the user's name
print("Hello " + name)

# Asking the user to pick a number
person = int(input("Pick any number: "))

# Creating a while loop and breaks when the person inputs exit
while person != "exit":
    
    # If the user's input is higher than the number the number the computer selected, it tells the user that the number you inputted is too high
    if (person > random_comp):
        print("Too high")

    # If the user's input is lower than the number the number the computer selected, it tells the user that the number you inputted is too low
    if (person < random_comp):
        print("Too low")

    # If the user's input is the same as the number the computer selected, it tells the user that the number you inputted is just right
    if (person == random_comp):
        print("just right")
        # After the user got the number, the code breaks because after you find the answer, the computer doesn't generage a new number, so you break it so that if you rin it again, it will create a new number
        break
    
    # Repeats until it goes to the if statement above
    person = int(input("Pick any number: "))