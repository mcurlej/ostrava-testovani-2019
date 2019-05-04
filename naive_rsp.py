import random



choice = input("Rock, Paper, Scissors?")

print("Human choice: ", choice)

choices = ["rock", "paper", "scissors"]
choice = choice.lower()

pc_choice = random.choice(choices)

print("Computer choice: ", pc_choice)

if pc_choice == choice:
    print("Tie")
elif pc_choice == "rock" and choice == "scissors" \
    or pc_choice == "paper" and choice == "rock" \
        or pc_choice == "scissors" and choice == "paper":
    print("Human lost!")
else:
    print("Human won!")