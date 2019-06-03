input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]
def contain_even(input_list):
    even_number = filter(lambda x: x % 2 == 0, input_list)
    return len(list(even_number)) != 0

print(contain_even(input_list))