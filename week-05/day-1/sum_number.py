input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def sum_number(input_list):
    even_below_10 = filter(lambda x: x%2 == 0 and x<= 10, input_list)
    output = sum(list(even_below_10))
    return output