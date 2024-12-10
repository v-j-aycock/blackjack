import sys,random,time

#we use this in randint to "shuffle"
deckSize = 51
#hand lists
playerHand = []
playerHandDisplay = []
dealerHand = []
dealerHandDisplay = []
#double down variable
dD = False

def setup():
    playerHand = []
    playerHandDisplay = []
    dealerHand = []
    dealerHandDisplay = []
    dD = False
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
            "T♤",
            "T♡",
            "T♢",
            "T♧",
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
    main(deck)

def main(deck):
    if len(deck) <= 13:
        print('Not enough cards! \n Reshuffling...')
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
        "T♤",
        "T♡",
        "T♢",
        "T♧",
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
    initialDeal(deck)
    whatDo(deck)

def getPlayerHandVal():
    playerHandFun=playerHand
    for i in range(len(playerHandFun)):
        try: 
            if len(playerHandFun[i]) == 2:
                playerHandFun[i] = playerHandFun[i].replace("♤",'')
                playerHandFun[i] = playerHandFun[i].replace("♡",'')
                playerHandFun[i] = playerHandFun[i].replace("♢",'')
                playerHandFun[i] = playerHandFun[i].replace("♧",'')
                playerHandFun[i] = playerHandFun[i].replace('T','10')
                playerHandFun[i] = playerHandFun[i].replace('J','10')
                playerHandFun[i] = playerHandFun[i].replace('Q','10')
                playerHandFun[i] = playerHandFun[i].replace('K','10')
                playerHandFun[i] = playerHandFun[i].replace("A",'11')
        except:
            1+1
    for i in range(len(playerHandFun)):
        playerHandFun[i] = int(playerHandFun[i])
    if sum(playerHandFun) > 21:
        for i in range(len(playerHandFun)):
            if playerHandFun[i] == 11:
                playerHandFun.remove(playerHandFun[i])
                playerHandFun.append(1)
    for i in range(len(playerHandFun)):
        playerHandFun[i] = int(playerHandFun[i])
    return sum(playerHandFun)

def getDealerHandVal():
    dealerHandFun = dealerHand
    for i in range(len(dealerHandFun)):
        try:
            if len(dealerHandFun[i]) == 2:
                dealerHandFun[i] = dealerHandFun[i].replace("♤",'')
                dealerHandFun[i] = dealerHandFun[i].replace("♡",'')
                dealerHandFun[i] = dealerHandFun[i].replace("♢",'')
                dealerHandFun[i] = dealerHandFun[i].replace("♧",'')
                dealerHandFun[i] = dealerHandFun[i].replace("T",'10')
                dealerHandFun[i] = dealerHandFun[i].replace('J','10')
                dealerHandFun[i] = dealerHandFun[i].replace('Q','10')
                dealerHandFun[i] = dealerHandFun[i].replace('K','10')
                dealerHandFun[i] = dealerHandFun[i].replace("A",'11')
        except:
            1+1
    for i in range(len(dealerHandFun)):
        dealerHandFun[i] = int(dealerHandFun[i])
    if sum(dealerHandFun) > 21:
        for i in range(len(dealerHandFun)):
            if dealerHandFun[i] == 11:
                dealerHandFun.remove(dealerHandFun[i])
                dealerHandFun.append(1)
    for i in range(len(dealerHandFun)):
        dealerHandFun[i] = int(dealerHandFun[i])
    return sum(dealerHandFun)

#what it says on the tin, give two cards to player and dealer, show hand, and 1 dealer card
def initialDeal(deck):
    for x in range(2):
        deal = random.randint(0,(len(deck)-1))
        playerHand.append(deck[deal]) 
        playerHandDisplay.append(deck[deal]) 
        deck.remove(deck[deal])
    for x in range(2):
        deal = random.randint(0,(len(deck)-1))
        dealerHand.append(deck[deal]) 
        dealerHandDisplay.append(deck[deal]) 
        deck.remove(deck[deal])
    print(f'Your cards are {(playerHandDisplay)}')
    print(f'The dealer is showing {str(dealerHandDisplay[1])}') 
    #now we check card values for blackjack
    playerHandVal = getPlayerHandVal()
    dealerHandVal = getDealerHandVal()
    if dealerHandVal == 21 and playerHandVal == 21:
        print('Double blackjack! Tie!')
        replay(deck)
    if playerHandVal == 21 and dealerHandVal != 21:
        print("PLAYER BLACKJACK! YOU WIN!")
        replay(deck)
    if dealerHandVal == 21 and playerHandVal !=21:
        print(f"Dealer blackjack with {dealerHandDisplay} You lose.")
        replay(deck)

#asks what you want to do
def whatDo(deck):
    print("Would you like to (h)it, (s)tand, (d)ouble down, or (f)old?")
    decision = input ()
    if decision == 'h':
        hit(deck)
    if decision == "s":
        stand(deck,dD)
    if decision =='d':
        doubleDown(deck)
    if decision == 'f':
        print("You lose.")
        replay(deck)
    else:
        print('Invalid input')
        whatDo(deck)

#add card to hand, check value to see if bust or 21
def hit (deck):
    deal = random.randint(0,(len(deck)-1))
    playerHand.append(deck[deal])
    playerHandDisplay.append(deck[deal])
    deck.remove(deck[deal])
    print(f'Your cards are {playerHandDisplay}')
    playerHandVal = getPlayerHandVal()
    if playerHandVal > 21:
        print('Bust.')
        replay(deck)   
    if playerHandVal == 21:
        print('You have 21')
        stand(deck,dD)
    else:
        whatDo(deck)

#dealers turn
def stand(deck,dD):
    print(f'Dealer reveals {dealerHandDisplay}')
    dealerHandVal = getDealerHandVal()
    if dealerHandVal > 21:
        time.sleep(1)
        if dD == True:
            print('Dealer bust! Double down win!')
        else:
            print("Dealer bust! You win.")
        replay(deck)
    if dealerHandVal >= 17:
        endGame(deck,dD)
    else:
        deal = random.randint(0,(len(deck)-1)) 
        dealerHand.append(deck[deal])
        dealerHandDisplay.append(deck[deal])
        deck.remove(deck[deal])
        time.sleep(1)
        stand(deck,dD)

def doubleDown(deck):
    dD = True
    deal = random.randint(0,(len(deck)-1))
    playerHand.append(deck[deal])
    playerHandDisplay.append(deck[deal])
    deck.remove(deck[deal])
    print(f'Your cards are {playerHandDisplay}')
    playerHandVal = getPlayerHandVal()
    if playerHandVal > 21:
        print('Double Down bust.')
        replay(deck)
    else:
        stand(deck,dD)

#checks hands against eachother
def endGame(deck,dD):
    playerHandVal = getPlayerHandVal()
    dealerHandVal = getDealerHandVal()
    if playerHandVal > dealerHandVal:
        if dD == True:
            print('Double down win!')
        else:    
            print('You win!')
        replay(deck)
            

    if playerHandVal == dealerHandVal:
        if len(playerHand) < len(dealerHand):
            if dD == True:
                print('Double down win!')
            else:    
                print('You win!')
            replay(deck)
        if len(playerHand) > len(dealerHand):
            if dD == True:
                print('Double down loss.')
            else:    
                print ('You lose.')
            replay(deck)
    if dealerHandVal > playerHandVal:
        if dD == True:
            print('Double down loss.')
        else:    
            print ('You lose.')
        replay(deck)


def replay(deck):
    print('Play again? Y/N')
    decision = input()
    if decision == 'y':
        dealerHand.clear()
        dealerHandDisplay.clear()
        playerHand.clear()
        playerHandDisplay.clear()
        main(deck)
    elif decision == 'n':
        sys.exit()
    else:
        print('Invalid input')
        replay(deck)
        




setup()