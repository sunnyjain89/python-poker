#######################
#Sunny Jain
#Created on: March 31st, 2021
#Last modified on: March 31st, 2021
#This program will play a game of black jack (with some changes - see rules) with any number of users, using one deck of cards.
#######################



import sys #I will need to terminate my program mid way in some conditions

#----------------------------------------------------------------------#

#This is the portion in which I'll be storing all my functions

#The following function will make hands for each player and the dealer with the deck as the input.
def makeHands(x):
    hands = []
    print()
    print()
    #The next six lines add one card to the dealer's hand.
    tempList = []
    card = x.pop()
    tempList.append("Dealer")
    tempList.append(card)
    print(tempList)
    print()
    #The next 3 lines adds a card to the dealer's hand which the player will be unable to see
    card1 = x.pop()
    tempList.append(card1)
    hands.append(tempList)
    for i in range(1,numOfPlayers+1):
        hand = []
        #put the player name in
        hand.append("Player "+str(i))
        for j in range(1, 3):
            card = x.pop()
            hand.append(card)
        print(hand)
        print()
        hands.append(hand)
    return hands

#The following fucntion turns all occurances of number cards into integers, turns 'K','Q','J' into 10, and 'A' into 11
def changeValues(x):
    for y in x:
        for z in range (1, 3):
            if y[z][0] == "A":
                y[z][0] = 11
            if y[z][0] == "J":
                y[z][0] = 10
            if y[z][0] == "Q":
                y[z][0] = 10
            if y[z][0] == "K":
                y[z][0] = 10
            if (y[z][0] != "A") and (y[z][0] != "Q") and (y[z][0] != "K") and (y[z][0] != "J"):
                y[z][0] = int(y[z][0])
    return x

#The followig function takes in a player's hand and adds their values up
def countValues(playerHand):
    number = 0
    for x in range (1, len(playerHand)):
        number = number + playerHand [x][0]
    return number

#The following function takes in the player hand's total value, and checks if they got a black jack
def checkForBlackJack(number):
    if number == 21:
        return True
    else:
        return False

#The following function takes in the player hand's total value, and checks if they busted   
def checkForBust(number):
    if number > 21:
        return True
    else:
        return False


#The following function will add a card to payer's hand if they choose to hit
def addCard (playerNumber, allCards, allHands):
    card = allCards.pop()
    print()
    print("The new card is,", card)
    print()
    if card[0] == "A":
            card[0] = 11
    elif  card[0] == "J":
         card[0] = 10
    elif  card[0] == "Q":
         card[0] = 10
    elif  card[0] == "K":
         card[0] = 10
    else:
         card[0] = int(card[0])

    position = allHands[playerNumber]
    position.append(card)
    return allHands
    

#----------------------------------------------------------------------#


#----------------------------------------------------------------------#

#This portion is where I create the actual deck that I will be using
possibleSuits = ['clubs','diamonds','hearts','spades']
possibleValues = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

allCards = [] #This is the list in which I will be where i'm stroing the cards
for suits in possibleSuits:
    for values in possibleValues:
        allCards.append([values, suits])

import random
random.shuffle(allCards)
#I have now shuffled my cards, and my deck of cards is ready
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
#This is the portion where I write my actual code.

#The following introduces the program and check with the user whether they know how to play the game
print('Hello user.')
print()
print('This program will play a game of black jack with you, with the computer as the dealer.')
print()
printRules = (input("Would you like to see the rules? Please answer with 'yes' or 'no' "))
printRules = printRules.lower()
while True: #This portion performs a action based on input from the user.
    if printRules == 'yes':
        print("The goal of blackjack is to beat the dealer's (the computer's) hand without going over 21.")
        print("Face cards are worth 10. Aces are worth 11. All other cards are worth their face values.")
        print("Each player starts with two cards, one of the dealer's cards is hidden until the end.")
        print("Each player will be allowed to hit as many times as they want before the game moves onto the next player.")
        print("To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.")
        print("If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.")
        print("If you are dealt 21 from the start (Ace & 10), you got a blackjack.")
        print("Blackjack means that you instantly win the game.")
        print("Dealer will hit until his/her cards total 17 or higher.")
        print("If the dealer busts, the player(s) with the highest value(s) win(S).")
        print("If you get two of the same card, they will retain their values with no changes.")
        print("If a player's hand matches the dealer's hand, then the player still wins.")
        print("If everyone (including the dealer) busts, the dealer automatically wins.")
        #I decided not to include the ability to split or double down, since this game only lasts one round, and those rules apply more
        #to versions of blackjack with betting/points.
        print()
        print()
        break
    elif printRules == 'no':
        break
    else: #This is just here to make sure the user gives a valid answer and the program doesn't crash
        print()
        print('Please provide a valid answer')
        printRules = (input("Would you like to see the rules? Please answer with 'yes' or 'no'"))
        printRules = printRules.lower()
        continue
#


#The following section will ask the user(s) how many people are present in the game.
while True: #I'm using try and accept to make sure they provide a valid answer
    #The reason I used try and except instead of if and else is because I need a way to ensure that the answer is an integer without the program crashing
    try:
        print()
        numOfPlayers = int(input('How many players are playing? Please enter a number between 1 and 10 (Not including the dealer.) '))
        if (numOfPlayers <= 0) or (numOfPlayers >= 11): #This part is here to ensure that a valid number is provided
            print()
            print('Please enter a valid value')
            print()
            continue
        break
    
    except:
        print()
        print('Please enter a valid value (from 1 - 10)')
        print()
        continue
    else:
        break
#


#Now that I know how many people are playing, I will distribute cards to each person.
allHands = makeHands(allCards)

#Now that the cards are distributed, I will assign each card its value.
allHands = changeValues(allHands)

#Now I will ask each player if they want to hit or stay, after giving them them the value of their cards
endCheck = []#This is the list I will be using at the end of the game to determine the winner.
tempList = []#This is the list in which I will store player's names and points so that I can evaluate the winner at the end
for a in range (1, (numOfPlayers + 1)):
    print()
    tempHand = allHands[a]
    totalValue = str(countValues(tempHand))
    a = str(a)
    playerName = ("Player "+ a)
    print("Player " + a + ", the total value of your cards is", totalValue + ".")
    a = int(a)
    totalValue = int(totalValue)
    bjyn = checkForBlackJack(totalValue)
    byn = checkForBust(totalValue)
    if byn == True: #There is a one in two thousand seven hundred and four chance that the player gets two aces (busts on first try)
        print()
        print('You have busted. You lose the game.')
        print()
        continue
        
    if bjyn == True:
        print()
        print('You have gotten Black Jack! You win the game!')
        print()
        tempList = []
        tempList.append(playerName)
        tempList.append(totalValue)
        endCheck.append(tempList) #Here I am adding player names and points to a list so that I can evaluate a winner at the end
        continue
    #hitOrStay = input("Would you like to hit (add another card to your hand), or stay (move onto the next player)? Please type your answer: ")
    while True:
        print()
        hitOrStay = input("Would you like to hit (add another card to your hand), or stand (move onto the next player)? Please type your answer: ")
        if hitOrStay == 'hit' or hitOrStay == 'Hit':
            allHands = addCard(a, allCards, allHands)
            tempHand = (allHands[a])
            totalValue = (countValues(tempHand))
            #The next two lines turn 'a' and 'total value' into strings so that they can be concatonated into the statment.
            totalValue = str(totalValue)
            a = str(a)
            #The following line prints the statement
            print("Player " + a + ", the total value of your cards is", totalValue + ".")
            #The next two lines turn 'a' and 'totalValue' back into integers so that they can again be worked with
            a = int(a)
            totalValue = int(totalValue)
            print()
            if checkForBust(totalValue) == True:
                print()
                print('You have busted, and have lost the game')
                print()
                break     
            elif checkForBlackJack(totalValue) == True:
                print()
                print('You have gotten Black Jack! You win the game!')
                print()
                tempList = []
                tempList.append(playerName)
                tempList.append(totalValue)
                endCheck.append(tempList) #Here I am adding player names and points to a list so that I can evaluate a winner at the end
                break
            else:
                print()
                continue
            
        elif hitOrStay == 'stand' or hitOrStay == 'Stand':
            tempList = []
            tempList.append(playerName)
            tempList.append(totalValue)
            endCheck.append(tempList)
            break
        else:
           print()
           print("Invalid answer. Try again")
           print()
           continue
#In the next lines I will format the 'endCheck' list so that it is easier to work with
#I will do this by adding another list with just the values to the end. This makes the numbers easier to compare.
#I will then use the index of the desired numbers in that list, and apply them to the rest of the list to see who won
tempList = []
for d in endCheck:
    tempNum = d[1]
    tempList.append(tempNum)
endCheck.append(tempList) 

#Now that all the players have gone through their choices, I will reveal the dealer's hand.
while True: #I put this all into a while loop because the dealer may not have cards that add up to 17 or more. In that case I will need to loop until it does
    print("Let's see what the dealer has. ")
    dealerHand = allHands[0]
    dealerValue = countValues(dealerHand)
    print()
    print("The dealer's value is", dealerValue)
    if (dealerValue >= 17) and (dealerValue <= 21):
        print()
        print("The dealer's hand's value is above 16. The winners will be the ones who have total values that are higher than this number, while under 21.")
        print("The winner may also win if their values are equal to the dealer's")
        dealerValue = dealerValue
        dealerStatus = ("qualified")
        print()
        break
    elif (dealerValue <= 16):
        print()
        print('The dealer does not have enough cards. They will add another card to their hand')
        print()
        input("Press enter to continue.")
        allHands = addCard(0, allCards, allHands)
        print()
        continue
    elif dealerValue > 21:
        print()
        print("The dealer has busted and is out of the game.")
        print()
        print("The winner(s) will be the ones with the cards closes to 21, while still being under 21.")
        dealerStatus = "busted"
        print()
        input("Press enter to continue.")
        break
#

#Now that the dealer has revealed their cards, I will find a winner using the 'endCheck' list.
#There are different approaches to finding the winner based on it they bust or don't
#For these if statements, since 'endCheck' only included those under 21, my work is a little easier here. (won't have to check if over/under 21)

winnerList = []
lengthOfEndCheck = len(endCheck[0])
tempEndCheck = []
dealerValue = int(dealerValue)
case = "nothing"

while True: #This is to solve an error that came up
    try:
        for q in endCheck:
            randomVariable = (q[1])
    except:
        tempEndCheck.append(endCheck)
        endCheck = tempEndCheck
        case = "doubleList" #This is here to eliminate an error
        break
    break

if lengthOfEndCheck == 0:
    print("The dealer has won the game. ")
    input("Press enter to finish. ")
    sys.exit()

elif dealerStatus == ("qualified"):
    print()
    print()
    if case == "doubleList":     
        for g in endCheck:
            numberToCheck = g[0][1]
            if numberToCheck >= dealerValue:
                winnerList.append(g[0])
            else:
                continue
    else:
        for g in endCheck:
            numberToCheck = g[1]
            if numberToCheck >= dealerValue:
                winnerList.append(g)
            else:
                continue
    
elif dealerStatus == ("busted"):
    if case == "doubleList":
        print(endCheck[0][0], "is the winner.")
        sys.exit()
        
    else:
        lastTerm = endCheck[-1]
        temporaryList = lastTerm
        temporaryList = sorted(temporaryList)
        biggestValue = temporaryList[-1]
        for k in endCheck:
            numberToCheck = k[1]
            if numberToCheck == biggestValue:
                winnerList.append(k)
            else:
                continue

for h in winnerList: #This is just here to account for a possible mistake
    lengthOfLastTerm = len(h)
    if lengthOfLastTerm > 2:
        winnerList.remove(h)
    else:
        continue

lengthOfWinnerList = len(winnerList)
if lengthOfWinnerList == 0:
    print("The dealer has won the game.")
    
else:
    for u in winnerList:
        theWinningPlayer = u[0]
        theWinningPoint = u[1]
        print(theWinningPlayer, "has won the game with", theWinningPoint, "points!") #This puts the results into simple words
    
input("Thank you for playing! Press enter to finish. ")
#----------------------------------------------------------------------#



