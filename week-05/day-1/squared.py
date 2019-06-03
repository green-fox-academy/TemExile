input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def square(input_list):
    positive = filter(lambda x: x > 0, input_list)
    squared_list = list(map(lambda x : x**2, positive))
    return squared_list
