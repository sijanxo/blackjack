from blackjack_helper import *

#Game Starts here 
players = game_start()
while True:
  # USER'S TURN
  for player in players:
    #user_hand = players[player]["hand"]
    players[player]["hand"] = draw_starting_hand(player)
    should_hit = 'y'
    while players[player]["hand"] < 21:
      should_hit = input(f"You have {players[player]['hand']}. Hit (y/n)? ")
      if should_hit == 'n':
        break
      elif should_hit != 'y':
        print("Sorry I didn't get that.")
      else:
        players[player]["hand"] = players[player]["hand"] + draw_card()
    print_end_turn_status(players[player]["hand"])
    
  # DEALER'S TURN
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)

  # GAME RESULT
  new_players = {}
  print_header('GAME RESULT')
  for player_name, player in players.items():
    player["score"] = print_end_game_status(player_name, player["hand"], dealer_hand, player["score"])
    if player["score"] == 0:
      print(f"{player_name} eliminated!")
    else:
      new_players[player_name] = player

  players = new_players
  if players == {}:
    print("All players eliminated!")
    break
    
  play_again = input("Do you want to play another hand (y/n)? ")
  if play_again == "y":
    pass
  elif play_again == "n":
    break
  
