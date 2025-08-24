import streamlit as st
st.title('Deck Randomizer')
col1, col2 = st.columns(2)
balanced_deck = col1.button("Balanced Deck")
random_deck = col2.button("Random Deck")

cards = [
    # Spells
    ("Zap", 26000038, "Spell"),
    ("Arrows", 26000001, "Spell"),
    ("Giant Snowball", 28000012, "Spell"),
    ("Royal Delivery", 28000017, "Spell"),
    ("Fireball", 28000000, "Spell"),
    ("Rocket", 28000003, "Spell"),
    ("Poison", 28000009, "Spell"),
    ("Lightning", 28000007, "Spell"),
    ("Freeze", 28000005, "Spell"),
    ("Clone", 28000011, "Spell"),
    ("Rage", 28000002, "Spell"),
    ("Earthquake", 28000015, "Spell"),
    ("Tornado", 28000010, "Spell"),
    ("Mirror", 28000001, "Spell"),
    ("Barbarian Barrel", 28000016, "Spell"),

    # Buildings
    ("Cannon", 27000000, "Building"),
    ("Tesla", 27000006, "Building"),
    ("Mortar", 27000002, "Building"),
    ("Bomb Tower", 27000004, "Building"),
    ("Furnace", 27000010, "Building"),
    ("Goblin Cage", 27000012, "Building"),
    ("Goblin Hut", 27000001, "Building"),
    ("Barbarian Hut", 27000003, "Building"),
    ("Elixir Collector", 27000007, "Building"),
    ("X-Bow", 27000008, "Building"),
    ("Inferno Tower", 27000005, "Building"),
    ("Tombstone", 27000009, "Building"),

    # Win Conditions
    ("Hog Rider", 26000021, "Win Condition"),
    ("Royal Giant", 26000024, "Win Condition"),
    ("Elite Barbarians", 26000028, "Win Condition"),
    ("Giant", 26000003, "Win Condition"),
    ("Battle Ram", 26000036, "Win Condition"),
    ("Balloon", 26000006, "Win Condition"),
    ("Goblin Drill", 27000013, "Win Condition"),
    ("Goblin Giant", 26000052, "Win Condition"),
    ("Golem", 26000009, "Win Condition"),
    ("Lava Hound", 26000029, "Win Condition"),
    ("Royal Hogs", 26000059, "Win Condition"),
    ("Ram Rider", 26000050, "Win Condition"),
    ("Miner", 26000032, "Win Condition"),
    ("Graveyard", 28000008, "Win Condition"),
    ("Sparky", 26000033, "Win Condition"),
    ("Electro Giant", 26000063, "Win Condition"),
    ("P.E.K.K.A", 26000004, "Win Condition"),

    # Troops
    ("Skeletons", 26000010, "Troop"),
    ("Archers", 26000001, "Troop"),
    ("Knight", 26000000, "Troop"),
    ("Bomber", 26000013, "Troop"),
    ("Bats", 26000049, "Troop"),
    ("Minions", 26000005, "Troop"),
    ("Spear Goblins", 26000002, "Troop"),
    ("Musketeer", 26000014, "Troop"),
    ("Mini P.E.K.K.A", 26000018, "Troop"),
    ("Baby Dragon", 26000015, "Troop"),
    ("Valkyrie", 26000011, "Troop"),
    ("Wizard", 26000012, "Troop"),
    ("Dark Prince", 26000027, "Troop"),
    ("Prince", 26000022, "Troop"),
    ("Skeleton Army", 26000009, "Troop"),
    ("Inferno Dragon", 26000040, "Troop"),
    ("Electro Dragon", 26000060, "Troop"),
    ("Bowler", 26000034, "Troop"),
    ("Executioner", 26000045, "Troop"),
    ("Giant Skeleton", 26000020, "Troop"),
    ("Cannon Cart", 26000054, "Troop"),
    ("Mega Minion", 26000035, "Troop"),
    ("Night Witch", 26000047, "Troop"),
    ("Firecracker", 28000002, "Troop"),
    ("Rascals", 28000006, "Troop"),
    ("Dart Goblin", 26000040, "Troop"),
    ("Battle Healer", 26000058, "Troop"),

    # Champions
    ("Skeleton King", 26000084, "Champion"),
    ("Golden Knight", 26000085, "Champion"),
    ("Archer Queen", 26000086, "Champion"),
    ("Mighty Miner", 26000088, "Champion"),
    ("Monk", 26000092, "Champion"),
    ("Little Prince", 26000096, "Champion"),


]

def randoms():


  names = [card[0] for card in cards]
  ids = [card[1] for card in cards]

  # pick 8 unique random indices
  chosen = random.sample(range(len(cards)), 8)

  # unpack them into names and ids
  name1, id1 = names[chosen[0]], ids[chosen[0]]
  name2, id2 = names[chosen[1]], ids[chosen[1]]
  name3, id3 = names[chosen[2]], ids[chosen[2]]
  name4, id4 = names[chosen[3]], ids[chosen[3]]
  name5, id5 = names[chosen[4]], ids[chosen[4]]
  name6, id6 = names[chosen[5]], ids[chosen[5]]
  name7, id7 = names[chosen[6]], ids[chosen[6]]
  name8, id8 = names[chosen[7]], ids[chosen[7]]


  link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
  st.write("link", link)


#randomize proper dekcs now: 1 win con 2 spells 2 air counters 1 mini tank 1 tank killer 1 building

# Spells
spells = [
    ("Zap", 26000038),
    ("Arrows", 26000001),
    ("Giant Snowball", 28000012),
    ("Royal Delivery", 28000017),
    ("Fireball", 28000000),
    ("Rocket", 28000003),
    ("Poison", 28000009),
    ("Lightning", 28000007),
    ("Freeze", 28000005),
    ("Clone", 28000011),
    ("Rage", 28000002),
    ("Earthquake", 28000015),
    ("Tornado", 28000010),
    ("Mirror", 28000001),
    ("Barbarian Barrel", 28000016)
]

# Buildings
buildings = [
    ("Cannon", 27000000),
    ("Tesla", 27000006),
    ("Mortar", 27000002),
    ("Bomb Tower", 27000004),
    ("Furnace", 27000010),
    ("Goblin Cage", 27000012),
    ("Goblin Hut", 27000001),
    ("Barbarian Hut", 27000003),
    ("Elixir Collector", 27000007),
    ("X-Bow", 27000008),
    ("Inferno Tower", 27000005),
    ("Tombstone", 27000009)
]

# Win Conditions
winConditions = [
    ("Hog Rider", 26000021),
    ("Royal Giant", 26000024),
    ("Elite Barbarians", 26000028),
    ("Giant", 26000003),
    ("Battle Ram", 26000036),
    ("Balloon", 26000006),
    ("Goblin Drill", 27000013),
    ("Goblin Giant", 26000052),
    ("Golem", 26000009),
    ("Lava Hound", 26000029),
    ("Royal Hogs", 26000059),
    ("Ram Rider", 26000050),
    ("Miner", 26000032),
    ("Graveyard", 28000008),
    ("Sparky", 26000033),
    ("Electro Giant", 26000063),
    ("P.E.K.K.A", 26000004)
]

# Troops
troops = [
    ("Skeletons", 26000010),
    ("Archers", 26000001),
    ("Knight", 26000000),
    ("Bomber", 26000013),
    ("Bats", 26000049),
    ("Minions", 26000005),
    ("Spear Goblins", 26000002),
    ("Musketeer", 26000014),
    ("Mini P.E.K.K.A", 26000018),
    ("Baby Dragon", 26000015),
    ("Valkyrie", 26000011),
    ("Wizard", 26000012),
    ("Dark Prince", 26000027),
    ("Prince", 26000022),
    ("Skeleton Army", 26000009),
    ("Inferno Dragon", 26000040),
    ("Electro Dragon", 26000060),
    ("Bowler", 26000034),
    ("Executioner", 26000045),
    ("Giant Skeleton", 26000020),
    ("Cannon Cart", 26000054),
    ("Mega Minion", 26000035),
    ("Night Witch", 26000047),
    ("Firecracker", 28000002),
    ("Rascals", 28000006),
    ("Dart Goblin", 26000040),
    ("Battle Healer", 26000058)
]

# Champions
champions = [
    ("Skeleton King", 26000084),
    ("Golden Knight", 26000085),
    ("Archer Queen", 26000086),
    ("Mighty Miner", 26000088),
    ("Monk", 26000092),
    ("Little Prince", 26000096)
]

# Tower Troops (IDs not public yet, so None)
tower_troops = [
    ("Tower Princess", None),
    ("Cannoneer", None),
    ("Dagger Duchess", None),
    ("Royal Chef", None)
]


import random

def deck():
  build_names = [b[0] for b in buildings]
  build_ids = [b[1] for b in buildings]
  name1, id1 = random.choice(list(zip(build_names, build_ids)))

  # spells (2 unique)
  spell_names = [s[0] for s in spells]
  spell_ids = [s[1] for s in spells]
  (name2, id2), (name3, id3) = random.sample(list(zip(spell_names, spell_ids)), 2)

  # troops (4 unique)
  troop_names = [t[0] for t in troops]
  troop_ids = [t[1] for t in troops]
  (name4, id4), (name5, id5), (name6, id6), (name7, id7) = random.sample(list(zip(troop_names, troop_ids)), 4)

  # win condition (1)
  wincon_names = [wc[0] for wc in winConditions]
  wincon_ids = [wc[1] for wc in winConditions]
  name8, id8 = random.choice(list(zip(wincon_names, wincon_ids)))



  # deck link
  link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
  st.write("link", link)





















if balanced_deck:
    deck()
elif random_deck:
    randoms()

