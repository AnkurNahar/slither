from race import Race

def main():
    balance = 200
    horses = [1, 2, 3, 4]

    print("To place an exacta bet enter: exacta num1 num2")
    print("To place an exactabox bet enter: exactabox num1 num2")
    print("To place a trifecta bet enter: trifecta num1 num2 num3")
    print("To place a trifectabox bet enter: trifectabox num1 num2")
    print("To check balace enter: balance")
    print("To stop enter: exit")

    while 1:
        race = Race(horses.copy())
        result = race.readysetgo()
        print(f"\ncheat: {result}")  

        cmd = input("bet> ")

        if cmd == "exit":
            return

        elif cmd == "balance":
            print(f"balance: ${balance}")
            continue

        parts = cmd.split()
        bet_type = parts[0]
        bet_numbers = list(map(int, parts[1:]))

        match bet_type:
            case "exacta":
                if len(bet_numbers) != 2:
                    print("need 2 numbers")
                    continue

                cost = 15
                if balance < cost:
                    print("insufficient funds")
                    continue

                balance -= cost
                if race.exacta(bet_numbers, result):
                    balance += 150
                    print("You won Exacta!")
                else:
                    print("You lost Exacta")

            case "exactabox":
                if len(bet_numbers) != 2:
                    print("need 2 numbers")
                    continue

                cost = 10
                if balance < cost:
                    print("insufficient funds")
                    continue

                balance -= cost
                if race.exactabox(bet_numbers, result):
                    balance += 100
                    print("You won Exactabox!")
                else:
                    print("You lost Exactabox")

            case "trifecta":
                if len(bet_numbers) != 3:
                    print("need 3 numbers")
                    continue

                cost = 20
                if balance < cost:
                    print("insufficient funds")
                    continue

                balance -= cost
                if race.trifecta(bet_numbers, result):
                    balance += 250
                    print("You won Trifecta!")
                else:
                    print("You lost Trifecta")

            case "trifectabox":
                if len(bet_numbers) != 3:
                    print("need 3 numbers")
                    continue

                cost = 18
                if balance < cost:
                    print("insufficient funds")
                    continue

                balance -= cost
                if race.trifectabox(bet_numbers, result):
                    balance += 180
                    print("You won Trifectabox!")
                else:
                    print("You lost Trifectabox")

            case _:
                print("invalid input")
                continue

        print(f"updated balance: ${balance}")
        if balance <= 0:
            print("You have zero balance")
            return

if __name__ == "__main__":
    main()