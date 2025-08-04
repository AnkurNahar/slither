def decimalToBinary(n):
    return bin(n)[2:]

def main():

    decimals = [10, 25, 50]
    for num in decimals:
        print(f"{num} in binary is {decimalToBinary(num)}")

if __name__ == "__main__":
    main()