from random import randint

def game_start():
  players = {} #player_name: {score: 3, hand: 0}
  num = 0
  while num <= 0:
    num = int(input("Welcome to Blackjack! How many players? "))
  for i in range(num):
    name = input(f"Player {i+1}: ")
    players[name] = {"score": 3, "hand": 0}
  return players


def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

def draw_starting_hand(name):
  print_header(name.upper() + '\'S TURN')
  return draw_card() + draw_card()


def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')

  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')


def print_end_game_status(user, user_hand, dealer_hand, score):
  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print(f"{user} wins! Score: {score+1}")
    return score + 1
  elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
    print(f"{user} loses! Score: {score-1}")
    return score - 1
  else:
    print(f"{user} pushes. Score: {score}")
    return score
