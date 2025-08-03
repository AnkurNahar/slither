def missing(entered_set):

    N = max(entered_set)
    all_nums = set(range(1, N+1))
    entered_set = set(entered_set)
    missing_nums = sorted(all_nums - entered_set)

    return missing_nums


def main():

    nums = input("enter a set of space seperated numbers : ")
    entered_set = nums.split()
    entered_set = [int(num) for num in entered_set]
    missing_nums = missing(entered_set)
    
    if missing_nums:
        print(f"missing numbers: {missing_nums}")

if __name__ == "__main__":
    main()