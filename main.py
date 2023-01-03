import random
from animals_list import word_list
from ascii_art import logo, stages

# variable initialization
character = "_"
hidden_word = []
tries_left = 6
used_letters = []
stop_playing = False
random_word = random.choice(word_list)

# creates a list of the underscore character based on the length of the hidden word variable.
for _ in range(len(random_word)):
    hidden_word.append(character)

print(logo)
print("Welcome to Python Hangman.\n"
      f"The word that you're searching for has {len(hidden_word)} letters.")

# cheat mode for debugging
# print(f"The word is: {random_word}")

while not stop_playing:

    letter = input("Write 1 letter between letters a-z, lowercase: ")

    if not letter.isalpha():
        print("Please choose only one letter between a-z, lowercase.")

    # checks every index in the random word and if the letter in that index is
    # the same as the user input it replaces the underscore character in the hidden word
    # with the user input.
    for index in range(len(random_word)):
        choice = random_word[index]
        if choice == letter:
            hidden_word[index] = choice

    print(f"{' '.join(hidden_word)}")

    if letter not in random_word:

        if letter in used_letters:
            print(f"You have already used this letter\n.")
        else:
            used_letters.append(letter)
            tries_left -= 1
            if tries_left >= 1:
                print(f"Wrong letter. You have {tries_left} tries left.")
            else:
                print("Game over. You have no more tries left.")
                stop_playing = True

    # prints ascii graphics according to how many lives are left
    print(stages[tries_left])

    # if all the underscore characters have been replaced you have won the game!
    if character not in hidden_word:
        stop_playing = True
        print("You've won. Congratulations!")
