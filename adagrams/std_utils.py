from random import randint
# Custom min() function
def minimum(items: list) -> int | None:
    todo("Implement min")

# Custom max() function
def maximum(items: list) -> int | None:
    todo("Implement max")
    
def randindex(list: list) -> int:
    try:
        random_index = randint(0, len(list) - 1)
        return random_index
    except ValueError as err:
        return 0

def binary_search(haystack: list, needle: str) -> int | None:
    left = 0
    right = len(haystack)

    while(left < right):
        middle = (left + right) // 2

        if haystack[middle].casefold() == needle.casefold():
            return middle
        elif haystack[middle].casefold() < needle.casefold():
            left = middle + 1
        elif haystack[middle].casefold() > needle.casefold():
            right = middle

    return None