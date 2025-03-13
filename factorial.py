def factorial(num):
    if type(num) != int or num < 0:
        return None
    if num == 0 :
        return 1
    i = num
    factorial = num
    while i > 1 :
        i -= 1
        factorial *= i
    return factorial  
    #return num * factorial(num-1) -> rrcursive method

number = 5
result = factorial(number)
print(result)