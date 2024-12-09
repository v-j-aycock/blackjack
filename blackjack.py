import sys,random,time
def main():
    #card value dictionary
    cardVal = {"2♤" : 2,
                "2♡" : 2,
                "2♢" : 2,
                "2♧" : 2,
                "3♤" : 3,
                "3♡" : 3,
                "3♢" : 3,
                "3♧" : 3,
                "4♤" : 4,
                "4♡" : 4,
                "4♢" : 4,
                "4♧" : 4,
                "5♤" : 5,
                "5♡" : 5,
                "5♢" : 5,
                "5♧" : 5,
                "6♤" : 6,
                "6♡" : 6,
                "6♢" : 6,
                "6♧" : 6,
                "7♤" : 7,
                "7♡" : 7,
                "7♢" : 7,
                "7♧" : 7,
                "8♤" : 8,
                "8♡" : 8,
                "8♢" : 8,
                "8♧" : 8,
                "9♤" : 9,
                "9♡" : 9,
                "9♢" : 9,
                "9♧" : 9,
                "10♤" : 10,
                "10♡" : 10,
                "10♢" : 10,
                "10♧" : 10,
                "J♤" : 10,
                "J♡" : 10,
                "J♢" : 10,
                "J♧" : 10,
                "Q♤" : 10,
                "Q♡" : 10,
                "Q♢" : 10,
                "Q♧" : 10,
                "K♤" : 10,
                "K♡" : 10,
                "K♢" : 10,
                "K♧" : 10,
                "A♤" : 11,
                "A♡" : 11,
                "A♢" : 11,
                "A♧" : 11}
    #full deck
    deck = ["2♤",
            "2♡",
            "2♢",
            "2♧",
            "3♤",
            "3♡",
            "3♢",
            "3♧",
            "4♤",
            "4♡",
            "4♢",
            "4♧",
            "5♤",
            "5♡",
            "5♢",
            "5♧",
            "6♤",
            "6♡",
            "6♢",
            "6♧",
            "7♤",
            "7♡",
            "7♢",
            "7♧",
            "8♤",
            "8♡",
            "8♢",
            "8♧",
            "9♤",
            "9♡",
            "9♢",
            "9♧",
            "10♤",
            "10♡",
            "10♢",
            "10♧",
            "J♤",
            "J♡",
            "J♢",
            "J♧",
            "Q♤",
            "Q♡",
            "Q♢",
            "Q♧",
            "K♤",
            "K♡",
            "K♢",
            "K♧",
            "A♤",
            "A♡",
            "A♢",
            "A♧"]
    #we use this for ace 11-1
    aces = ["A♤",
            "A♡",
            "A♢",
            "A♧"]
    #we use this in randint to "shuffle"
    deckSize = 51
    #we use this for initial deals and to break ties
    playerHandSize = 0
    dealerHandSize = 0
    playerHand = []
    dealerHand = []
    #double down variable
    dD = False
    initialDeal(playerHandSize,deckSize,deck,playerHand,dealerHandSize,dealerHand)
    #now we check card values for blackjack
    playerHandVal = 0
    dealerHandVal = 0
    for item in playerHand:
        playerHandVal = playerHandVal + cardVal[item]
    for item in dealerHand:
        dealerHandVal = dealerHandVal + cardVal[item]
    if dealerHandVal == 21 and playerHandVal == 21:
        print('Double blackjack! Tie!')
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    if playerHandVal == 21 and dealerHandVal != 21:
        print("PLAYER BLACKJACK! YOU WIN!")
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    if dealerHandVal == 21 and playerHandVal !=21:
        print("Dealer blackjack. You lose.")
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    else:
        whatDo(playerHand,cardVal,playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,dealerHandSize)#,aces)




    

#what it says on the tin, give two cards to player and dealer, show hand, and 1 dealer card
def initialDeal(playerHandSize,deckSize,deck,playerHand,dealerHandSize,dealerHand):
    for x in range(2):
        deal = random.randint(0,deckSize)
        playerHand.append(deck[deal]) 
        del deck[deal]
        playerHandSize+=1
        deckSize-=1
    for x in range(2):
        deal = random.randint(0,deckSize)
        dealerHand.append(deck[deal]) 
        del deck[deal]
        dealerHandSize+=1
        deckSize-=1
    print(f'Your cards are {playerHand}')
    print(f'The dealer is showing {str(dealerHand[1])}') 

#asks what you want to do
def whatDo(playerHand,cardVal,playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,dealerHandSize):#,aces):
    print("Would you like to (H)it, (S)tand, (D)ouble down, or (F)old?")
    decision = input ()
    if decision == 'h':
        hit(playerHandVal,playerHandSize,deckSize,deck,playerHand,cardVal)#,aces)
    if decision == "s":
        stand(playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,dealerHandSize,cardVal)#,aces)
    if decision =='d':
        doubleDown()
    if decision == 'f':
        print("You lose.")
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()

#add card to hand, check value to see if bust or 21
def hit (playerHandVal,playerHandSize,deckSize,deck,playerHand,cardVal,dealerHand,dealerHandVal,dealerHandSize):#,aces):
    deal = random.randint(0,deckSize)
    playerHand.append(deck[deal])
    del deck[deal]
    playerHandSize+=1
    deckSize-=1
    print(f'Your cards are {playerHand}')
    playerHandVal = 0
    for item in playerHand:
        playerHandVal = playerHandVal + cardVal[item]
    if playerHandVal > 21:
        #if any(aces) in playerHand:
            #playerHandVal=-10
            #whatDo()
        print('Bust.')
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    if playerHandVal == 21:
        stand(playerHandSize,playerHandVal,deckSize,deck,cardVal,dealerHand,dealerHandVal,dealerHandSize)
    else:
        whatDo(playerHand,cardVal,playerHandVal,playerHandSize,deckSize,deck)#,aces)

#dealers turn
def stand(playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,cardVal,dealerHandSize):#s,aces):
    dealerHandVal = 0
    for x in dealerHand:
        dealerHandVal = dealerHandVal + cardVal[x]
    if dealerHandVal >= 17:
        endGame(playerHandVal,playerHandSize,dealerHandVal,dealerHandSize)
    else:
        deal = random.randint(0,deckSize) 
        dealerHand.append(deck[deal])
        dealerHandSize+=1
        deckSize-=1
        stand(playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,cardVal,dealerHandSize)#,aces)

def doubleDown(playerHand,playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,cardVal,dealerHandSize,dD,):#aces):
    dD = True
    deal = random.randint(0,deckSize)
    playerHand.append(deck[deal])
    del deck[deal]
    playerHandSize+=1
    deckSize-=1
    print(f'Your cards are {playerHand}')
    playerHandVal = 0
    for item in playerHand:
        playerHandVal = playerHandVal + cardVal[item]
    if playerHandVal > 21:
        if aces in playerHand:
            playerHandVal=-10
            whatDo()
        print('Bust.')
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    else:
        stand(playerHandVal,playerHandSize,deckSize,deck,dealerHand,dealerHandVal,cardVal,dealerHandSize)#,aces)

#checks hands against eachother
def endGame(playerHandVal,playerHandSize,dealerHandVal,dealerHandSize,dD):
    if playerHandVal > dealerHandVal:
        if dD == True:
            print('Double down win!')
        else:    
            print('You win!')
        print('Play again? Y/N')
        replay = input()
        if replay == 'y':
            main()
    if playerHandVal == dealerHandVal:
        if playerHandSize < dealerHandSize:
            if dD == True:
                print('Double down win!')
            else:    
                print('You win!')
            replay = input()
            if replay == 'y':
                main()
        if playerHandSize > dealerHandSize:
            if dD == True:
                print('Double down loss.')
            else:    
                print ('You lose.')
            print('Play again? Y/N')
            replay = input()
            if replay == 'y':
                main()
        if dealerHandVal > playerHandVal:
            if dD == True:
                print('Double down loss.')
            else:    
                print ('You lose.')
            print('Play again? Y/N')
            replay = input()
            if replay == 'y':
                main()







main()