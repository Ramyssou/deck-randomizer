import streamlit as st
import sys
sys.setrecursionlimit(5000)
from utils import random_deck, rare_deck , epic_deck , legendary_deck
from utils import common_deck
from utils import randomizer

st.title('Deck Randomizer')
col1, col2 = st.columns(2)
random_decks = st.button("Random Deck")
select = st.selectbox("Choose Rarity", options=["all" , "common" , "rare" , "epic" , "legendary"])

if select == "common":
    if random_decks:
        common_deck.common_deck()
if select == "rare":
    if random_decks:
        rare_deck.rare_deck()
if select == "epic":
    if random_decks:
        epic_deck.epic_deck()
if select == "legendary":
    if random_decks:
        legendary_deck.legendary_deck()
elif select == "all" and random_decks:
    random_deck.random_deck()
