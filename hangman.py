import random
import os
from hangman_words import word_list
from hangman_art import logo, stages


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')


def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'


while True:
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6
    display = ["_" for _ in range(word_length)]

    print(logo)

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear_screen()  # Clear the screen before displaying the updated state

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")
        print(stages[lives])

        if "_" not in display:
            end_of_game = True
            print("You win.")

    if play_again():
        clear_screen()
    else:
        break
