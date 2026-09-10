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