import streamlit as st
import array
from . import randomizer





def random_deck():
    random_cards = randomizer.randomizer()
    ids = []
    row1 = st.columns(4)
    for i in range(0,8):
        ids.append(random_cards[i]["id"])
        with row1[i-4]:
            st.image(random_cards[i]["iconUrls"]["medium"] , width=100)
            st.write(random_cards[i]["name"], random_cards[i]["elixirCost"])
    deck_url = f"https://link.clashroyale.com/en?clashroyale://copyDeck?deck={ids[0]};{ids[1]};{ids[2]};{ids[3]};{ids[4]};{ids[5]};{ids[6]};{ids[7]}&slots=0;0;0;0;0;0;0;0&tt=159000000&l=Royals"
    st.write(deck_url)



