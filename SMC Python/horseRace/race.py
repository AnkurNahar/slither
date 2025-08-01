import random

class Race:
    def __init__(self, horses):
        self.horses = horses

    def readysetgo(self):
        random.shuffle(self.horses)
        return self.horses

    def exacta(self, bet, result):
        return bet[0] == result[0] and bet[1] == result[1]

    def exactabox(self, bet, result):
        return (bet[0] in result[:2]) and (bet[1] in result[:2])

    def trifecta(self, bet, result):
        return bet[0] == result[0] and bet[1] == result[1] and bet[2] == result[2]

    def trifectabox(self, bet, result):
        return all(horse in result[:3] for horse in bet)