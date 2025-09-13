from pathlib import Path
import json
import random
import streamlit as st


dataset = Path(__file__).parent.parent / 'dataset' / 'cards.json'


with open(dataset, "r") as f:
    cards = json.load(f)








def randomizer():
    cards_list = cards["items"]
    random_card = random.sample(cards_list, 8)
    card1 = random_card[0]
    card2 = random_card[1]
    card3 = random_card[2]
    card4 = random_card[3]
    card5 = random_card[4]
    card6 = random_card[5]
    card7 = random_card[6]
    card8 = random_card[7]
    deck = [card1, card2, card3, card4, card5, card6, card7, card8]
    for i in range(len(deck)):
        for j in range(i + 1, len(deck)):
            if deck[i]["rarity"] == deck[j]["rarity"] and not "champion":
                randomizer()
            else:
                continue

    return deck





