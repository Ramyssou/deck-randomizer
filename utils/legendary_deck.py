from pathlib import Path
import json
import random
import streamlit as st


dataset = Path(__file__).parent.parent / 'dataset' / 'cards.json'


with open(dataset, "r") as f:
    cards = json.load(f)



common = {}
def common_cards():
    card = cards["items"]
    for idx, i in enumerate(card):
        if i["rarity"] == "legendary":
            common[idx] = i
    return common



def common_randomizer():
    common_cards()
    cards_list = sorted(common)
    random_card = random.sample(cards_list, 8)
    card1 = common[random_card[0]]
    card2 = common[random_card[1]]
    card3 = common[random_card[2]]
    card4 = common[random_card[3]]
    card5 = common[random_card[4]]
    card6 = common[random_card[5]]
    card7 = common[random_card[6]]
    card8 = common[random_card[7]]
    deck = [card1, card2, card3, card4, card5, card6, card7, card8]
    return deck





def legendary_deck():
    random_cards = common_randomizer()
    ids = []
    row1 = st.columns(4)
    for i in range(0, 8):
        ids.append(random_cards[i]["id"])
        with row1[i - 4]:
            st.image(random_cards[i]["iconUrls"]["medium"], width=100)
            st.write(random_cards[i]["name"], random_cards[i]["elixirCost"])
    deck_url = f"https://link.clashroyale.com/en?clashroyale://copyDeck?deck={ids[0]};{ids[1]};{ids[2]};{ids[3]};{ids[4]};{ids[5]};{ids[6]};{ids[7]}&slots=0;0;0;0;0;0;0;0&tt=159000000&l=Royals"
    st.write(deck_url)

#st.write(commons[i]["name"], commons[i]["elixirCost"], commons[i]["id"])

