def didIFail():
    try:
        score = float(input('Enter your score: '))

    except ValueError:
        print('input needs to be a numeric value')

    match score:
        case s if s < 60:
            print('Yeah, you did fail, I’m sorry.')
        case s if s < 70:
            print('It’s a D.')
        case s if s < 80:
            print('It’s a C!')
        case s if s < 90:
            print('No, you got a B!')
        case s if s <= 100:
            print('No, you got an A!')
        case _:
            print('invalid score') 
    

didIFail()