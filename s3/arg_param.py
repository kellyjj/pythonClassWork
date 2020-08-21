#kelly jaramillo, 8-11-2020 fcc python class learnTogether Week 3 code, step 2
#this is for week 3 step 3.  we need to demostrate our understanding of arguments,
#parameters and default parameters.  so this will be a little bit of a game of black jack.

import random

def checkifCardTotalisBust(cardTotal):
        
    return (cardTotal>21)

def GetCardValue():
    return random.randint(1,22)

def SetBet(betamt, DefaultBet=5):
    #this is to show I understand default arguments
    if (betamt==0):
        return DefaultBet
    else:
        return betamt
 

#global vars
playerpot = 100
keepplaying = "Y"
playerbet = 0
dealercardtotal = 0
playercardtotal = 0

while (playerpot>0 and keepplaying.upper()=="Y"):
    tempbet = input("Please Enter your Bet {if you input 0, you will default to 5}: ")
    playerbet = int(tempbet)
    playerbet = SetBet(playerbet)

    if (playerbet >playerpot):
        print("you do not have enough for that bet")
        continue

    playercardtotal =0
    tempcard = GetCardValue()
    playercardtotal =playercardtotal+tempcard

    print("you have "+str(playercardtotal)+" !")
 

    if (not checkifCardTotalisBust(playercardtotal)):
        hitme = input("Do you want a hit: ")
        while (hitme.upper()=="Y" ):
            tempcard = GetCardValue()
            playercardtotal =playercardtotal+tempcard
            print("You now have "+str(playercardtotal))
            if (checkifCardTotalisBust(playercardtotal)):
                print("you lose")
                playercardtotal = 0
                break
            print("you have "+str(playercardtotal))
            hitme = input("Do you want to hit  : ")
    
    dealercardtotal = GetCardValue()
    print("The Dealer got "+str(dealercardtotal))
    if (dealercardtotal >= playercardtotal):
        print("you have lost. Oh discordia. ")
        playerpot = playerpot - playerbet
        if (playerpot <=0):
            print("you are sooooo broke.  we are sending some gentlemen to talk with you...")
    else:
        print("YOU WON.  you have brought glory to the empire")
        playerpot = playerpot + (playerbet *2 )
    print("you now have "+str(playerpot))

    keepplaying = input("Do you want another turn: ")

    

