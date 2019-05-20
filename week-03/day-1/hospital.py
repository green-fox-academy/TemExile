import random
class patient(object):
    def __init__(self):
        self.severity = random.randint(1,10)
    def retrieve(self):
        return self.severity
    def treat(self):
        self.severity -= 1
        if self.severity < 0:
            self.severity = 0

class queue(object):
    def __init__(self, q_type):
        self.q_type = q_type
        self.queuelist = []
    def add(self, newpatient):
        self.queuelist.append(newpatient)
        self.queuelist = list(filter(lambda x : x > 0, self.queuelist))
        if q_type == 'safe':
            safe_queue = sorted(self.queuelist, key = lambda x : x.retrieve())
            return safe_queue
        elif q_type == 'classic':
            return self.queuelist
    def getNext(self):
