from random import randint
from adagrams.std_utils import randindex, binary_search

LETTER_WEIGHTS = {
    "A": 9, "B": 2, "C": 2, "D": 4,
    "E": 12, "F": 2, "G": 3, "H": 2,
    "I": 9, "J": 1, "K": 1, "L": 4,
    "M": 2, "N": 6, "O": 8, "P": 2,
    "Q": 1, "R": 6, "S": 4, "T": 6,
    "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1
}

LETTER_SCORES = {
    "A": 1, "E": 1, "I": 1, "O": 1,
    "U": 1, "L": 1, "N": 1, "R": 1,
    "S": 1, "T": 1, "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4,
    "Y": 4, "K": 5, "J": 8, "X": 8,
    "Q": 10, "Z": 10
}

HAND_SIZE = 10
BONUS_POINTS = 8

def populate_letter_cache(letter_list: list):
    if not letter_list:
        for letter, weight in LETTER_WEIGHTS.items():
            for i in range(0, weight):
                letter_list.append(letter)

def draw_letters() -> list[str]:
    hand = []
    # Generate a simple list containing all the individual instances of
    # available letters ( ["a", "a", "b", "c", "c", "d"] )
    letter_cache = []
    populate_letter_cache(letter_cache)

    for i in range(HAND_SIZE):
        #select a random index
        random_letter_index = randindex(letter_cache)
        # Fetch that letter, removing it from the list as we go
        random_letter = letter_cache.pop(random_letter_index)
        # Add it to the hand
        hand.append(random_letter)

    return hand

def uses_available_letters(word: str, letter_bank: list) -> bool:
    # Let's not mess up the referenced letter_bank list
    letter_bank_tmp = letter_bank.copy()
    letter_bank_tmp.sort()
    for i in range(len(word)):
        # Find first instance of this letter in the letter_bank
        first_index_of = binary_search(letter_bank_tmp, word[i])

        # If not found, it all fails
        if first_index_of is None:
            return False

        # If we got here, remove that letter and continue checking
        letter_bank_tmp.pop(first_index_of)

    # If we got through the entire word safely,
    # all the letters were available in the letter bank
    return True

def score_word(word: str) -> int:
    total = 0
    # note: this is problematic for future i18n
    cmp_word = word.upper()
    for i in range(len(cmp_word)):
        total += LETTER_SCORES[cmp_word[i]]

    # this word gets a bonus :3
    if len(cmp_word) >= 7:
        total += BONUS_POINTS

    return total

def get_highest_word_score(word_list: list) -> int | None:
    # yay, sanity checks
    if not word_list:
        return None

    # score the first word
    highest_score = score_word(word_list[0])
    winning_word = word_list[0]

    # algo to find the highest
    for i in range(1, len(word_list)):
        score = score_word(word_list[i])
        word = word_list[i]
        # Score is higher. Simple.
        if score > highest_score:
            highest_score = score
            winning_word = word
        # Tie breaking logic
        elif score == highest_score:
            # Word over ten letters supercedes, 
            # unless the previous candidate matches it
            if len(word) >= 10 and len(word) != len(winning_word):
                highest_score = score
                winning_word = word
            # otherwise, thesmallest word takes precedence.
            elif len(word) < len(winning_word) < 10:
                highest_score = score
                winning_word = word

    return ( winning_word, highest_score )