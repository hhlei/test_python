import numpy 

def printFizzBuzz(rounds):
    total = 20
    for i in range(1, total+1): #range is [start, stop)
        if (i % 3 == 0) and (i % 5==0):
            print("Fizz Buzz")
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    printFizzBuzz(20)