from carprocon import Carprocon

class Main:

    def __init__(self):
        self.car1 = Carprocon()
        self.car2 = Carprocon()

    def run(self):
        self.car1.setcar('Tesla Model 3', 48000)
        self.car1.setpro('great gas mileage', 7)
        self.car1.setpro('color quality', 8)
        self.car1.setpro('engine health', 6)
        self.car1.setcon('expensive repairs', 8)
        self.car1.setcon('scratches', 6)
        self.car1.setcon('high fuel consumption', 7)

        self.car2.setcar('Toyota Camry', 35000)
        self.car2.setpro('great gas mileage', 7)
        self.car2.setpro('color quality', 8)
        self.car2.setpro('engine health', 6)
        self.car2.setcon('expensive repairs', 7)
        self.car2.setcon('scratches', 6)
        self.car2.setcon('high fuel consumption', 5)

        print('\nCar 1:')
        self.car1.printit()

        print('\nCar 2:')
        self.car2.printit()

        self.car2.compare(self.car1)


if __name__ == "__main__":
    app = Main()
    app.run()