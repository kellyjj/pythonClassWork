#kelly jaramillo, 8-31-2020 fcc python class learnTogether Week 5 learn together code, step 2
#this is a snippet of how I intend to use lists in my dev 0 project.

#for my dev0 project, I intend to write a black jack game (or a somethign similar.)
#since black jack is a card game,  we need a deck.  this is exactly where lists would come into play
# I will use the append method of a random number to put a number into my array
#the number will be be betwwen 2 and 11.  before the append, I will check to see if the number generated
#has been found in my deck 4 times.  

#note, this code doesn't really work, but is gooed enough for my concept.
import random

mydeck = [random.randint(2,12)]  #seed the deck.
print(mydeck)

while len(mydeck)<52:
    newcard = random.randint(2,11)
    if (mydeck.count(newcard)<4):
        mydeck.append(newcard)

print(mydeck)
