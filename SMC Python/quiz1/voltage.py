def voltage():
    try:
        volt = float(input('Enter a voltage value: '))

    except ValueError:
        print('input needs to be a numeric value')

    if volt <= 30 :
        print('low voltage')

    elif volt > 30 and volt < 60 :
        print('medium voltage')

    elif volt >= 60 and volt < 240 :
        print('high voltage')

    else:
        print('electrocution')
    
voltage()