def didIFail():
    try:
        score = float(input('Enter your score: '))

    except ValueError:
        print('input needs to be a numeric value')

    if score < 60:
        print('Yeah, you did fail, I’m sorry.')
    elif score < 70:
        print('It’s a D.')
    elif score < 80:
        print('It’s a C!')
    elif score < 90:
        print('No, you got a B!')
    elif score <= 100:
        print('No, you got an A!')
    else:
       print('invalid score') 
    

didIFail()