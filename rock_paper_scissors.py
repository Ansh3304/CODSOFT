import random

def get_user_choice():
    print("\nChoose one: Rock, Paper, or Scissors")
    choice = input("Your choice: ").strip().lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please type Rock, Paper, or Scissors.")
        choice = input("Your choice: ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \         (user == "scissors" and computer == "paper") or \         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def display_result(user, computer, result):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if result == "tie":
        print("Result: It's a Tie!")
    elif result == "win":
        print("Result: You Win! 🎉")
    else:
        print("Result: You Lose! 😢")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game! 🎮")
    
    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScore ➤ You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        while play_again not in ['yes', 'no']:
            play_again = input("Please type 'yes' or 'no': ").strip().lower()
        if play_again == 'no':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 You are the overall winner!")
            elif user_score < computer_score:
                print("💻 Computer wins this time!")
            else:
                print("🤝 It's a tie overall!")
            break
        round_number += 1

# Start the game
if __name__ == "__main__":
    play_game()
