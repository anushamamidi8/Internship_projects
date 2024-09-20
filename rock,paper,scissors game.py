import random

def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Rules of the game
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    
    return "Computer wins!"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get user choice
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue
        
        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = get_winner(user_choice, computer_choice)
        print(result)
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Start the game
play_game()
