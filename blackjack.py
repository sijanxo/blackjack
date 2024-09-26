from blackjack_helper import *

# User 
user_hand = draw_starting_hand("YOUR")
user_stand = False
while user_hand < 21 and not user_stand == True:
  stand_prompt = input(f"You have {user_hand}. Hit (y/n)? ")
  if stand_prompt.lower() == "n":
    user_stand = True
  elif stand_prompt.lower() == "y":
    user_hand += draw_card()
  else:
    print("Sorry I didn't get that.")

print_end_turn_status(user_hand)

# Dealer
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  dealer_hand += draw_card()

print_end_turn_status(dealer_hand)

# Game Result
print_end_game_status(user_hand, dealer_hand)
