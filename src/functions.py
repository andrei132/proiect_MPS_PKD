from functools import reduce

def min_leafs(*data):
    """
    data - List of data.
    """
    return min(data)

def max_leafs(*data):
    """
    data - List of data.
    """
    return max(data)

def arithmetic_average(*data):
    """
    data - List of data.
    """
    return sum(data) / len(data)

def geometric_average(*data):
    """
    data - List of data.
    """
    return reduce(lambda x, y: x * y, data) ** (1 / len(data))

def weighted_average(data, dataw):
    """
    data - List of data.\n
    dataw - List of weights.
    """
    weighted_sum = sum(data[i] * dataw[i] for i in range(len(data)))
    total_weights = sum(dataw)
    return weighted_sum / total_weights