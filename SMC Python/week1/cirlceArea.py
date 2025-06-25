import math

def calculateCircleArea(input, inputType):

    #input validation
    try :
        radius = float(input)
    except ValueError: 
        print('input needs to be a numeric value')

    if(input <= 0):
        print('input needs to be a number')
        return

    #radius calculation
    if(inputType == 'diameter'):
        radius = input/2
    elif(inputType == 'circumference'):
        radius = input/(math.pi*2)

    #calculating area
    area = math.pi * radius ** 2
    return area

print(calculateCircleArea(2.5, 'radius'))