import random

class GetLive:

    bitcoin_price = 30000

    def getBitcoinPrice(self):
        return self.bitcoin_price

    def getUpdatedPrice(self):
        self.bitcoin_price = random.uniform(25000, 34000)
        return self.bitcoin_price