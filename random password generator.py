import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special):
    """Generate a random password based on the user's criteria."""
    
    # Define the pools of characters to choose from
    character_pool = ""
    
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_numbers:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation
    
    if not character_pool:
        return "You must select at least one character type!"
    
    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

def get_user_input():
    """Collect user inputs for password requirements."""
    
    length = int(input("Enter the desired password length: "))
    
    print("Choose the types of characters to include in your password:")
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    return length, include_uppercase, include_lowercase, include_numbers, include_special

def main():
    """Main function to run the password generator."""
    print("Welcome to the Random Password Generator!")
    
    while True:
        # Get user input
        length, include_uppercase, include_lowercase, include_numbers, include_special = get_user_input()
        
        # Generate the password
        password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)
        
        # Display the result
        print(f"Generated Password: {password}")
        
        # Ask if the user wants to generate another password
        again = input("Do you want to generate another password? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the Password Generator!")
            break

# Run the program
main()
