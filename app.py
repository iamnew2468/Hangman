import random
from words import words
import string


def valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed_letter = set()

    while len(word_letter) > 0:
        print("\n\nYou have used these letter : "," ".join(guessed_letter))

        word_list = [letter if letter in guessed_letter else '_' for letter in word]
        print("current word :", " ".join(word_list))

        current_letter = input("Enter the letter :").upper()

        if current_letter in alphabet - guessed_letter:
            guessed_letter.add(current_letter)
            if current_letter in word_letter:
                word_letter.remove(current_letter)

        elif current_letter in guessed_letter:
            print("The letter is already used")

        else:
            print("Invalid letter")

    print("You have guessed the word : ", word)


hangman()