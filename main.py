import random
from collections import Counter
import os

# ===== CONFIG =====
LOW = 1
HIGH = 100
MAX_ATTEMPTS = 7
best_score = 0

# ===== GUESSING GAME =====
def play_guessing_game():
    global best_score
    secret = random.randint(LOW, HIGH)
    attempts = 0
    print(f"\n--- New Game! Guess between {LOW} and {HIGH} ---")

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts+1}/{MAX_ATTEMPTS} - Enter guess: "))
            attempts += 1

            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")
            else:
                print(f"Correct! You guessed in {attempts} attempts!")
                score = 100 - (attempts - 1) * 10
                print(f"Your Score: {score}")
                if score > best_score:
                    best_score = score
                print(f"Best Score: {best_score}")
                return
        except ValueError:
            print("Invalid! Enter whole number only.")

    print(f"\nOut of attempts! The number was {secret}")
    print(f"Best Score: {best_score}")

# ===== WORD COUNTER - FILE BASED =====
def word_counter():
    print("\n--- File-based Word Counter ---")
    
    # Create a sample file if not exists
    if not os.path.exists("sample.txt"):
        with open("sample.txt", "w") as f:
            f.write("Hello world hello python world. This is a sample text file for word counter project. Python is fun and python is easy.")

    file_name = input("Enter file name (press Enter for sample.txt): ").strip()
    if file_name == "":
        file_name = "sample.txt"

    try:
        with open(file_name, "r") as file:
            text = file.read().lower()
            
            # Basic string manipulation
            words = text.split()
            # Clean punctuation for frequency
            clean_words = [w.strip(".,!?;:\"'()[]") for w in words]
            
            total_words = len(words)
            word_freq = Counter(clean_words)

            print(f"\nFile '{file_name}' read successfully!")
            print(f"Total words: {total_words}")
            print(f"Unique words: {len(word_freq)}")
            print("\nWord Frequency:")
            for word, count in word_freq.most_common():
                print(f"  {word}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")

# ===== MAIN MENU =====
while True:
    print("\n===== PROJECT 02 MAIN MENU =====")
    print("1. Number Guessing Game")
    print("2. Word Counter (File Based)")
    print("3. Exit")
    choice = input("Choose 1/2/3: ")

    if choice == "1":
        while True:
            play_guessing_game()
            again = input("Play again? (y/n): ").lower()
            if again != 'y':
                break
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Bye! Project Complete.")
        break
    else:
        print("Invalid choice!")
