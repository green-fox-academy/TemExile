input_list = [1, 3, -2, -4, -7, -3, -8, 12, 19, 6, 9, 10, 14]

def allpositive(inputlist):
    positive = filter(lambda x: x > 0, input_list)
    return len(input_list) == len(list(positive))

print(allpositive(input_list))