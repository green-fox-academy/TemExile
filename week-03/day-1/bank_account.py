class currency(object):
    def __init__(self, code, centralBank, value):
        self.code = code
        self.centralBank = centralBank
        self.value = value

class USADollar(currency):
    def __init__(self, value):
        self.code = 'USA'
        self.centralBank = 'Federal Reserve System'
        super().__init__()
class HungarianForint(currency):
    def __init__(self, value):
        self.code = 'HUF'
        self.centralBank = 'Hungarian National Bank'
        super().__init__()

class bankAccount(object):
    def __init__(self, pin, curr):
        self.pin = pin
        self.curr = curr
    def deposit(self, amount):
        if amount > 0:
            self.curr.value += amount
        else:
            print('Please deposit the right amount')
    def withdraw(self, pin, amount):
        if self.pin == pin and self.curr.value >= amount:
            self.curr.value -= amount
            return amount
        elif self.pin != pin:
            print('Please enter the right pin')
            return 0
        elif self.curr.value < amount:
            print('You do not have enough balance in you account.')
            return 0

class bank(object):
    def __init__(self, accountlist = []):
        self.accountlist = accountlist
    def createAccount(self, newaccount):
        self.accountlist.append(newaccount)
    def getAllMoney(self):
        totalamount = 0
        for account in self.accountlist:
            value = account.curr.value
            totalamount += value
        return totalamount