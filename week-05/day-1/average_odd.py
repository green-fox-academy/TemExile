import numpy as np
input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def averageodd(input_list):
    odd_number = filter(lambda x: x%2 != 0, input_list)
    avg = np.mean(list(odd_number))
    return avg
