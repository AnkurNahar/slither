class Employee:

    def __init__(self, name, hours_worked, pay_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.pay_rate = pay_rate

    def calculateGrossPay(self):
        return self.hours_worked * self.pay_rate

    def __str__(self):
        return f"employee name: {self.name}, hours worked: {self.hours_worked}, pay rate: ${self.pay_rate}"


def main():
   
    print("Welcome to Pay Calculator")
    name = input("enter name: ")
    hours_worked = float(input("enter hours worked: "))
    pay_rate = float(input("enter pay rate: "))

    employee = Employee(name, hours_worked, pay_rate)

    gross = employee.calculateGrossPay()
    print(f"\ngross pay: ${gross}")

    print(employee)


if __name__ == "__main__":
    main()