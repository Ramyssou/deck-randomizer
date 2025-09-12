import streamlit as st
import array
from . import randomizer





def random_deck():
    random_cards = randomizer.randomizer()
    deck = []
    costs = []
    ids = []
    pics = []
    for i in range(0,8):
        deck.append(random_cards[i]["name"])
        costs.append(random_cards[i]["elixirCost"])
        ids.append(random_cards[i]["id"])
        pics.append(random_cards[i]["medium"])
        st.write(random_cards[i]["name"] , random_cards[i]["elixirCost"] ,random_cards[i]["id"])
        st.image(random_cards[i]["medium"])
    deck_url = f"https://link.clashroyale.com/en?clashroyale://copyDeck?deck={ids[0]};{ids[1]};{ids[2]};{ids[3]};{ids[4]};{ids[5]};{ids[6]};{ids[7]}&slots=0;0;0;0;0;0;0;0&tt=159000000&l=Royals"
    st.write(deck_url)



