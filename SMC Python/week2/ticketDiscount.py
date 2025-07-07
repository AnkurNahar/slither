def ticketDiscount():
    try:
        age = int(input('Ticket costs $14.\nWhat is your age? : '))

    except ValueError:
        return print('input needs to be a numeric value')

    if age < 18:
        print('You qualify for a $10 ticket because you are a minor.')
    elif age >= 65:
        print('You qualify for a $10 ticket because you are a senior citizen.')
    else:
       print('You must pay $14.') 
    

ticketDiscount()