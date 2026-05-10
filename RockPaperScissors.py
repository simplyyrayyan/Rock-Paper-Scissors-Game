# Rock Paper Scissors Game Program 
import random
import time
import sys
from slow_printing import slow_print
from slow_printing import slow_input
# Message: Add Scores and Round system

# Most Varibles

answerlist = ["I Choose Rock", "I Choose Paper", "I Choose Scissors"]
tie_message = "It's a Tie! Try Again!, (QUIT) or (PLAY): "
win_message = "Congratulations! You Win!, (QUIT) or (PLAY): "
lose_message = "Sorry! You Lose! Better Luck Next Time!, (QUIT) or (PLAY): "

# Functions

# Ask to Continue Function
def ask_to_continue(message):
    message1 = input(message).lower().strip()
    if message1 == "quit":
        slow_print("Thanks for Playing hope to see you again!")
        sys.exit()
    if message1 == "play":
        return True
    else:
        slow_print("Invalid Input, Please Try Again")
        return True 
# The Game Logic
def game_logic(option_message, objective_message1, objective_message2, objective_message3):
        # Must print user choice
        slow_print(option_message)
        computer_choice = random.choice(answerlist)
        slow_print(computer_choice)

        # Computer Chooses Rock
        if computer_choice == 'I Choose Rock':
            ask_to_continue(objective_message1)
        
        # Computer Chooses Paper
        elif computer_choice == 'I Choose Paper':
            ask_to_continue(objective_message2)
        
        # Computer Chooses Scissors
        elif computer_choice == 'I Choose Scissors':
            ask_to_continue(objective_message3)

# Greeting
slow_print("Welcome to Rock Paper Scissors Game!")
time.sleep(1)

# Main Loop

# User Chooses Rock Paper or Scissors
while True:
    slow_print("Please choose one of the follwing options:")
    slow_print("1. Rock")
    slow_print("2. Paper")
    slow_print("3. Scissors")
    
    # Validation
    try:
        user_input = slow_input("Enter your choice (1-3): ")
    except ValueError:
        slow_print("Invalid input. Please enter a number between 1 and 3.")
        continue
    except TypeError:
        slow_print("Invalid input. Please enter a number between 1 and 3.")
        continue

    # If user Chooses Rock (1)
    if user_input in ["1", "rock", "Rock", "ROCK"]:
        # For Rock 
        game_logic("You Chose Rock", tie_message, lose_message, win_message)

    # If user Chooses Paper (2)
    elif user_input in ["2", "paper", "Paper", "PAPER"]:
        # For Paper
        game_logic("You Chose Paper", win_message, tie_message, lose_message)
        
    # If user Chooses Scissors (3)
    elif user_input in ["3", "scissors", "Scissors", "SCISSORS"]:
        # For Scissors
        game_logic("You Chose Scissors", lose_message, win_message, tie_message)
# Code Ends
