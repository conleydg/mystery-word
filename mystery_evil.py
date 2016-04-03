import re
import sys
import random



def parse_words(evil_word_list, word_length):
    with open('/usr/share/dict/words') as f:
        for word in f.readlines():
            word = re.sub(r'[^A-Za-z]', "", word).lower()
            if len(word) != len(set(word)):
                False
            elif len(word) == word_length:
                evil_word_list.append(word)
        return evil_word_list




def user_guess(correct_guesses, incorrect_guesses):
    while True:
        user_input = input('Please enter your guess: ').lower()
        if user_input.isalpha():
            if len(user_input) != 1 or  user_input.isdigit():
                print('Try again - Only enter one letter!!')
            elif user_input in correct_guesses or user_input in incorrect_guesses:
                print('you already guessed that letter, please try again.')
            else:
                return user_input
        else:
            print('Try again - Only enter one letter!!')


def win_or_lose(computers_word, correct_guesses):
    test_correctness_word = ''
    for letter in computers_word:
        if letter in correct_guesses:
            test_correctness_word += letter
    if test_correctness_word == computers_word:
        return True

def count_character_per_index(evil_word_list, guess, word_length):
    while True:
        character_index_count = [0] * word_length
        print(character_index_count)
        for word in evil_word_list:
            index = 0
            for character in word:
                if character == guess:
                    character_index_count[index] = character_index_count[index] +  1
                index += 1
        print(character_index_count)
        return character_index_count





def choose_most_possible_words(evil_word_list, max_index, user_input, evil_word_list_update):
    for word in evil_word_list:
        if word[max_index] == user_input:
            evil_word_list_update.append(word)
    return evil_word_list_update


def update_correct_guess_for_print(correct_guess_for_print):
    for item in correct_guess_for_print:
        item = ('-')
    return correct_guess_for_print

def update_correct_guess_for_print(correct_guess_for_print, max_index, user_input):
    correct_guess_for_print[max_index] = user_input
    return correct_guess_for_print







def main():
    remaining_guesses = 8
    evil_word_list = []
    evil_word_list_update = []
    guessed_letters = []
    correct_guesses =[]
    incorrect_guesses = []


    word_length = int(input('How long of a word do you want me to pick, must be between 4 and 12 characters: '))

    correct_guess_for_print = ['-'] * word_length

    parse_words(evil_word_list, word_length)


    while remaining_guesses > 1:
        user_input = user_guess(correct_guesses, incorrect_guesses)

        count_guess_per_index = count_character_per_index(evil_word_list, user_input, word_length)

        max_index = count_guess_per_index.index(max(count_guess_per_index))

        print(max_index)


        if count_guess_per_index[max_index] == 0:
            incorrect_guesses.append(user_input)
            print('That was an incorrect guess')

        elif count_guess_per_index[max_index] > 1:
            correct_guesses.append(user_input)
            print('That was a correct guess')
            choose_most_possible_words(evil_word_list, max_index, user_input, evil_word_list_update)


        print(update_correct_guess_for_print(correct_guess_for_print, max_index, user_input))



        del evil_word_list
        evil_word_list = evil_word_list_update
        del evil_word_list_update
        evil_word_list_update = []

        print(len(evil_word_list))



















if __name__ == "__main__":
    main()
