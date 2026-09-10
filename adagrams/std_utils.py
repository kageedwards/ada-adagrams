from random import randint

def randindex(list: list) -> int:
    try:
        random_index = randint(0, len(list) - 1)
        return random_index
    except ValueError as err:
        return 0

# Binary search
# Look in the middle.
# - if it's our letter, return it,
# - if it's not, move left and right
# - based on which direction the letter's in.
# Search gets smaller and smaller.
# | --------------> mid <-------------- |
# | ----> mid <---- |
# | -mid- |
# mid is needle. return mid
def binary_search(haystack: list, needle: str) -> int | None:
    left = 0
    right = len(haystack)

    while(left < right):
        # find the middle index of the list
        middle = (left + right) // 2

        # if equal, we zeroed in on the letter. return the index
        if haystack[middle].casefold() == needle.casefold():
            return middle
        # if letter comes after this item, move the left wall in
        elif haystack[middle].casefold() < needle.casefold():
            left = middle + 1
        # if letter comes before this, move the right wall
        # to our current middle
        elif haystack[middle].casefold() > needle.casefold():
            right = middle

    # if nothing came up at all...
    return None