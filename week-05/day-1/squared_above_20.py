input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def square_above_20(input_list):
    square_above_20 = list(filter(lambda x : x**2 > 20, input_list))
    return square_above_20