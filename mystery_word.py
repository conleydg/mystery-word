import re
import sys
import random


def read_words_file(easy_words, normal_words, hard_words):
    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            word = re.sub(r'[^A-Za-z]', "", word).lower()
            if  len(word) >=4 and len(word) <= 6:
                easy_words.append(word)
            elif len(word) >= 6 and len(word) <= 8:
                normal_words.append(word)
            elif len(word) >= 8:
                hard_words.append(word)

def chose_word_difficulty_based(user_difficulty_input, easy_words, normal_words, hard_words):
    while True:
        if user_difficulty_input == 'easy':
            return random.choice(easy_words)
        elif user_difficulty_input == 'normal':
            return random.choice(normal_words)
        elif user_difficulty_input == 'hard':
            return random.choice(hard_words)


def is_guess_hit_or_miss(user_input, computers_word):
    if user_input in computers_word:
        return True
    else:
        return False


def user_guess():
    while True:
            user_input = input('Please enter your guess: ').lower()
            if user_input.isalpha():
                if len(user_input) != 1 or  user_input.isdigit():
                    print('Try again - Only enter one letter!!')
                else:
                    return user_input
            else:
                print('Try again - Only enter one letter!!')


def word_dispay(computers_word,correct_guesses):
    for letter in computers_word:
        if letter in correct_guesses:
            print(letter, " ", end="")
        else:
            print('- ', end="")


def win_or_lose(computers_word, correct_guesses):
    test_correctness_word = ''
    for letter in computers_word:
        if letter in correct_guesses:
            test_correctness_word += letter
    if test_correctness_word == computers_word:
        return True

def play_again():
    return input('Would you like to play again? Y/N: ')

def difficulty_input():
    while True:
        difficulty = input('Which mode you would you like to Play?\n'
                '\nPlease type Easy/Normal/Hard and hit enter:  ').lower()
        if difficulty == 'easy' or difficulty == 'normal' or difficulty == 'hard':
            return difficulty
        else:
            print('You did not enter Easy, Normal, or Hard')


def main():
    easy_words = []
    normal_words = []
    hard_words = []
    correct_guesses = []
    incorrect_guesses = []

    guess_count = 0

    read_words_file(easy_words, normal_words, hard_words)

    welcome_message = print('\n\nWelcome to the mystery word game! \n \n')


    user_difficulty_input = difficulty_input()


    computers_word = chose_word_difficulty_based(user_difficulty_input, easy_words, normal_words, hard_words)


    print('The computer\'s word contains {} letters'.format(len(computers_word)))

    while True:
        remaining_guesses = 8 - guess_count
        user_input = user_guess()


        if user_input in correct_guesses or user_input in incorrect_guesses:
            print('you already guessed that letter, please try again.')
        else:
            if is_guess_hit_or_miss(user_input, computers_word):
                    correct_guesses.append(user_input)
                    print('\nGood Guess!!')
            elif not is_guess_hit_or_miss(user_input, computers_word):
                    guess_count += 1
                    incorrect_guesses.append(user_input)
                    print('\nBad Guess!')

        word_display = word_dispay(computers_word,correct_guesses)

        remaining_guesses = 8 - guess_count

        win = win_or_lose(computers_word, correct_guesses)

        if win:
            print('\nYou won!!')
            if play_again() == 'y':
                main()
            break

        if remaining_guesses == 0:
            print('\nYou lose! The computer\'s word was {}'.format(computers_word))
            if play_again() == 'y':
                main()
            break

        print('\nYou have {} guess remaining'.format(remaining_guesses))
        print(computers_word)



if __name__ == "__main__":
    main()
