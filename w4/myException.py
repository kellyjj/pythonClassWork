#kelly jaramillo, 8-11-2020 fcc python class learnTogether Week 4 code, step 2
#for this, I have to pick a exception to try.  for my pick, I am going to do both
#a generic exception, and a arithmic exception

try:
    mynumstr = input("Please input a number  ")
    mynum = int(mynumstr)
    mynum = mynum / 0
except ArithmeticError as mathex:
    print("A divide by zero error "+repr(mathex))
except Exception as ex:
    print("Unknown Error "+repr(ex))
finally:
    print("why are we dividing by zero")