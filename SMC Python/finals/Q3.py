def main():

    while 1:
        username = input("enter username: ")
        password = input("enter password: ")

        if username == "Magic" and password == "Kingdom1":
            return print("\nSuccess!")
        else:
            print("\nIncorrect credentials. Try again.\n\n")


if __name__ == "__main__":
    main()