import random
import copy
import logging
from init import configure_logging

def random_choice(data, end=None, number=None):
    """
    data - It can be the beginning of a range or a list.\n
    end - End of an interval. [Optional]\n
    number - Number of random objects from list. [Optional]
    """
    configure_logging()
    if isinstance(data, int) and isinstance(end, int) and number is None:
        return random.randint(data, end)
    elif isinstance(data, list) and end is None and number is None:
        algorithm = random.choice(data)
        logging.info(f'{algorithm}')
        return algorithm
    elif isinstance(data, list) and end is None and isinstance(number, int):
        data = copy.copy(data)
        randomlist = []
        for _ in range(number):
            algorithm = random.choice(data)
            if isinstance(algorithm, str):
                logging.info(f'A fost aleasa functia : {algorithm}')
            data.remove(algorithm)
            randomlist.append(algorithm)
        return randomlist
    else:
        return None

def random_numers_between(end, count, star=0):
    """
        Generate a random list with number in range
    """
    return random.sample(range(star, end), count)