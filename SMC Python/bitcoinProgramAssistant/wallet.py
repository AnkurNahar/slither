class Wallet:

    _crypto_currency = 'BTC'

    def __init__(self, current_crypto_balance, current_cash_balance):
        self._current_crypto_balance = current_crypto_balance
        self._current_cash_balance = current_cash_balance
    

    def displayBalance(self, current_bitcoin_price):
        print(f'USD Cash Balance: ${self._current_cash_balance}')
        print(f'Crypto Balance: {self._current_crypto_balance} {self._crypto_currency}')
        print(f'{self._crypto_currency} market value: {self._current_crypto_balance * current_bitcoin_price}')


    def getWalletInfo(self):
        return  self._current_crypto_balance, self._current_cash_balance
    
    def setWalletInfo(self, crypto_balance, cash_balance):
        self._current_crypto_balance = crypto_balance
        self._current_cash_balance = cash_balance

