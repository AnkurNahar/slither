def calculatePrice():
    product_price = 50
    try:
        money_owned = float(input('How much money do you have? : '))

    except ValueError:
        return print('input needs to be a numeric value')
    
    money_required = product_price + (8 / 100 * product_price)

    if money_owned < money_required:
        print('You can not buy this product.')
    else:
       print(f'Congratulations on your purchase! You have ${money_owned - money_required} left.') 
    

calculatePrice()