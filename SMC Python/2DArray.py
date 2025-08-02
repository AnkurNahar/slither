import numpy as np


def clear(arr):
   arr.fill(0)


def main():


   arr = np.arange(0, 25).reshape(5,5)
   row = 2
   col = 2
   clear(arr)
   arr[row, col] = 1


   while (True):
       print("Welcome to udlr, we wrap around")
       print("\tu # will print out # up moves")
       print("\td # will print out # down moves")
       print("\tl # will print out # left moves")
       print("\tr # will print out # right moves")
       print("\texit will exit the program")
       print("")


       print(arr)


       clear(arr)




       sentence = input("Please enter your command : ")
       words = sentence.split()


       ### Take action as per selected menu-option ###
       if (words[0] == "u"):
           try:
              x = int(words[1])
           except:
              x = 1
           print("U says ", x)
           for i in range(x):
               row = (row - 1) % 5
               clear(arr)
               arr[row, col] = 1
               print(arr)


       elif (words[0] == "d"):
           try:
              x = int(words[1])
           except:
              x = 1
           print("D says ", x)
           for i in range(x):
               row = abs((row + 1) % 5)
               print("row = ", row, " col = ", col)
               clear(arr)
               arr[row, col] = 1
               print(arr)


       elif (words[0] == "l"):
           try:
              x = int(words[1])
           except:
              x = 1
           print("L says ", x)
           for i in range(x):
               col = (col - 1) % 5
               clear(arr)
               arr[row, col] = 1
               print(arr)


       elif (words[0] == "r"):
           try:
              x = int(words[1])
           except:
              x = 1
           print("R says ", x)
           for i in range(x):
               col = (col + 1) % 5  
               clear(arr)
               arr[row, col] = 1
               print(arr)


       elif words[0] == "exit":
           print("Exit program...")
           break
       else:  ## defauult 
           print("Invalid input. Try again...")




main()
