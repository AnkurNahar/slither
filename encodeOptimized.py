def encodeString(stringVal):
    prevChar = stringVal[0]
    count = 0
    encoding = []
    for char in stringVal:
        if char != prevChar:
            encoding.append((prevChar, count))
            count = 0
        
        prevChar = char
        count += 1

    encoding.append((prevChar, count))
    return encoding

def decodeString(encodedList):
    decodedString = ''

    for item in encodedList:
        decodedString = decodedString + item[0] * item[1]

    return decodedString