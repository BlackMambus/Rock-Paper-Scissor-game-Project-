import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    while choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    return choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(f"\nResult: {result}")

if __name__ == "__main__":
    play_game()

