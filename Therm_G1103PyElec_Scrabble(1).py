import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

def get_word_score(word, n):
    word_length = len(word)
    word_score = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word) * word_length
    if word_length == n:
        word_score += 50
    return word_score

def display_hand(hand):
    for letter, count in hand.items():
        for _ in range(count):
            print(letter, end=" ")
    print()

def deal_hand(n):
    num_vowels = n // 3
    hand = {}
    for _ in range(num_vowels):
        vowel = random.choice(VOWELS)
        hand[vowel] = hand.get(vowel, 0) + 1
    for _ in range(num_vowels, n):
        consonant = random.choice(CONSONANTS)
        hand[consonant] = hand.get(consonant, 0) + 1
    return hand

def update_hand(hand, word):
    updated_hand = hand.copy()
    for letter in word:
        updated_hand[letter] -= 1
    return updated_hand

def is_valid_word(word, hand, word_list):
    word = word.lower()
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1
    return word in word_list

def calculate_hand_len(hand):
    return sum(hand.values())

def play_hand(hand):
    total_score = 0
    while True:
        print("Current Hand:", end=" ")
        display_hand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ').lower()
        if word == ".":
            break
        if not is_valid_word(word, hand, word_list):
            print("Invalid word. Please try again.")
            continue
        word_score = get_word_score(word, calculate_hand_len(hand))
        total_score += word_score
        print(f'"{word}" earned {word_score} points. Total: {total_score} points\n')
        hand = update_hand(hand, word)
    print("Total score:", total_score, "points.")

def play_game(word_list):
    last_hand = None  
    while True:
        user_input = input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: ").lower()
        if user_input == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand)
            last_hand = hand
        elif user_input == 'r':
            if last_hand:
                play_hand(last_hand)
            else:
                print("You haven't played any hand yet. Please play a new hand first.")
        elif user_input == 'e':
            print("Exiting the game.")
            break

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)