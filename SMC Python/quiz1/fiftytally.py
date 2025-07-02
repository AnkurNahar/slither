def fiftytally():
    num = 0
    tally = 0
    while num >= 0:
        num = float(input('Enter a number: '))
        if num > 50:
            tally += 1
        
    print(f'{tally} numbers entered were greater than 50') 
    

fiftytally()