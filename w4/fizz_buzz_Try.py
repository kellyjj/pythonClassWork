#kelly jaramillo, 8-27-2020 fcc python class learnTogether Week 4 learn together code, step 1
#kjj 8-27-20 we will refactor this to include some try/catch in our code.  everything else will stay the same
#this will use a funciton called fizz_buzz.  
#we will get input from our user.  send that input to the fizz_buzz function

def fizz_buzz(userno):
    #if useerno div by 3 then print "fizz"
    # If it is divisible by 5, it should return Buzz
    # If it is divisible by both 3 and 5, it should return FizzBuzz
    #Otherwise, it should return the same number
    #adding some try/except blocks to this method.

    numberStr = "kjj"
    try:
        convertedNum = int(userno)
        if (convertedNum <=0):
            raise ValueError("Error: You entered a negitive number ")

        if ((convertedNum % 3)==0) and ((convertedNum % 5)==0):
            numberStr = "FizzBuzz"
        elif ((convertedNum % 3)==0):
            numberStr = "fizz"
        elif ((convertedNum % 5)==0):
            numberStr = "Buzz"
        else:
            numberStr = userno

    except ValueError as vex:
        print(repr(vex))
    except Exception as ex:
        print("Undefined Error :"+repr(ex))

    return numberStr


userinput = input("Please Enter A Number: ")

returnedVal = fizz_buzz(userinput)


if (returnedVal=="kjj"):
  print("the number you entered was not a valid for this")
else:
   print(returnedVal)

