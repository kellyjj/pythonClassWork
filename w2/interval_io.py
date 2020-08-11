#kelly jaramillo, 8-11-2020 fcc python class learnTogether Week 2 code

#take 2 inputs from user, a starting & ending value (integer) 
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
    #we are adding a +1 here so that we will get last number.  could have done this with a while or do while loop
    for x in range(starting_val_int,ending_val_int+1):
        print(str(x))

