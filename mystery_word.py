import re
import sys
import random


def read_words_file(easy_words, normal_words, hard_words):
    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            clean_word = re.sub(r'[^A-Za-z]', "", word).lower()
            if  len(word) >=4 and len(word) <= 6:
                easy_words.append(word)
            elif len(word) >= 6 and len(word) <= 8:
                normal_words.append(word)
            elif len(word) >= 8:
                hard_words.append(word)

def chose_word_difficulty_based(user_difficulty_input, easy_words, normal_words, hard_words):
    if user_difficulty_input == 'easy':
        return random.choice(easy_words)
    elif user_difficulty_input == 'normal':
        return random.choice(normal_words)
    elif user_difficulty_input == 'hard':
        return random.choice(hard_words)

def guess_hit_or_miss(user_input, computers_word, correct_guesses, incorrect_guesses):
    if user_input in computers_word:
        return True
    else:
        return False



def user_guess():
    while True:
        user_input = input('Please enter your guess: ')
        if len(user_input) != 1 or  user_input.isdigit():
            print('Try again - Only enter one letter!!')
        else:
            break
    return user_input

def word_dispay(computers_word,correct_guesses):
    for letter in computers_word:
        if letter in correct_guesses:
            print(letter, " ", end="")
        else:
            print('- ', end="")




def main():
    easy_words = []
    normal_words = []
    hard_words = []
    correct_guesses = []
    incorrect_guesses = []

    guess_count = 0

    read_words_file(easy_words, normal_words, hard_words)

    welcome_print = print('Welcome to the mystery word game!')

    user_difficulty_input = input('Which mode you would you like to Play?'
                        'Please type Easy/Normal/Hard or E/N/H and hit enter:  ').lower()

    computers_word = chose_word_difficulty_based(user_difficulty_input, easy_words, normal_words, hard_words)

    print('The computer\'s word contains {} letters'.format(len(computers_word)))

    while guess_count < 8:

        user_input = user_guess()

        if guess_hit_or_miss(user_input, computers_word, correct_guesses, incorrect_guesses):
                correct_guesses.append(user_input)
                print('Good Guess!!')
                correct_guesses.append(user_input)
        elif not guess_hit_or_miss(user_input, computers_word, correct_guesses, incorrect_guesses):
                guess_count += 1
                print('Bad Guess!')


        guess_hit_or_miss(user_input, computers_word, correct_guesses, incorrect_guesses)

        word_display = word_dispay(computers_word,correct_guesses)




        remaining_guesses = 8 - guess_count

        print('You have {} guess remaining'.format(remaining_guesses))
        print(computers_word)






if __name__ == "__main__":
    main()
