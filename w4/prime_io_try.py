#kelly jaramillo, 8-11-2020 fcc python class learnTogether Week 4 code, step 1
#kjj 8-27-20 we will refactor this to include some try/catch in our code.  everything else will stay the same

#take 2 inputs from user, a starting & ending value (integer) 
try:
    print("Please enter a starting value ")
    starting_val_str = input()
    starting_val_int = int(starting_val_str)  #lets convert our str to int

    print("Please Enter a ending value ")
    ending_val_str = input()
    ending_val_int = int(ending_val_str)  #lets convert our str to int
    print( " ------------------------------- ")

    #the values cant equal each other, and the starting should be smaller
    if (starting_val_int >=ending_val_int):
        print("your starting value is larger or equal to your ending value.  Nothing else will happen")
    else:
        print("the prime numbers from your inputs are...")
        #we are adding a +1 here so that we will get last number.  could have done this with a while or do while loop
        for x in range(starting_val_int,ending_val_int+1):
            #a prime number is any number that is evenly divided by itself and 1 only.  so for
            #example,  5 is prime since you get no reminder after you divide. but 6 is not prime
            #since we can divid it evenly with 1, 2, 3, and 6.
            #to do this, we will skip over checking if x is in  [1,2,3,5,7], since we know all these are 
            #prime.  after 7,  we will mod by these 5 numbers. 
            
            isPrime = True
            if (x not in [1,2,3,5,7]):
                isPrime = (x % 2)!=0 and (x % 3)!=0 and (x % 5)!=0 and (x % 7)!=0
        
            if (isPrime):
                print(str(x)+" is a prime number")


except Exception as ex:
    print(repr(ex))
else:
    print(" ")
    print("Doing Clean up")
finally:
    print(" ")
    print("Find prime Try Catch edition Complete")

  
