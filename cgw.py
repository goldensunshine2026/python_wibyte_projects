import random
import time



cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']             
suits = ['C', 'D', 'H', 'S']  

deck_of_cards = []; 

for kk in range(len(suits)):
    for jj in range(len(cards)):
        deck_of_cards.append(suits[kk]+cards[jj])


print('Unshuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')
print()

random.shuffle(deck_of_cards) 

print('Shuffled Deck:')
for kk in range(len(deck_of_cards)):
    print(deck_of_cards[kk], end = ' ')

toss_cards = random.sample(deck_of_cards, 3)
print()
print("Toss cards are:", toss_cards[0], toss_cards[1], toss_cards[2])

toss_sum = 0
for card in toss_cards:
    toss_sum = toss_sum + cards.index(card[1]) + 2

print("Toss sum =", toss_sum)

if toss_sum % 2 == 0:
    first_mover = 'player'
    print('You won the toss, you will play first.')
else:
    first_mover = 'computer'
    print('Computer won the toss, it will play first')

player_cards = deck_of_cards[0:26:1]
comput_cards = deck_of_cards[26:52:1]
table_cards = []

player_cards.sort(key=lambda x: (cards.index(x[1]), suits.index(x[0]))) 

move_complete = False
game_complete = False
moves_played = 0


def show_player_cards(player_cards):
    print()
    print("Your cards are:")
    for ii in range(len(player_cards)):
        print(str(ii+1) + ":" + player_cards[ii], end='   ')
    print()


def choose_player_card(player_cards, message):
    show_player_cards(player_cards)

    while True:
        choice = input(message)

        if choice.isdigit():
            choice = int(choice) - 1
            if choice >= 0 and choice < len(player_cards):
                return player_cards.pop(choice)

        print("Invalid choice. Try again.")


print()
print("========== GAME START ==========")
input("Press Enter to begin...")

while not(game_complete):
  
  move_complete = False
  
  if len(player_cards)<1 or len(comput_cards)<1:
    move_complete = True
    game_complete = True
  
  while not(move_complete):
    print()
    print("Player Cards:", len(player_cards), "Computer Cards:", len(comput_cards), "Table Cards:", len(table_cards))

    card_p = choose_player_card(player_cards, "Choose a card number to play: ")

    comp_index = random.randint(0, len(comput_cards)-1)
    card_c = comput_cards.pop(comp_index)

    print()
    print('Player Card is ...', card_p)
    print('Computer Card is ...', card_c)
    

    table_cards.append(card_p)
    table_cards.append(card_c)
    
    if cards.index(card_p[1])>cards.index(card_c[1]):
      print('Player Wins ... ')
      input("Press Enter to continue...")
      player_cards.extend(table_cards)
      table_cards.clear()

      player_cards.sort(key=lambda x: (cards.index(x[1]), suits.index(x[0])))

      move_complete = True
      moves_played = moves_played + 1

    elif cards.index(card_p[1])<cards.index(card_c[1]):
      print('Computer Wins ... ')
      input("Press Enter to continue...")
      comput_cards.extend(table_cards)
      table_cards.clear()
      move_complete = True
      moves_played = moves_played + 1

    else:

      print("WAR begins")
      input("Press Enter to continue...")

      if len(player_cards)<4 or len(comput_cards)<4:
        print("Not enough cards to continue WAR.")
        move_complete = True
        game_complete = True

      else:
        print()
        print("Each side puts 3 cards face down.")

        for kk in range(3):
          war_card = choose_player_card(player_cards, "Choose face-down war card " + str(kk+1) + ": ")
          table_cards.append(war_card)

        for kk in range(3):
          comp_index = random.randint(0, len(comput_cards)-1)
          table_cards.append(comput_cards.pop(comp_index))

        print("Now choose the deciding WAR card.")

        war_player = choose_player_card(player_cards, "Choose your WAR card: ")

        comp_index = random.randint(0, len(comput_cards)-1)
        war_computer = comput_cards.pop(comp_index)

        print()
        print("Player WAR card is ...", war_player)
        print("Computer WAR card is ...", war_computer)

        table_cards.append(war_player)
        table_cards.append(war_computer)

        if cards.index(war_player[1]) > cards.index(war_computer[1]):
          print("Player Wins the WAR ... ")
          input("Press Enter to continue...")
          player_cards.extend(table_cards)
          table_cards.clear()

          player_cards.sort(key=lambda x: (cards.index(x[1]), suits.index(x[0])))

          move_complete = True
          moves_played = moves_played + 1

        elif cards.index(war_player[1]) < cards.index(war_computer[1]):
          print("Computer Wins the WAR ... ")
          input("Press Enter to continue...")
          comput_cards.extend(table_cards)
          table_cards.clear()
          move_complete = True
          moves_played = moves_played + 1

        else:
          print("WAR tied again. The battle continues...")
          input("Press Enter to continue...")

    if moves_played == 100:
      game_complete = True
		
    print("Player Cards:", len(player_cards), "Computer Cards:", len(comput_cards), "Table Cards:", len(table_cards))    


print()
print()

if len(player_cards) > len(comput_cards):
	print('PLAYER is the winner')
elif len(player_cards) < len(comput_cards):
	print('COMPUTER is the winner')
else:
	print('GAME drawn!')