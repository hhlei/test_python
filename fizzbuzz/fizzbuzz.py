def playFizzBuzz(rounds):

    if not isinstance(rounds, int):
        raise TypeError("That's not legal buddy")
    if (rounds <= 0):
        raise ValueError("That ain't right bro")
    
    output_str = ""
    for i in range(1, rounds+1): #range is [start, stop)
        if (i % 3 == 0) and (i % 5==0):
            output_str += "Fizz Buzz, "
        elif (i%3==0):
            output_str += "Fizz, "
        elif (i%5==0):
            output_str += "Buzz, "
        else:
            output_str += str(i)+ ", "
    output_str = output_str[:-2]
    return output_str

if __name__ == "__main__":
    rounds = int(input('How many rounds do you want to play? '))
    str_out = playFizzBuzz(rounds)
    print(str_out)