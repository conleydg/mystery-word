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

def game_difficulty(user_difficulty_input, easy_words, normal_words, hard_words):
    if user_difficulty_input == 'easy':
        return random.choice(easy_words)
    elif user_difficulty_input == 'normal':
        return random.choice(normal_words)
    elif user_difficulty_input == 'hard':
        return random.choice(hard_words)


def main():
    easy_words = []
    normal_words = []
    hard_words = []
    read_words_file(easy_words, normal_words, hard_words)

    welcome_print = print('Welcome to the mystery word game!')

    user_difficulty_input = input('Which mode you would you like to Play?'
                        'Please type Easy/Normal/Hard or E/N/H and hit enter:  ').lower()

    difficulty = game_difficulty(user_difficulty_input, easy_words, normal_words, hard_words)

    print(difficulty)
    print(len(easy_words))
    print(len(normal_words))
    print(len(hard_words))


if __name__ == "__main__":
    main()
