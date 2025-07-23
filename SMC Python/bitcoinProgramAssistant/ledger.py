class Ledger:

    transactions = list()

    def addNewTransaction(self, transaction):
        self.transactions.append(transaction)

    def displayTransactions(self):
        for transaction in self.transactions:
            print(transaction)

    