import random

choices = ["rock", "paper", "scissors"]

def is_valid_choice(choice):
    if choice in choices:
        return True

    return False

def random_choice():
    return random.choice(choices)

def get_game_results(choice, pc_choice):
    if pc_choice == choice:
        return 0
    elif pc_choice == "rock" and choice == "scissors" \
        or pc_choice == "paper" and choice == "rock" \
            or pc_choice == "scissors" and choice == "paper":
        return -1
    else:
        return 1