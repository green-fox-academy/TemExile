import random

class cab(object):
    def __init__(self, state = 'playing', counter = 0):
        self.state = state
        self.counter = counter
        self.number = list(map(lambda x : str(random.randint(0,9)),[1,2,3,4]))
        self.goal = (1000 * int(self.number[0]) + 100 * int(self.number[1])+
        10 * int(self.number[2]) + int(self.number[3]))
    def guess(self):
        bull = 0
        cow = 0
        self.counter += 1
        guess_number = input()
        num = list(guess_number)
        temp1 = self.number
        temp2 = self.number
        for i in range(len(num)):
            if num[i] == temp1[i]:
                cow += 1
            elif num[i] in temp2:
                bull += 1
                temp2.remove[num[i]]
        if (cow != 0 or bull != 0) and cow != 4:
                return f'{cow} cow, {bull} bull.'
        elif cow == 4:
            self.state = 'finish'
            return f'You got the Number!'