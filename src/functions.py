from functools import reduce
import numpy as np

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

def calculate_median(*data):
    """
    data - List of data.
    """
    sorted_list = sorted(*data)
    length = len(sorted_list)
    
    if length % 2 == 0:
        left_middle = sorted_list[length // 2 - 1]
        right_middle = sorted_list[length // 2]
        median = (left_middle + right_middle) / 2
    else:
        median = sorted_list[length // 2]
    
    return median

def power_limit(data, power):
    """
    data - List of data.
    """
    result = np.power(data, power)
    return np.max(np.maximum(0, np.minimum(1, result)))

def log_limit(data):
    """
    data - List of data.
    """
    result = np.log(data + 1)
    return np.max(np.maximum(0, np.minimum(1, result)))

def sin_limit(data):
    """
    data - List of data.
    """
    result = np.sin(data)
    return np.min(np.maximum(0, np.minimum(1, result)))
    
