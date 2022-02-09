class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    
    def cashWithdrawal(self):
        print("Amount has been withdrawn")

    def balanceEnquiry(self):
        print("Balance remaining :")

Atm.cashWithdrawal(Atm)