def calculateArea():
    base, height = input('enter base and height of triangle seperated by space: ').split()
    base = float(base)
    height = float(height)
    area = base * height * 0.5
    print(area)

calculateArea()