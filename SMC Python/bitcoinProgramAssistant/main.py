from getLive import GetLive
from date import Date 
from ledger import Ledger
from wallet import Wallet

class Main:

    def __init__(self):
        self.getLive = GetLive()
        self.date = Date()
        self.ledger = Ledger()
        self.wallet = Wallet(0, 75000)
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

    def buy(self):
        try:
            is_float = 0
            amount = 0
            buy_amount = input('Enter value : ')
            if '.' in buy_amount:
                amount = float(buy_amount)
                is_float = 1
            else:
                amount = int(buy_amount)

        except ValueError:
            print('input needs to be a numeric value')

        crypto, cash = self.wallet.getWalletInfo()
    
        if is_float:
            current_price = self.getLive.getBitcoinPrice()
            amount = amount * current_price

        if amount > cash:
            return print('insufficient funds')
        
        new_cash = cash - amount
        new_bits = amount/current_price
        new_crypto = crypto + new_bits

        self.wallet.setWalletInfo(new_crypto, new_cash)
        str = f'Bought {new_bits} Bitcoin on {self.date.formatDate()}'
        self.ledger.addNewTransaction(str)
        print(str)


    def sell(self):
        
        try:
            is_cash = 0
            amount = 0
            bits = 0
            sell_amount = input('Enter value : ')
            if '.' in sell_amount:
                amount = float(sell_amount)
            else:
                amount = int(sell_amount)
                is_cash = 1


        except ValueError:
            print('input needs to be a numeric value')

        crypto, cash = self.wallet.getWalletInfo()
        current_price = self.getLive.getBitcoinPrice()
    
        if is_cash:
            amount = amount / current_price

        if amount > crypto:
            return print('insufficient funds')
        
        new_crypto = crypto - amount
        added_cash = amount * current_price
        new_cash = cash + added_cash

        self.wallet.setWalletInfo(new_crypto, new_cash)
        str = f'Sold {amount} Bitcoin on {self.date.formatDate()}'
        self.ledger.addNewTransaction(str)
        print(str)

    
if __name__ == "__main__":
    app = Main()
    app.run()