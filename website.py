import streamlit as st
import sys
sys.setrecursionlimit(5000)
from utils import random_deck
from utils import randomizer

st.title('Deck Randomizer')
col1, col2 = st.columns(2)
random_decks = col2.button("Random Deck")


if random_deck:
    random_deck.random_deck()
