from getLive import GetLive
from date import Date 
from ledger import Ledger
from wallet import Wallet

class Main:

    def __init__(self):
        self.getLive = GetLive()
        self.date = Date()
        self.ledger = Ledger()
        self.wallet = Wallet()
        print('1. Check price\n2. Buy Bitcoin\n3. Sell Bitcoin\n4. Check balance\n5. View history\n6. Exit')
        try:
            self.user_req = int(input('Enter any value from 1 to 6: '))

        except ValueError:
            print('input needs to be a numeric value')



    def run(self):

        while self.user_req != 6:
            self.operations()
            self.takeUserInput()



    def takeUserInput(self):
        try:
            self.user_req = int(input('Enter any value from 1 to 6: '))

        except ValueError:
            print('input needs to be a numeric value')



    def operations(self):   
        match self.user_req:
            case 1:
                currentPrice = self.getLive.getUpdatedPrice()
                print(f'Current Bitcoin Price: ${currentPrice}')

            case 2:
                self.buy()

            case 3:
                self.sell()

            case 4:
                currentPrice = self.getLive.getBitcoinPrice()
                self.wallet.displayBalance(currentPrice)

            case 5:
                self.ledger.displayTransactions()

            case _:
                print('invalid input')

    def buy():
        pass

    def sell():
        pass

    
if __name__ == "__main__":
    app = Main()
    app.run()