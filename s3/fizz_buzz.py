#kelly jaramillo, 8-11-2020 fcc python class learnTogether Week 3 code, step 1
#this will use a funciton called fizz_buzz.
#we will get input from our user.  send that input to the fizz_buzz function

def fizz_buzz(userno):
    #if useerno div by 3 then print "fizz"
    # If it is divisible by 5, it should return Buzz
    # If it is divisible by both 3 and 5, it should return FizzBuzz
    #Otherwise, it should return the same number
    numberStr = "kjj"
    if str.isdigit(userno):
        convertedNum = int(userno)
        if ((convertedNum % 3)==0) and ((convertedNum % 5)==0):
            numberStr = "FizzBuzz"
        elif ((convertedNum % 3)==0):
            numberStr = "fizz"
        elif ((convertedNum % 5)==0):
           numberStr = "Buzz"
        else:
           numberStr = userno


    return numberStr


userinput = input("Please Enter A Number: ")

returnedVal = fizz_buzz(userinput)


if (returnedVal=="kjj"):
  print("the number you entered was not a valid number")
else:
   print(returnedVal)

