import streamlit as st
import array
from . import randomizer





def random_deck():
    this = randomizer.randomizer()
    deck = []
    costs = []
    ids = []
    for i in range(0,8):
        deck.append(this[i]["name"])
        costs.append(this[i]["elixirCost"])
        ids.append(this[i]["id"])
        st.write(this[i]["name"] , this[i]["elixirCost"] ,this[i]["id"])
    deck_url = f"https://link.clashroyale.com/en?clashroyale://copyDeck?deck={ids[0]};{ids[1]};{ids[2]};{ids[3]};{ids[4]};{ids[5]};{ids[6]};{ids[7]}&slots=0;0;0;0;0;0;0;0&tt=159000000&l=Royals"
    st.write(deck_url)



