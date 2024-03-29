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
#
# Problem #1: Scoring a word
#
def get_word_score(word: str, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    """
    Word Length and Score Calculation
        Calculate word length in word_length.
        Calculate word score by summing SCRABBLE_LETTER_VALUES values.
        Store score in word_score.
        Add 50 points to word_score if length equals n.
        Return final word_score.
    """
    word_length = len(word)
    word_score = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word) * word_length
    if word_length == n:
        word_score += 50
    return word_score
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand: dict):
    """
    Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter, count in hand.items():
        for _ in range(count):
            print(letter, end=" ")
    print()
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    """
    Vowel Generation Process
        Calculate num_vowels by dividing n by 3 and store it in a variable.
        Initialize an empty dictionary, hand.
        Generate vowels by randomly selecting a vowel from the VOWELS list and adding it to the hand dictionary.
        Generate consonants by randomly selecting a consonant from the CONSONANTS list and adding it to the hand dictionary.
        Return the generated hand dictionary.
    """
    num_vowels = n // 3
    hand = {}
    for _ in range(num_vowels):
        vowel = random.choice(VOWELS)
        hand[vowel] = hand.get(vowel, 0) + 1
    for _ in range(num_vowels, n):
        consonant = random.choice(CONSONANTS)
        hand[consonant] = hand.get(consonant, 0) + 1
    return hand
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand: dict, word: str):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    """
    Hand Dictionary Creation and Maintenance
        Create a new dictionary, updated_hand.
        Decrease each letter's count in updated_hand dictionary by 1.
        Return the updated_hand dictionary.
    """
    updated_hand = hand.copy()
    for letter in word:
        updated_hand[letter] -= 1
    return updated_hand
#
# Problem #3: Test word validity
#
def is_valid_word(word: str, hand: dict, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    """
    Word Analysis Procedure
        Check if word is not present in word_list.
        Create a copy of hand dictionary and store in hand_copy.
        Check if letter count in hand_copy is 0.
        If not, decrement count by 1.
        If all letters are available, return True.
    """
    word = word.lower()
    hand_copy = hand.copy()
    
    # Check if word is not present in word_list
    if word not in word_list:
        return False
    
    # Check if word can be formed using letters in the hand
    for letter in word:
        if hand_copy.get(letter, 0) == 0:
            return False
        hand_copy[letter] -= 1
        
    return True

def calculate_hand_len(hand: dict):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

def play_hand(hand: dict):
    """
    Allows the user to play out a single hand.

    hand: dictionary (string-> int)
    """
    """
    Infinite Loop Implementation
        Initialize variable total_score to 0.
        Run infinite loop: print current hand, 
        prompt user for input, 
        break if input is a period, 
        print message if input is invalid, 
        calculate word score, 
        add word score to total score, 
        print word, score, and total score, 
        update hand by removing letters, exit loop, print total score.
    """
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
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """
    """
    Game Handling Process
        User input: input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: ").lower().
        Hand: deal_hand(HAND_SIZE)
        Last hand: hand
        If user_input == 'n': hand = deal_hand(HAND_SIZE)
        If user_input == 'r': last_hand = hand
        If user_input == 'e': exiting the game
        If user_input == 'e': break
        If user_input == 'n', 'r', or 'e', continue.
    """
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