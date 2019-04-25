import random

options = ['rock', 'paper', 'scissors']

#Computer Choice
computer_choice = random.choice(options) #assign variable to random

#User Input
print "Let's start our match!"
user_choice = raw_input("Do you choose rock, paper, or scissors? : ")
user_choice = user_choice.lower() #this converts whatever the user types into all lowercase

#User Choice
if user_choice == 'rock' or 'paper'or 'scissors':
    user_choice = user_choice.lower()
    print "The computer has drawm %s whilst you have drawn %s" % (computer_choice, user_choice)

if user_choice != 'rock' or 'paper' or 'scissors':
    print("Sorry, please try again")
    user_choice = raw_input("Do you choose rock, paper, or scissors? : ")
    user_choice = user_choice.lower()


#Rock Choice
if user_choice == 'rock':
    if computer_choice == 'rock':
        print "It's a tie."
    elif computer_choice == 'paper':
        print "You lose!"
    else:
        print "You win!!"

#Paper Choice
if user_choice == 'paper':
    if computer_choice == 'rock':
        print "You win!!"
    elif computer_choice == 'paper':
        print "It's a tie."
    else:
        print "You lose!"

#Scissors Choice
if user_choice == 'scissors':
    if computer_choice == 'rock:':
        print "You lose!"
    elif computer_choice == 'paper':
        print "You win!!"
    else:
        print "It's a tie."