import random

# ===== Guessing Game Part =====
LOW = 1
HIGH = 100
MAX_ATTEMPTS = 7
best_score = 0

def play_one_game():
    global best_score
    secret_number = random.randint(LOW, HIGH)
    attempts_used = 0
    print(f"\n--- New Game! Guess between {LOW} and {HIGH} ---")

    while attempts_used < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts_used+1}/{MAX_ATTEMPTS} - Enter guess: "))
            attempts_used += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! In {attempts_used} attempts!")
                score = 100 - (attempts_used - 1) * 10
                print(f"Your Score: {score}")
                if score > best_score:
                    best_score = score
                    print(f"NEW Best Score: {best_score}")
                else:
                    print(f"Best Score: {best_score}")
                return
        except ValueError:
            print("Invalid! Enter whole number.")

    print(f"\nOut of attempts! Number was {secret_number}")
    print(f"Score: 0 | Best Score: {best_score}")

def guessing_game_menu():
    while True:
        play_one_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print(f"Final Best Score: {best_score}.")
            break

# ===== Word Counter Part =====
def word_counter():
    print("\n--- Word Counter ---")
    text = input("Enter a sentence / paragraph: ").strip()

    if not text:
        print("No input! Please type something.")
        return

    # Step 6 - Clean and split
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    char_no_space = len(text.replace(" ", ""))

    # Step 7 - Analysis
    longest_word = max(words, key=len) if words else ""
    
    print(f"\nResults:")
    print(f"Words: {word_count}")
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (no spaces): {char_no_space}")
    print(f"Longest word: '{longest_word}' ({len(longest_word)} letters)")

# ===== MAIN MENU =====
while True:
    print("\n===== MAIN MENU =====")
    print("1. Play Guessing Game")
    print("2. Word Counter")
    print("3. Exit")
    choice = input("Choose 1/2/3: ").strip()

    if choice == "1":
        guessing_game_menu()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice! Enter 1, 2 or 3.")
