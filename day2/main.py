import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(options)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "scissors" and computer_choice == "paper") or
    (user_choice == "paper" and computer_choice == "rock")
):
    print("You win! 🎉")
else:
    print("You lose! 😢")
