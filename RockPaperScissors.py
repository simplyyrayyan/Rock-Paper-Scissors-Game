import random
import time
import sys

# Functions

def ask_to_continue(message):
    message1 = input(message).lower().strip()
    if message1 == "quit":
        time.sleep(0.5)
        print("Thanks for Playing hope to see you again!")
        sys.exit()
    if message1 == "play":
        time.sleep(0.5)
        return True
    else:
        time.sleep(0.3)
        print("Invalid Input, Please Try Again")
        return True 

# Most Varibles

answerlist = ["I Choose Rock", "I Choose Paper", "I Choose Scissors"]
tie_message = "It's a Tie! Try Again!, To Quit the Game Type Quit, To Play Again type Play: "
win_message = "Congratulations! You Win!, To Quit the Game Type Quit, To Play Again type Play: "
lose_message = "Sorry! You Lose! Better Luck Next Time!, To Quit the Game Type Quit, To Play Again type Play: "

# Greeting
print("Welcome to Rock Paper Scissors Game!")
time.sleep(1)

while True:
    print("Please choose one of the follwing options:")
    time.sleep(1)
    print("1. Rock")
    time.sleep(1)
    print("2. Paper")
    time.sleep(1)
    print("3. Scissors")
    time.sleep(1)

    try:
        user_input = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue

    # If user Chooses Rock (1)
    if user_input == 1: 
        print("You Chose Rock")
        time.sleep(0.5)
        computer_choice = random.choice(answerlist)
        print(computer_choice)

        # User Ties if Computer Chooses Rock
        if computer_choice == 'I Choose Rock':
            time.sleep(1)
            ask_to_continue(tie_message)
        
        # User Wins if Computer Chooses Scissors
        elif computer_choice == 'I Choose Scissors':
            time.sleep(1)
            ask_to_continue(win_message)
        
        # User Loses if Computer Chooses Paper
        elif computer_choice == 'I Choose Paper':
            time.sleep(1)
            ask_to_continue(lose_message)
    
    # If user Chooses Paper (2)
    if user_input == 2: 
        print("You Chose Paper")
        time.sleep(0.5)
        computer_choice = random.choice(answerlist)
        print(computer_choice)

        # User Ties if Computer Chooses Rock
        if computer_choice == 'I Choose Rock':
            time.sleep(1)
            ask_to_continue(win_message)
        
        # User Wins if Computer Chooses Scissors
        elif computer_choice == 'I Choose Scissors':
            time.sleep(1)
            ask_to_continue(lose_message)
        
        # User Loses if Computer Chooses Paper
        elif computer_choice == 'I Choose Paper':
            time.sleep(1)
            ask_to_continue(tie_message)


    # If user Chooses Scissors (3)
    if user_input == 3: 
        print("You Chose Scissors")
        time.sleep(0.5)
        computer_choice = random.choice(answerlist)
        print(computer_choice)

        # User Ties if Computer Chooses Rock
        if computer_choice == 'I Choose Rock':
            time.sleep(1)
            ask_to_continue(lose_message)
        
        # User Wins if Computer Chooses Scissors
        elif computer_choice == 'I Choose Scissors':
            time.sleep(1)
            ask_to_continue(tie_message)
        
        # User Loses if Computer Chooses Paper
        elif computer_choice == 'I Choose Paper':
            time.sleep(1)
            ask_to_continue(win_message)
