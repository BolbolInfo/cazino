

suits = ['♣','♠','♥','♦']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a list to hold the deck of cards
deck = []

# Populate the deck with cards
for suit in suits:
    for rank in ranks:
        card = rank+' '+ suit  # Each card is a tuple containing rank and suit
        deck.append(card)

# Print the deck to verify
print(deck)