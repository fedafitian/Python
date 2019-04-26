from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)

# For Testing:
print(aRandomNumber)

numTries = 0
while True:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	numTries += 1
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
		continue
	else:
		guess = int(guess) # converts a string to an integer

	# Check if correct
	if guess == aRandomNumber:
		print("You got it!")
		break

	# Check if out of tries
	if numTries >= 3: #numTries >= 2
		print("Sorry! You failed.")
		break

	# Give hints
	if(guess > aRandomNumber):
		print("Try a smaller number next time.")
	elif(guess < aRandomNumber):
		print("Try a bigger number next time.")
