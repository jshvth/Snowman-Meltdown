import random
from ascii_art import STAGES

# List of possible secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum allowed mistakes before game over
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Returns a randomly chosen word from the WORDS list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Prints the current state of the snowman and the word.

    Parameters:
        mistakes (int): Number of incorrect guesses so far.
        secret_word (str): The word the player is trying to guess.
        guessed_letters (list): Letters the player has guessed.
    """
    print(STAGES[mistakes])

    # Build and print the word with guessed letters and underscores
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Guessed Letters:", " ".join(sorted(guessed_letters)))
    print()


def play_game():
    """
    Runs the main game loop: handles user input, game logic,
    win/loss conditions, and displays the game state.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        # Update game state based on guess
        if guess not in secret_word:
            print(f"Oops! '{guess}' is not in the word.")
            mistakes += 1
        else:
            print(f"Good job! '{guess}' is in the word.")

        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 You saved the snowman! You win!")
            break
    else:
        # Loss condition
        display_game_state(mistakes, secret_word, guessed_letters)
        print(f"💧 The snowman melted... The word was '{secret_word}'. Better luck next time!")


if __name__ == "__main__":
    play_game()