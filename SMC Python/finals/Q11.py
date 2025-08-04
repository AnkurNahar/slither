def printIt(arr):
    for num in arr:
        print(num, end=" ")

def findItem(arr, num):
    return num in arr

def main():
    arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    printIt(arr1)
    has_num = findItem(arr1, 50)
    print(f"\nHas 50: {has_num}")

    arr2 = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110]
    printIt(arr2)
    has_num = findItem(arr2, 50)
    print(f"\nHas 50: {has_num}")


if __name__ == "__main__":
    main()