import random

class Player():
    def __init__(self, name, budget) -> None:
        self.name = name
        self.budget = budget
        self.current_bet = 0

    def placeBet(self):
        while True:
            try:
                bet = float(input(f"{self.name}, enter your bet (Current budget: {self.budget} $): "))
                if 0 < bet <= self.budget:
                    self.current_bet = bet
                    break
                else:
                    print("Invalid bet amount! Please enter a valid amount within your budget.")
            except ValueError:
                print("Invalid input! Please enter a number.")

def start(players, cards, values):
    print("\n--- Welcome to Blackjack! ---\n")
    
    # Betting phase
    for player in players:
        print(f"\n{player.name}'s turn to place a bet:")
        print("=================================")
        player.placeBet()
        print(f"{player.name} has placed a bet of {player.current_bet}.")

    # Game phase
    for player in players:
        print(f"\n{player.name}'s turn:")
        print("=================================")
        deck = cards.copy()
        random.shuffle(deck)
        player_hand = []
        dealer_hand = []

        # Deal initial hands
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

        print("\nYour hand:", player_hand)
        print("Total:", sum_hand(player_hand))
        print("Dealer's hand:", [dealer_hand[0], "X"])

        # Player's turn
        while True:
            choice = input("Would you like to [H]it or [S]tand? ").upper()
            if choice == 'H':
                player_hand.append(deck.pop())
                print("Your hand:", player_hand)
                print("Total:", sum_hand(player_hand))
                if sum_hand(player_hand) > 21:
                    print("Busted! You lose.")
                    player.budget -= player.current_bet
                    break
            elif choice == 'S':
                break
            else:
                print("Invalid choice. Please enter 'H' or 'S'.")

        if sum_hand(player_hand) <= 21:
            # Dealer's turn
            while sum_hand(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nYour hand:", player_hand)
            print("Your total:", sum_hand(player_hand))
            print("\nDealer's hand:", dealer_hand)
            print("Dealer's total:", sum_hand(dealer_hand))

            # Determine winner
            player_total = sum_hand(player_hand)
            dealer_total = sum_hand(dealer_hand)
            if player_total == 21 and len(player_hand) == 2:  # Blackjack
                print("\nBlackjack! You win 150% of your bet!")
                player.budget += player.current_bet * 1.5
            elif player_total > 21:
                print("\nBusted! You lose.")
                player.budget -= player.current_bet
            elif dealer_total > 21 or player_total > dealer_total:
                print("\nCongratulations! You win!")
                player.budget += player.current_bet
            elif player_total < dealer_total:
                print("\nDealer wins.")
                player.budget -= player.current_bet
            else:
                print("\nIt's a tie!")

            print(f"\nCurrent budget: {player.budget} $")

    play_again = input("\nWould you like to play again? [Y/N] ").upper()
    if play_again != 'Y':
        print("\nThanks for playing!")

def sum_hand(hand):
    total = 0
    num_aces = 0
    for card in hand:
        value = card.split()[0]
        if value in ['J', 'Q', 'K']:
            total += 10
        elif value == 'A':
            num_aces += 1
            total += 11
        else:
            total += int(value)
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

if __name__ == '__main__':
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        budget = float(input(f"Enter budget for player {i+1}: "))
        players.append(Player(name, budget))

    cards = ['2 ♣', '3 ♣', '4 ♣', '5 ♣', '6 ♣', '7 ♣', '8 ♣', '9 ♣', '10 ♣', 'J ♣', 'Q ♣', 'K ♣', 'A ♣',
             '2 ♠', '3 ♠', '4 ♠', '5 ♠', '6 ♠', '7 ♠', '8 ♠', '9 ♠', '10 ♠', 'J ♠', 'Q ♠', 'K ♠', 'A ♠',
             '2 ♥', '3 ♥', '4 ♥', '5 ♥', '6 ♥', '7 ♥', '8 ♥', '9 ♥', '10 ♥', 'J ♥', 'Q ♥', 'K ♥', 'A ♥',
             '2 ♦', '3 ♦', '4 ♦', '5 ♦', '6 ♦', '7 ♦', '8 ♦', '9 ♦', '10 ♦', 'J ♦', 'Q ♦', 'K ♦', 'A ♦']
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11]
    }
    start(players, cards, values)
