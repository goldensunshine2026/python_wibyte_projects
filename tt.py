import csv
import random

with open('cricket.csv', mode='r') as file:
  csvFile = csv.DictReader(file)
  all_cards = list(csvFile)


print("Welcome to the Top Trumps Game, Cricket theme")
print('Make your choices wisely and try to win all the cards')
print('Click Enter to begin')

input()


def display_card(card):
  max_chars = 0

  for keys in card:
    if len(keys) > max_chars:
      max_chars = len(keys)

  for keys in card:
    print(keys, (max_chars-len(keys))*' ', ': ', card[keys])


def determine_winner(m1, m2, order=1):
  dct = {'player': m1, 'computer': m2}
  v = list(dct.values())
  k = list(dct.keys())

  if m1 == m2:
    return 'draw'
  else:
    if order == 1:
      return k[v.index(max(v))]
    else:
      return k[v.index(min(v))]


random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False
chance = 'player'


relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]

mapping_dict = {}

for key in relevant_keys:
  mapping_dict[key[0].upper()] = key


input()


while not game_over:

  print('Player cards: ', len(player_cards), 'Computer cards: ', len(comput_cards), 'Table cards: ', len(table_cards))

  player = player_cards.pop(0)
  comput = comput_cards.pop(0)

  table_cards.append(player)
  table_cards.append(comput)

  print()
  print(f'It is now {chance}\'s chance')
  print()

  print('Your (Player) card is ')
  display_card(player)
  print()

  if chance == 'player':

    print('Choose one of these attributes:')

    for short_key, long_key in mapping_dict.items():
      print(short_key, '=', long_key)

    chosen_key = input('What is your choice?').upper()

    while chosen_key not in mapping_dict:
      print('Invalid choice. Please choose one of the available attributes.')
      chosen_key = input('What is your choice?').upper()

    chance = 'computer'

  else:

    chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'player'

  key_requested = mapping_dict[chosen_key]

  value_player = player[key_requested]
  value_comput = comput[key_requested]

  print('Key of interest is ', key_requested)

  winner = determine_winner(float(value_player), float(value_comput))

  print('Player ', key_requested, 'is', value_player)
  print('Computer ', key_requested, 'is', value_comput)

  print()
  print('Winner is ... ', winner)

  input()

  if winner == 'player':
    player_cards.extend(table_cards)
    table_cards.clear()

  elif winner == 'computer':
    comput_cards.extend(table_cards)
    table_cards.clear()

  if len(player_cards) == 0:
    print('Computer Won')
    game_over = True

  elif len(comput_cards) == 0:
    print('Player Won')
    game_over = True