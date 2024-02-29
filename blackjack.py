import random

class Cards():
    total_cards = 52

    def __init__(self):
        self.player = []
        self.hands= {'player': [], 'dealer': []}
        self.suits = {}
        self.deck = []

    def deal_cards(self):
        if not self.suits:
            self.suits = {'Clubs': 13,
                        'Diamonds': 13,
                        'Hearts': 13,
                        'Spades': 13}
        suits = self.suits.keys()
        tiers = ['2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for tier in tiers:
                card = {'tiers': tier, 'suit': suit}
                self.deck.append(card)

        random.shuffle(self.deck)
        self.hands['player'] = self.deck[:2]
        self.hands['dealer'] = self.deck[2:4]
        print(f'Your hand is: ')
        for card in self.hands['player']:
            print(f'{card['tiers']} of {card['suit']}')
        print(f'My hand is: {self.hands['dealer'][0]['tiers']} of {self.hands['dealer'][0]['suit']}')
        
    def hit_cards(self):
        if len(self.hands['player']) < 5:
            leftover_deck = [card for card in self.deck if card not in self.hands['player']]
            card = random.choice(leftover_deck)
            self.hands['player'].append(card)
            print(f'You receievd: {card['tiers']} of {card['suit']}')
        else: 
            print("You have been busted.")
        if len(self.hands['dealer']) < 5:
            leftover_deck = [card for card in self.deck if card not in self.hands['dealer']]
            card = random.choice(leftover_deck)
            self.hands['dealer'].append(card)
        else: 
            print("I have busted.")

    def black_jack(self):
        has_ace = False
        has_10 = False
        for card in self.hands['player']:
            if card['tiers'] == 'Ace':
                has_ace = True
            if card['tiers'] in ['10', 'Jack', 'Queen', 'King']:
                has_10 = True
        if has_ace and has_10:
                print('Blackjack!')
                print('You cheated, rematch!')

    def stand_compare(self):
            stand = input('You sure you want to stand?: (y/n)')
            if stand.lower() == 'y':
                player_sum = sum(int(card['tiers']) if card['tiers'].isdigit() else 10 for card in self.hands['player'])
                dealer_sum = sum(int(card['tiers']) if card['tiers'].isdigit() else 10 for card in self.hands['player'])
                print(f'My hand: ')
                for card in self.hands['dealer']:
                    print(f"{card['tiers']} of {card['suit']}")
                print('\nYour hand: ')
                for card in self.hands['player']:
                    print(f"{card['tiers']} of {card['suit']}")
                print('\n')
                print(f'Your hand total: {player_sum}')
                print(f'My hand total: {dealer_sum}')
                if player_sum > dealer_sum:
                    print('You won! ')
                elif dealer_sum > player_sum:
                    print('I won! ')
                else:
                    print('Draw game.')



my_cards = Cards()

def PlayBlackJack():
    while True:
        i = input('Time to play blackjack! You ready?: (start/hit/stand): q to quit: ')
        if i.lower() == 'start':
            my_cards.deal_cards()
            my_cards.black_jack()
        elif i.lower() == 'hit':
            my_cards.hit_cards()
        elif i.lower() == 'stand':
            my_cards.stand_compare()
        elif i.lower() == 'q':
            my_cards.stand_compare()
            break
        else:
            print("GGs")

PlayBlackJack()