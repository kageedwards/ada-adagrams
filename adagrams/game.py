from random import randint
from adagrams.std_utils import minimum, maximum, randindex

LETTER_WEIGHTS = {
    "A": 9, "B": 2, "C": 2, "D": 4,
    "E": 12, "F": 2, "G": 3, "H": 2,
    "I": 9, "J": 1, "K": 1, "L": 4,
    "M": 2, "N": 6, "O": 8, "P": 2,
    "Q": 1, "R": 6, "S": 4, "T": 6,
    "U": 4, "V": 2, "W": 2, "X": 1,
    "Y": 2, "Z": 1
}

HAND_SIZE = 10

def populate_letter_cache(letter_list: list):
    if not letter_list:
        for letter, weight in LETTER_WEIGHTS.items():
            for i in range(0, weight):
                letter_list.append(letter)

def draw_letters() -> list[str]:
    hand = []
    letter_cache = []
    populate_letter_cache(letter_cache)

    for i in range(HAND_SIZE):
        random_letter_index = randindex(letter_cache)
        random_letter = letter_cache.pop(random_letter_index)
        hand.append(random_letter)

    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass