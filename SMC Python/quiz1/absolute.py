def absolute() :
    try:
        num = float(input('Enter a number: '))

    except ValueError:
        print('input needs to be a numeric value')

    ab = abs(num)
    print(f'absolute value on {num} is {ab}')

absolute()