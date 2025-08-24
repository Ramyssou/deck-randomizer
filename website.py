import streamlit as st
st.title('Deck Randomizer')
col1, col2 = st.columns(2)
balanced_deck = col1.button("Balanced Deck")
random_deck = col2.button("Random Deck")
cards = [
    # 1 Elixir
    ("Skeletons", 26000010, 1),
    ("Ice Spirit", 26000030, 1),
    ("Fire Spirit", 26000031, 1),
    ("Heal Spirit", 26000051, 1),
    ("Electro Spirit", 26000064, 1),

    # 2 Elixir
    ("Spear Goblins", 26000002, 2),
    ("Bomber", 26000013, 2),
    ("Bats", 26000049, 2),
    ("Giant Snowball", 28000012, 2),
    ("Rage", 28000002, 2),
    ("Barbarian Barrel", 28000016, 2),
    ("Zap", 26000038, 2),
    ("Mirror", 28000001, 2),  # dynamic cost = last card +1

    # 3 Elixir
    ("Archers", 26000001, 3),
    ("Knight", 26000000, 3),
    ("Minions", 26000005, 3),
    ("Firecracker", 28000002, 3),
    ("Dart Goblin", 26000040, 3),
    ("Arrows", 26000001, 3),
    ("Royal Delivery", 28000017, 3),
    ("Earthquake", 28000015, 3),
    ("Tornado", 28000010, 3),
    ("Clone", 28000011, 3),
    ("Cannon", 27000000, 3),
    ("Tombstone", 27000009, 3),
    ("Mega Minion", 26000035, 3),
    ("Miner", 26000032, 3),

    # 4 Elixir
    ("Musketeer", 26000014, 4),
    ("Mini P.E.K.K.A", 26000018, 4),
    ("Baby Dragon", 26000015, 4),
    ("Valkyrie", 26000011, 4),
    ("Dark Prince", 26000027, 4),
    ("Inferno Dragon", 26000040, 4),
    ("Night Witch", 26000047, 4),
    ("Battle Healer", 26000058, 4),
    ("Hog Rider", 26000021, 4),
    ("Battle Ram", 26000036, 4),
    ("Goblin Drill", 27000013, 4),
    ("Tesla", 27000006, 4),
    ("Bomb Tower", 27000004, 4),
    ("Goblin Cage", 27000012, 4),
    ("Furnace", 27000010, 4),
    ("Fireball", 28000000, 4),
    ("Poison", 28000009, 4),
    ("Freeze", 28000005, 4),
    ("Skeleton King", 26000084, 4),
    ("Golden Knight", 26000085, 4),
    ("Mighty Miner", 26000088, 4),
    ("Little Prince", 26000096, 4),


    # 5 Elixir
    ("Wizard", 26000012, 5),
    ("Prince", 26000022, 5),
    ("Electro Dragon", 26000060, 5),
    ("Bowler", 26000034, 5),
    ("Executioner", 26000045, 5),
    ("Cannon Cart", 26000054, 5),
    ("Rascals", 28000006, 5),
    ("Giant", 26000003, 5),
    ("Ram Rider", 26000050, 5),
    ("Royal Hogs", 26000059, 5),
    ("Graveyard", 28000008, 5),
    ("Inferno Tower", 27000005, 5),
    ("Goblin Hut", 27000001, 5),
    ("Archer Queen", 26000086, 5),
    ("Monk", 26000092, 5),


    # 6 Elixir
    ("Giant Skeleton", 26000020, 6),
    ("Elite Barbarians", 26000028, 6),
    ("Royal Giant", 26000024, 6),
    ("Goblin Giant", 26000052, 6),
    ("Sparky", 26000033, 6),
    ("Rocket", 28000003, 6),
    ("Lightning", 28000007, 6),
    ("Mortar", 27000002, 6),
    ("X-Bow", 27000008, 6),
    ("Elixir Collector", 27000007, 6),

    # 7 Elixir
    ("Lava Hound", 26000029, 7),
    ("P.E.K.K.A", 26000004, 7),
    ("Barbarian Hut", 27000003, 7),

    # 8 Elixir
    ("Golem", 26000009, 8),
    ("Electro Giant", 26000063, 8),
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
# Spells
spells = [
    ("Zap", 26000038, 2),
    ("Mirror", 28000001, 0),
    ("Arrows", 26000001, 3),
    ("Giant Snowball", 28000012, 2),
    ("Rage", 28000002, 2),
    ("Barbarian Barrel", 28000016, 2),
    ("Royal Delivery", 28000017, 3),
    ("Fireball", 28000000, 4),
    ("Poison", 28000009, 4),
    ("Earthquake", 28000015, 3),
    ("Freeze", 28000005, 4),
    ("Lightning", 28000007, 6),
    ("Rocket", 28000003, 6),
    ("Tornado", 28000010, 3),
    ("Clone", 28000011, 3),
]

# Buildings
buildings = [
    ("Cannon", 27000000, 3),
    ("Tombstone", 27000009, 3),
    ("Tesla", 27000006, 4),
    ("Bomb Tower", 27000004, 4),
    ("Goblin Cage", 27000012, 4),
    ("Furnace", 27000010, 4),
    ("Goblin Hut", 27000001, 5),
    ("Barbarian Hut", 27000003, 7),
    ("Mortar", 27000002, 4),
    ("X-Bow", 27000008, 6),
    ("Inferno Tower", 27000005, 5),
    ("Elixir Collector", 27000007, 6),
]

# Win Conditions
winConditions = [
    ("Hog Rider", 26000021, 4),
    ("Miner", 26000032, 3),
    ("Elite Barbarians", 26000028, 6),
    ("Royal Giant", 26000024, 6),
    ("Giant", 26000003, 5),
    ("Battle Ram", 26000036, 4),
    ("Balloon", 26000006, 5),
    ("Goblin Drill", 27000013, 4),
    ("Goblin Giant", 26000052, 6),
    ("Ram Rider", 26000050, 5),
    ("Royal Hogs", 26000059, 5),
    ("Graveyard", 28000008, 5),
    ("Lava Hound", 26000029, 7),
    ("Golem", 26000009, 8),
    ("Sparky", 26000033, 6),
    ("Electro Giant", 26000063, 8),
    ("P.E.K.K.A", 26000004, 7),
]

# Troops
troops = [
    ("Skeletons", 26000010, 1),
    ("Ice Spirit", 26000030, 1),
    ("Fire Spirit", 26000031, 1),
    ("Heal Spirit", 26000051, 1),
    ("Electro Spirit", 26000064, 1),
    ("Spear Goblins", 26000002, 2),
    ("Archers", 26000001, 3),
    ("Knight", 26000000, 3),
    ("Bomber", 26000013, 2),
    ("Bats", 26000049, 2),
    ("Minions", 26000005, 3),
    ("Musketeer", 26000014, 4),
    ("Mini P.E.K.K.A", 26000018, 4),
    ("Baby Dragon", 26000015, 4),
    ("Valkyrie", 26000011, 4),
    ("Wizard", 26000012, 5),
    ("Dark Prince", 26000027, 4),
    ("Prince", 26000022, 5),
    ("Skeleton Army", 26000009, 3),
    ("Inferno Dragon", 26000040, 4),
    ("Electro Dragon", 26000060, 5),
    ("Bowler", 26000034, 5),
    ("Executioner", 26000045, 5),
    ("Giant Skeleton", 26000020, 6),
    ("Cannon Cart", 26000054, 5),
    ("Mega Minion", 26000035, 3),
    ("Night Witch", 26000047, 4),
    ("Firecracker", 28000002, 3),
    ("Rascals", 28000006, 5),
    ("Dart Goblin", 26000040, 3),
    ("Battle Healer", 26000058, 4),
]

# Champions
champions = [
    ("Skeleton King", 26000084, 4),
    ("Golden Knight", 26000085, 4),
    ("Archer Queen", 26000086, 5),
    ("Mighty Miner", 26000088, 4),
    ("Monk", 26000092, 5),
    ("Little Prince", 26000096, 4),
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

