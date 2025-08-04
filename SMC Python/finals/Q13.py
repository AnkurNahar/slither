def main():
    
    gold_count = 0

    while 1:
        name = input("enter name: ")
        
        if name == "leave":
            print(f"\nentered gold {gold_count} times")
            return        
        elif name == "gold":
            gold_count += 1


if __name__ == "__main__":
    main()