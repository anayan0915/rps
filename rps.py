import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    choice = input("Your choice: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice! Please choose again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock, Paper, Scissors Game!")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        print(decide_winner(user, computer))

        again = input("\nPlay again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play()
