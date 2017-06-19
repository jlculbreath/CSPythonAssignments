# Jeremy Culbreath
# CS490-001
# Assignments due 06-15-2017


# odd or even program
print ("\n\nThis program determines if a number is odd or even.")   #program info

userInput = input ("Enter a number: ")  #user input
num = int(userInput)                    #convert to integer

if (num%2==0): print (num, " is an even number.")       #output if number is even
else: print (num, "is an odd number.")                  #output if number is odd


# rectangle perimeter and area
print ("\n\nThis program give the area and perimeter of a rectangle given a height and width.") #program info

userInput = input("Enter height of rectangle: ")    #user input height
height= int(userInput)                              #convert to integer
userInput = input("Enter wideth of rectangle: ")    #user input width
width = int(userInput)                              #convert to integer

area = height*width                                 #calculation of area
perimeter = 2*(height+width)                        #calculation of perimter

print ("The area of a rectangle of height ", height, " and width ", width, " is ", area, ".")   #output area
print ("The perimeter of a rectangle of height ", height, " and width ", width, " is ", perimeter, ".") #output perimeter


# random number guessing
print ("\n\nThis program tries to get the user to match a random number.")  #program info

import random                       #to use random number generation
rand = random.randint(0, 9)         #generate random number 0 to 9

while (True):                       #repeat loop until user guesses correct number
    userInput = input("Guess a number (0-9): ")         #user input guess
    guess = int(userInput)                              #convert to int
    if (rand < guess):
        print ("Sorry, your guess was too high. Try again.") #output if guess is high
        continue                    #skip rest of loop
    if (rand > guess):
        print ("Sorry, your guess was too low. Try again.")  #output if guess is low
        continue                    #skip rest of loop
    if (rand == guess):
        print ("You are correct! The number was ", guess, ".")             #output if guess is correct
        break                       #break loop if guess is correct


#final output
print ("\n\nAll three programs are finished. Thank you!")
print ("Written by: Jeremy Culbreath")