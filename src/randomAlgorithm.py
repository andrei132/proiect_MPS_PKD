import random
import copy

def random_choice(data, end=None, number=None):
    """
    data - It can be the beginning of a range or a list.\n
    end - End of an interval. [Optional]\n
    number - Number of random objects from list. [Optional]
    """
    if isinstance(data, int) and isinstance(end, int) and number is None:
        return random.randint(data, end)
    elif isinstance(data, list) and end is None and number is None:
        return random.choice(data)
    elif isinstance(data, list) and end is None and isinstance(number, int):
        data = copy.copy(data)
        randomlist = []
        for _ in range(number):
            algorithm = random.choice(data)
            data.remove(algorithm)
            randomlist.append(algorithm)
        return randomlist
    else:
        return None