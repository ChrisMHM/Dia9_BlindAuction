import os
import art

biddersList = []
again = True

# Clearing the Screen
def clear():
    os.system('cls')

def addBidders(name, bid):
    bidder = {
        "name": name,
        "bid": bid
    }

    biddersList.append(bidder)

def findWinner():
    winnerBid = 0
    winnerName = ""
    participantName = ""
    participantBid = 0
    bids = []

    for bidderParticipant in biddersList:
        participantName = bidderParticipant["name"]
        participantBid = bidderParticipant["bid"]

        if winnerBid < participantBid:
            winnerBid = participantBid
            winnerName = participantName
        
        bids.append(participantBid)

    clear()
    print(f"The winner is {winnerName} with a bid of ${winnerBid}")


print(art.logo)
print("Welcome to the secret auction program. ")

while again:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    addBidders(name, bid)

    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if otherBidders == "yes":
        clear()
    else:
        findWinner()
        again = False