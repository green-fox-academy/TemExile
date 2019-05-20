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
    def __init__(self):
        self.queuelist = []
    def add(self, newpatient):
        