import os

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"🎉 Drumroll please... 🥁\nThe winner is {winner} with a whopping bid of ${highest_bid}!\n🎊 Congratulations, {winner}! 🎊")

def clear():
    # Clear the console (works for Windows, Mac, and Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

while not bidding_finished:
    name = input("What is your name, brave bidder? 🏷️: ")
    try:
        price = int(input(f"Alright, {name}, what is your bid? 💰 $"))
        if price < 0:
            print("Nice try, but bids can't be negative! 😜")
            continue
    except ValueError:
        print("That's not a number! Please enter a valid bid amount. 📉")
        continue
    bids[name] = price
    should_continue = input("Are there any other bidders? (yes, no, default yes). 📝\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes" or should_continue == "":
        clear()
        print("Onward to the next bidder! 🏇")
    else:
        print("I'll take that as a 'yes'! Onward to the next bidder! 🏇")
        clear()

