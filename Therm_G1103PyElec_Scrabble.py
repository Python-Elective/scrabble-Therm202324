# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
# (end of helper code)
# -----------------------------------

def get_word_score(word):
    """
    Calculates the score for a single word according to the provided scoring rules.
    """
    SCRABBLE_LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

    word = word.lower()
    score = sum(SCRABBLE_LETTER_VALUES.get(letter, 0) for letter in word)
    return score * len(word) if word else 0

def update_hand(hand, word):
    """
    Updates the hand after a word is played.
    """
    updated_hand = hand.copy()
    for letter in word:
        updated_hand[letter] = updated_hand.get(letter, 0) - 1
    return {k: v for k, v in updated_hand.items() if v > 0}

def is_valid_word(word, hand, word_list):
    """
    Checks if a word is valid according to the game rules.
    """
    word = word.lower()
    if word not in word_list:
        return False
    words_freq = get_frequency_dict(word)
    for letter, freq in words_freq.items():
        if hand.get(letter, 0) < freq:
            return False
    return True

def calculate_hand_len(hand):
    """
    Calculates the length of the hand.
    """
    return sum(hand.values())

def play_hand(hand, word_list, n):
    """
    Allows the user to play a single hand.
    """
    total_score = 0
    while True:
        print("Current Hand:", display_hand(hand))
        word = input("Enter word, or a '.' to indicate that you are finished: ")
        if word == '.':
            break
        if not is_valid_word(word, hand, word_list):
            print("Invalid word, please try again.")
            continue
        score = get_word_score(word)
        total_score += score
        print(f'"{word}" earned {score} points. Total: {total_score} points')
        hand = update_hand(hand, word)
        if calculate_hand_len(hand) == 0:
            print("Run out of letters. Total score:", total_score, "points.")
            break
    return total_score

def play_game(word_list):
    """
    Allows the user to play multiple hands.
    """
    hand = None
    while True:
        user_input = input("Enter 'n' to deal a new hand, 'r' to replay the last hand, or 'e' to end game: ")
        if user_input == 'e':
            break
        elif user_input == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
        elif user_input == 'r':
            if hand:
                play_hand(hand, word_list, HAND_SIZE)
            else:
                print("You have not played a hand yet. Please play a new hand first!")
        else:
            print("Invalid command.")
