import numpy as np
import math

def maths() :
    arr = np.array([
        [2, 3],
        [4, 5],
        [8, 10]
    ])

    # adds columns and gives new array
    newArr = arr.sum(axis=0)
    # multiplies values in array
    result = math.prod(newArr)

    print(newArr)
    print(result)

maths()