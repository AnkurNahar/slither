def fifty():
    try:
        val = float(input('Enter a number: '))

    except ValueError:
        print('input needs to be a numeric value')

    if val > 50:
        print('input is greater than 50')
    else:
       print('input is not greater than 50') 
    

fifty()