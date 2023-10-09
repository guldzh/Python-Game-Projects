from art import logo
import os

print(logo)
bids={}
want_to_bid=True

def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
      bid_amount=bidding_record[bidder]
      if bid_amount>highest_bid:
         highest_bid=bid_amount
         winner=bidder
    print(f"The Winner is {winner} with bid of ${highest_bid}")       

while want_to_bid:
  name=input("What is your name?: ")
  bid_price=int(input("What is your bid?: $"))
  bids[name]=bid_price
  ask_user=input("Are there any other people who wants to bid? 'yes' or 'no' ")
  if ask_user=="no":
     want_to_bid=False
     find_highest_bidder(bids)
  elif ask_user=="yes":     
    os.system('clear')
  
        