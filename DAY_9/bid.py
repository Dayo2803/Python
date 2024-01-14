from art import logo
# from replit import clear
print(logo)


bid_dict = {}

print(bid_dict)

bid_ends = False

winner = ""

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_ends:
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    other_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bid == "no":
        bid_ends = True
        find_highest_bidder(bid_dict)
    
