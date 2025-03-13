def encodeString(stringVal):
    currentChar = stringVal[0]
    count = 0
    encoding = []
    for char in stringVal:
        if char == currentChar:
            count += 1
        else:
            strTuple = (currentChar, count)
            encoding.append(strTuple)
            currentChar = char
            count = 1

    strTuple = (currentChar, count)
    encoding.append(strTuple)
    return encoding

def decodeString(encodedList):
    decodedString = ''

    for eachTuple in encodedList:
        count = eachTuple[1]
        while count > 0:
            decodedString += eachTuple[0]
            count -= 1

    return decodedString
    