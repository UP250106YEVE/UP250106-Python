import random

def number_guessing_game():
    """A simple number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("🎮 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("📈 Too low! Try again.")
            elif guess > secret_number:
                print("📉 Too high! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} attempts!")
                return
            
            print(f"Attempts remaining: {max_attempts - attempts}\n")
        
        except ValueError:
            print("❌ Please enter a valid number.\n")
    
    print(f"💀 Game Over! The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()