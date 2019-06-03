input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def even_number(input_list):
    output = filter(lambda x: x % 2 == 0, input_list)
    output_list = list(output)
    return output_list
