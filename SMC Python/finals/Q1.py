import statistics

def displaySum():

    numbers = []
    for i in range(3):
        num = float(input(f"enter number {i+1}: "))
        numbers.append(num)

    total = sum(numbers)
    avg = statistics.mean(numbers)

    print(f"sum: {total}")
    print(f"average: {avg}")

displaySum()