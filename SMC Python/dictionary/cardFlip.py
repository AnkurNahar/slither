def flipCards():
    stack1 = {
        1: "Ace",
        2: "King",
        3: "Queen",
        4: "Jack",
        5: "Ten"
    }

    stack2 = {
        1: "Ace",
        2: "King",
        3: "Queen",
        4: "Jack",
        5: "Ten"
    }
    
    key1 = int(input("Choose a from 1-5 to pick card from stack 1: "))
    key2 = int(input("Choose a from 1-5 to pick card from stack 2: "))
    
    card1 = stack1[key1]
    card2 = stack2[key2]

    print(f"\nStack 1 card: {card1}")
    print(f"Stack 2 card: {card2}")

    if card1 == card2:
        print("\nCongratulations you won!")
    else:
        print("\nBetter luck next time")

flipCards()

