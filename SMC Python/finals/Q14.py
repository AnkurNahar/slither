def zerosAndOnes(li):
    d = {0: 0, 1: 0}  
    for num in li:
        if num in d:
            d[num] += 1
    return d


s = [1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1]
print(zerosAndOnes(s)) 