import numpy as np
# only boys
input_list = [['John', 16, 'male', [5,5,4,2]], ['Jane', 15, 'female', [4,3,4,4,5]], ['Bob', 17, 'male', [2,2,3,1]]]
def onlyboys(input_list):
    boys = filter(lambda x: 'male' in x, input_list)
    return list(boys)
print(onlyboys(input_list))

# name starts with letter J
def name_starts(input_list):
    name_start_J = filter(lambda x: x[0][0] == 'J', input_list)
    return list(name_start_J)
print(name_starts(input_list))

# average grade above 4
def avg_above_4(input_list):
    above_4 = filter(lambda x: np.mean(x[3]) >= 4, input_list)
    return list(above_4)
print(avg_above_4(input_list))

# at least got two 5s
def got_two_5(input_list):
    at_least_two = filter(lambda x: len(list(filter(lambda n: n ==5, x[3])))>=2, input_list)
    return list(at_least_two)
print(got_two_5(input_list))