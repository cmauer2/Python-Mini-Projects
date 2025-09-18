import random


def get_valid_word():
    words = ["python", "algorithm", "project", "gaming", "hangman", "java", "program"]
    return random.choice(words).upper()


def display_hangman(tries):
    stages = [
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   / \\
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   / 
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |    
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |    |
        |    
        -
        """,
        """
        ------
        |    |
        |    O
        |    |
        |    |
        |    
        -
        """,
        """
        ------
        |    |
        |    O
        |    
        |    
        |    
        -
        """,
        """
        ------
        |    |
        |    
        |    
        |    
        |    
        -
        """
    ]
    return stages[tries]


def get_player_input(prompt):
    while True:
        user_input = input(prompt).upper()
        if user_input.isalpha() and len(user_input) == 1:
            return user_input
        print("Invalid input. Please enter a single letter.")


def play():
    word = get_valid_word()
    word_complete = "_" * len(word)
    guessed_letters = []
    tries = 6

    print("Let's Play Hangman!\n")

    while tries > 0:
        print(f"{display_hangman(tries)}\n{word_complete}\n")

        guess = get_player_input("Guess a letter: ")

        if guess in guessed_letters:
            print(f"Incorrect! You've already guessed {guess}")
        else:
            guessed_letters.append(guess)
            if guess not in word:
                tries -= 1
                print(f"{guess} is not in the word.")
            else:
                word_complete = "".join(
                    [letter if letter == guess or revealed.isalpha() else '_' for letter, revealed in
                     zip(word, word_complete)])
                if "_" not in word_complete:
                    print("Congratulations, you've won!")
                    return

    print(
        f"Unfortunately you have run out of tries. The word was {word}. Thank you for playing, better luck next time!")


def main():
    play_again = "y"
    while play_again == "y":
        play()
        play_again = input("Play again? (y/n): ").strip().lower()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
