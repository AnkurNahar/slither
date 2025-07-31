class Carprocon:

    budget = 50000

    def __init__(self):
        self.price = 0.0
        self.model = ''
        self.pros = []
        self.cons = []
        self.propoints = []
        self.conpoints = []

    def setcar(self, model, price):
        self.model = model
        self.price = price

    def setpro(self, pro, point):
        self.pros.append(pro)
        self.propoints.append(point)

    def setcon(self, con, point):
        self.cons.append(con)
        self.conpoints.append(point)

    def sum(self, points):
        return sum(points)

    def printit(self):
        print(f'Budget: ${Carprocon.budget}')
        print(f'Model: {self.model}')
        print(f'Price: ${self.price}')
        print('Pros:')
        for i in range(len(self.pros)):
            print(f'   {self.pros[i]} (Priority: {self.propoints[i]})')
        print('Cons:')
        for i in range(len(self.cons)):
            print(f'   {self.cons[i]} (Priority: {self.conpoints[i]})')

    def compare(self, other):
        this_total = self.sum(self.propoints) - self.sum(self.conpoints)
        other_total = other.sum(other.propoints) - other.sum(other.conpoints)

        print(f'\nComparison:')
        print(f'{self.model} Total score: {this_total}')
        print(f'{other.model} Total score: {other_total}')

        if this_total > other_total:
            print(f'Recommended: {self.model}')
        elif other_total > this_total:
            print(f'Recommended: {other.model}')
        else:
            print('Both cars are great!')