import streamlit as st
import sys
from decimal import Decimal, ROUND_HALF_UP
sys.setrecursionlimit(15000)
st.title('Deck Randomizer')
col1, col2 = st.columns(2)
balanced_deck = col1.button("Balanced Deck")
random_deck = col2.button("Random Deck")
chose_elixir = col2.checkbox("Chose Elixir cost")



if chose_elixir:
    elixir_cost = col2.number_input("elixir cost", min_value=1.3, max_value=7.3 , format="%.1f" , step=0.1, value=4.0)
    if (elixir_cost * 10) % 10 == 7:
        elixir_cost += 0.1

else:
    elixir_cost = False


cards = [
    ("Skeletons", 26000010, 1),
    ("Ice Spirit", 26000030, 1),
    ("Fire Spirit", 26000031, 1),
    ("Electro Spirit", 26000084, 1),
    ("Heal Spirit", 28000016, 1),

    ("Goblins", 26000002, 2),
    ("Bomber", 26000013, 2),
    ("Spear Goblins", 26000019, 2),
    ("Ice Golem", 26000038, 2),
    ("Bats", 26000049, 2),
    ("Wall Breakers", 26000058, 2),
    ("Suspicious Bush", 26000097, 2),
    ("Rage", 28000002, 2),
    ("Zap", 28000008, 2),
    ("The Log", 28000011, 2),
    ("Barbarian Barrel", 28000015, 2),
    ("Giant Snowball", 28000017, 2),
    ("Goblin Curse", 28000024, 2),

    ("Knight", 26000000, 3),
    ("Archers", 26000001, 3),
    ("Minions", 26000005, 3),
    ("Skeleton Army", 26000012, 3),
    ("Ice Wizard", 26000023, 3),
    ("Guards", 26000025, 3),
    ("Princess", 26000026, 3),
    ("Miner", 26000032, 3),
    ("Mega Minion", 26000039, 3),
    ("Dart Goblin", 26000040, 3),
    ("Goblin Gang", 26000041, 3),
    ("Bandit", 26000046, 3),
    ("Royal Ghost", 26000050, 3),
    ("Skeleton Barrel", 26000056, 3),
    ("Fisherman", 26000061, 3),
    ("Firecracker", 26000064, 3),
    ("Elixir Golem", 26000067, 3),
    ("Little Prince", 26000093, 3),
    ("Cannon", 27000000, 3),
    ("Tombstone", 27000009, 3),
    ("Arrows", 28000001, 3),
    ("Goblin Barrel", 28000004, 3),
    ("Tornado", 28000012, 3),
    ("Clone", 28000013, 3),
    ("Earthquake", 28000014, 3),
    ("Royal Delivery", 28000018, 3),
    ("Void", 28000023, 3),

    ("Valkyrie", 26000011, 4),
    ("Musketeer", 26000014, 4),
    ("Baby Dragon", 26000015, 4),
    ("Mini P.E.K.K.A", 26000018, 4),
    ("Hog Rider", 26000021, 4),
    ("Dark Prince", 26000027, 4),
    ("Lumberjack", 26000035, 4),
    ("Battle Ram", 26000036, 4),
    ("Inferno Dragon", 26000037, 4),
    ("Electro Wizard", 26000042, 4),
    ("Hunter", 26000044, 4),
    ("Night Witch", 26000048, 4),
    ("Zappies", 26000052, 4),
    ("Flying Machine", 26000057, 4),
    ("Magic Archer", 26000062, 4),
    ("Mighty Miner", 26000065, 4),
    ("Battle Healer", 26000068, 4),
    ("Skeleton Dragons", 26000080, 4),
    ("Mother Witch", 26000083, 4),
    ("Phoenix", 26000087, 4),
    ("Goblin Demolisher", 26000095, 4),
    ("Rune Giant", 26000101, 4),
    ("Goblin Hut", 27000001, 4),
    ("Mortar", 27000002, 4),
    ("Bomb Tower", 27000004, 4),
    ("Tesla", 27000006, 4),
    ("Furnace", 27000010, 4),
    ("Goblin Cage", 27000012, 4),
    ("Goblin Drill", 27000013, 4),
    ("Fireball", 28000000, 4),
    ("Freeze", 28000005, 4),
    ("Poison", 28000009, 4),

    ("Giant", 26000003, 5),
    ("Balloon", 26000006, 5),
    ("Witch", 26000007, 5),
    ("Barbarians", 26000008, 5),
    ("Prince", 26000016, 5),
    ("Wizard", 26000017, 5),
    ("Minion Horde", 26000022, 5),
    ("Bowler", 26000034, 5),
    ("Executioner", 26000045, 5),
    ("Ram Rider", 26000051, 5),
    ("Rascals", 26000053, 5),
    ("Cannon Cart", 26000054, 5),
    ("Royal Hogs", 26000059, 5),
    ("Graveyard", 28000010, 5),
    ("Electro Dragon", 26000063, 5),
    ("Goblin Machine", 26000096, 5),
    ("Inferno Tower", 27000003, 5),

    ("Giant Skeleton", 26000020, 6),
    ("Royal Giant", 26000024, 6),
    ("Sparky", 26000033, 6),
    ("Elite Barbarians", 26000043, 6),
    ("Goblin Giant", 26000060, 6),
    ("Barbarian Hut", 27000005, 6),
    ("Elixir Collector", 27000007, 6),
    ("X-Bow", 27000008, 6),
    ("Rocket", 28000003, 6),
    ("Lightning", 28000007, 6),
    ("Spirit Empress", 28000025, 6),

    ("P.E.K.K.A", 26000004, 7),
    ("Lava Hound", 26000029, 7),
    ("Royal Recruits", 26000047, 7),
    ("Mega Knight", 26000055, 7),
    ("Electro Giant", 26000085, 7),

    ("Golem", 26000009, 8),

    ("Three Musketeers", 26000028, 9),
]


# Note: Mirror (id=28000006) was present in your JSON but had no "elixirCost" field — omitted above.
# Support items (ids 159000000, 159000001, 159000002, 159000004) also had no elixirCost — omitted.


def big_deck():
    big_cards = cards[33:]
    names = [card[0] for card in big_cards]
    ids = [card[1] for card in big_cards]
    elixir = [card[2] for card in big_cards]

    # pick 8 unique random indices
    chosen = random.sample(range(len(big_cards)), 8)

    # unpack them into names and ids
    name1, id1, elixir1 = names[chosen[0]], ids[chosen[0]], elixir[chosen[0]]
    name2, id2, elixir2 = names[chosen[1]], ids[chosen[1]], elixir[chosen[1]]
    name3, id3, elixir3 = names[chosen[2]], ids[chosen[2]], elixir[chosen[2]]
    name4, id4, elixir4 = names[chosen[3]], ids[chosen[3]], elixir[chosen[3]]
    name5, id5, elixir5 = names[chosen[4]], ids[chosen[4]], elixir[chosen[4]]
    name6, id6, elixir6 = names[chosen[5]], ids[chosen[5]], elixir[chosen[5]]
    name7, id7, elixir7 = names[chosen[6]], ids[chosen[6]], elixir[chosen[6]]
    name8, id8, elixir8 = names[chosen[7]], ids[chosen[7]], elixir[chosen[7]]

    g = (elixir1 + elixir2 + elixir3 + elixir4 + elixir5 + elixir6 + elixir7 + elixir8) / 8
    if (g * 100) % 10 == 5:
        avg_elixir = g + 0.05
    else:
        avg_elixir = round(g, 1)

    while avg_elixir != elixir_cost:
        big_deck()
        break
    if avg_elixir == elixir_cost:
        link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
        st.write("link", link)
        st.write(avg_elixir)
        st.write(name1)
        st.write(name2)
        st.write(name3)
        st.write(name4)
        st.write(name5)
        st.write(name6)
        st.write(name7)
        st.write(name8)

def bigger_deck():
    bigger_cards = cards[75:]
    names = [card[0] for card in bigger_cards]
    ids = [card[1] for card in bigger_cards]
    elixir = [card[2] for card in bigger_cards]

    # pick 8 unique random indices
    chosen = random.sample(range(len(bigger_cards)), 8)

    # unpack them into names and ids
    name1, id1, elixir1 = names[chosen[0]], ids[chosen[0]], elixir[chosen[0]]
    name2, id2, elixir2 = names[chosen[1]], ids[chosen[1]], elixir[chosen[1]]
    name3, id3, elixir3 = names[chosen[2]], ids[chosen[2]], elixir[chosen[2]]
    name4, id4, elixir4 = names[chosen[3]], ids[chosen[3]], elixir[chosen[3]]
    name5, id5, elixir5 = names[chosen[4]], ids[chosen[4]], elixir[chosen[4]]
    name6, id6, elixir6 = names[chosen[5]], ids[chosen[5]], elixir[chosen[5]]
    name7, id7, elixir7 = names[chosen[6]], ids[chosen[6]], elixir[chosen[6]]
    name8, id8, elixir8 = names[chosen[7]], ids[chosen[7]], elixir[chosen[7]]

    g = (elixir1 + elixir2 + elixir3 + elixir4 + elixir5 + elixir6 + elixir7 + elixir8) / 8

    if (g * 100) % 10 == 5:
        avg_elixir = g + 0.05
    else:
        avg_elixir = round(g, 1)

    while avg_elixir != elixir_cost:
        bigger_deck()
        break
    if avg_elixir == elixir_cost:
        link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
        st.write("link", link)
        st.write(avg_elixir)
        st.write(name1)
        st.write(name2)
        st.write(name3)
        st.write(name4)
        st.write(name5)
        st.write(name6)
        st.write(name7)
        st.write(name8)

def small_deck():
    small_cards = cards[:-75]
    names = [card[0] for card in small_cards]
    ids = [card[1] for card in small_cards]
    elixir = [card[2] for card in small_cards]

    # pick 8 unique random indices
    chosen = random.sample(range(len(small_cards)), 8)

    # unpack them into names and ids
    name1, id1, elixir1 = names[chosen[0]], ids[chosen[0]], elixir[chosen[0]]
    name2, id2, elixir2 = names[chosen[1]], ids[chosen[1]], elixir[chosen[1]]
    name3, id3, elixir3 = names[chosen[2]], ids[chosen[2]], elixir[chosen[2]]
    name4, id4, elixir4 = names[chosen[3]], ids[chosen[3]], elixir[chosen[3]]
    name5, id5, elixir5 = names[chosen[4]], ids[chosen[4]], elixir[chosen[4]]
    name6, id6, elixir6 = names[chosen[5]], ids[chosen[5]], elixir[chosen[5]]
    name7, id7, elixir7 = names[chosen[6]], ids[chosen[6]], elixir[chosen[6]]
    name8, id8, elixir8 = names[chosen[7]], ids[chosen[7]], elixir[chosen[7]]

    g = (elixir1 + elixir2 + elixir3 + elixir4 + elixir5 + elixir6 + elixir7 + elixir8) / 8

    if (g * 100) % 10 == 5:
        avg_elixir = g + 0.05
    else:
        avg_elixir = round(g, 1)

    while avg_elixir != elixir_cost:
        small_deck()
        break
    if avg_elixir == elixir_cost:
        link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
        st.write("link", link)
        st.write(avg_elixir)
        st.write(name1)
        st.write(name2)
        st.write(name3)
        st.write(name4)
        st.write(name5)
        st.write(name6)
        st.write(name7)
        st.write(name8)



def randoms():


  names = [card[0] for card in cards]
  ids = [card[1] for card in cards]
  elixir = [card[2] for card in cards]

  # pick 8 unique random indices
  chosen = random.sample(range(len(cards)), 8)

  # unpack them into names and ids
  name1, id1, elixir1 = names[chosen[0]], ids[chosen[0]], elixir[chosen[0]]
  name2, id2, elixir2 = names[chosen[1]], ids[chosen[1]], elixir[chosen[1]]
  name3, id3, elixir3 = names[chosen[2]], ids[chosen[2]], elixir[chosen[2]]
  name4, id4, elixir4 = names[chosen[3]], ids[chosen[3]], elixir[chosen[3]]
  name5, id5, elixir5 = names[chosen[4]], ids[chosen[4]], elixir[chosen[4]]
  name6, id6, elixir6 = names[chosen[5]], ids[chosen[5]], elixir[chosen[5]]
  name7, id7, elixir7 = names[chosen[6]], ids[chosen[6]], elixir[chosen[6]]
  name8, id8, elixir8 = names[chosen[7]], ids[chosen[7]], elixir[chosen[7]]

  g = (elixir1 + elixir2 + elixir3 + elixir4 + elixir5 + elixir6 + elixir7 + elixir8) / 8

  if (g * 100) % 10 == 5:
      avg_elixir = g + 0.05
  else:
      avg_elixir = round(g, 1)

  if chose_elixir:
      while avg_elixir != elixir_cost:
          deck()
          break
      if avg_elixir == elixir_cost:
          link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
          st.write("link", link)
          st.write(avg_elixir)

          st.write(name1)
          st.write(name2)
          st.write(name3)
          st.write(name4)
          st.write(name5)
          st.write(name6)
          st.write(name7)
          st.write(name8)
          st.write(g)
  elif elixir_cost == False:
      link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
      st.write("link", link)
      st.write(avg_elixir)
      st.write(name1)
      st.write(name2)
      st.write(name3)
      st.write(name4)
      st.write(name5)
      st.write(name6)
      st.write(name7)
      st.write(name8)
      st.write(g)





#randomize proper dekcs now: 1 win con 2 spells 2 air counters 1 mini tank 1 tank killer 1 building

# Spells
import random
# Converted from the JSON you provided.
# Only entries that had an "elixirCost" in the source are included.
# Omitted entries where elixirCost was not present in the JSON (e.g. Mirror id=28000006, supportItems 159000000+).

troops = [

    ("Knight", 26000000, 3),
    ("Archers", 26000001, 3),
    ("Goblins", 26000002, 2),
    ("P.E.K.K.A", 26000004, 7),
    ("Barbarians", 26000008, 5),
    ("Skeletons", 26000010, 1),
    ("Valkyrie", 26000011, 4),
    ("Skeleton Army", 26000012, 3),
    ("Bomber", 26000013, 2),
    ("Musketeer", 26000014, 4),
    ("Prince", 26000016, 5),
    ("Mini P.E.K.K.A", 26000018, 4),
    ("Spear Goblins", 26000019, 2),
    ("Giant Skeleton", 26000020, 6),
    ("Wizard", 26000017, 5),
    ("Ice Wizard", 26000023, 3),
    ("Guards", 26000025, 3),
    ("Princess", 26000026, 3),
    ("Dark Prince", 26000027, 4),
    ("Ice Spirit", 26000030, 1),
    ("Fire Spirit", 26000031, 1),
    ("Bowler", 26000034, 5),
    ("Lumberjack", 26000035, 4),
    ("Battle Ram", 26000036, 4),
    ("Ice Golem", 26000038, 2),
    ("Dart Goblin", 26000040, 3),
    ("Goblin Gang", 26000041, 3),
    ("Electro Wizard", 26000042, 4),
    ("Elite Barbarians", 26000043, 6),
    ("Hunter", 26000044, 4),
    ("Executioner", 26000045, 5),
    ("Bandit", 26000046, 3),
    ("Royal Recruits", 26000047, 7),
    ("Night Witch", 26000048, 4),
    ("Royal Ghost", 26000050, 3),
    ("Zappies", 26000052, 4),
    ("Rascals", 26000053, 5),
    ("Cannon Cart", 26000054, 5),
    ("Skeleton Barrel", 26000056, 3),
    ("Flying Machine", 26000057, 4),
    ("Wall Breakers", 26000058, 2),
    ("Fisherman", 26000061, 3),
    ("Magic Archer", 26000062, 4),
    ("Firecracker", 26000064, 3),
    ("Mighty Miner", 26000065, 4),
    ("Battle Healer", 26000068, 4),
    ("Mother Witch", 26000083, 4),
    ("Electro Spirit", 26000084, 1),
    ("Little Prince", 26000093, 3),
    ("Goblin Demolisher", 26000095, 4),
    ("Goblin Machine", 26000096, 5),
    ("Suspicious Bush", 26000097, 2),
    ("Rune Giant", 26000101, 4),
    ("Berserker", 26000102, 2),
    ("Minions", 26000005, 3),
    ("Minion Horde", 26000022, 5),
    ("Baby Dragon", 26000015, 4),
    ("Bats", 26000049, 2),
    ("Mega Minion", 26000039, 3),
    ("Inferno Dragon", 26000037, 4),
    ("Electro Dragon", 26000063, 5),
    ("Skeleton Dragons", 26000080, 4),
    ("Phoenix", 26000087, 4),
]


winConditions = [
    ("Giant", 26000003, 5),
    ("Golem", 26000009, 8),
    ("Hog Rider", 26000021, 4),
    ("Royal Giant", 26000024, 6),
    ("Balloon", 26000006, 5),
    ("Miner", 26000032, 3),
    ("Lava Hound", 26000029, 7),
    ("Goblin Giant", 26000060, 6),
    ("Battle Ram", 26000036, 4),
    ("Royal Hogs", 26000059, 5),
    ("Ram Rider", 26000051, 5),
    ("Skeleton Barrel", 26000056, 3),
    ("Elixir Golem", 26000067, 3),
]

air_attackers = [
    ("Minions", 26000005, 3),
    ("Minion Horde", 26000022, 5),
    ("Baby Dragon", 26000015, 4),
    ("Balloon", 26000006, 5),
    ("Lava Hound", 26000029, 7),
    ("Bats", 26000049, 2),
    ("Mega Minion", 26000039, 3),
    ("Inferno Dragon", 26000037, 4),
    ("Electro Dragon", 26000063, 5),
    ("Flying Machine", 26000057, 4),
    ("Skeleton Dragons", 26000080, 4),
    ("Phoenix", 26000087, 4),
    ("Sparky", 26000033, 6),        # ground-targeting but placed here in case you consider heavy ranged/air-relevant threats (optional)
    ("Firecracker", 26000064, 3),   # can hit air units with its projectile
]

# Notes:
# - I intentionally kept overlaps (Balloon, Lava Hound) because they are both air units and common win conditions.
# - "Skeleton Barrel" is included as a win condition here (it's often used as a win-condition/chip finisher). If you want a stricter list
#   (only classic 'building-pushers' like Giant/Hog/Royal Giant/Golem/etc.), tell me and I'll remove borderline items (Skeleton Barrel, Battle Ram, Royal Hogs).
# - I avoided including troops/spells not present in your pasted tuple list.


buildings = [
    ("Cannon", 27000000, 3),
    ("Goblin Hut", 27000001, 4),
    ("Mortar", 27000002, 4),
    ("Inferno Tower", 27000003, 5),
    ("Bomb Tower", 27000004, 4),
    ("Barbarian Hut", 27000005, 6),
    ("Tesla", 27000006, 4),
    ("Elixir Collector", 27000007, 6),
    ("X-Bow", 27000008, 6),
    ("Tombstone", 27000009, 3),
    ("Furnace", 27000010, 4),
    ("Goblin Cage", 27000012, 4),
    ("Goblin Drill", 27000013, 4)
    ]

spells = [
    ("Fireball", 28000000, 4),
    ("Arrows", 28000001, 3),
    ("Rage", 28000002, 2),
    ("Rocket", 28000003, 6),
    ("Goblin Barrel", 28000004, 3),
    ("Freeze", 28000005, 4),
    ("Lightning", 28000007, 6),
    ("Zap", 28000008, 2),
    ("Poison", 28000009, 4),
    ("Graveyard", 28000010, 5),
    ("The Log", 28000011, 2),
    ("Tornado", 28000012, 3),
    ("Clone", 28000013, 3),
    ("Earthquake", 28000014, 3),
    ("Barbarian Barrel", 28000015, 2),
    ("Heal Spirit", 28000016, 1),
    ("Giant Snowball", 28000017, 2),
    ("Royal Delivery", 28000018, 3),
    ("Void", 28000023, 3),
    ("Goblin Curse", 28000024, 2),
    ("Spirit Empress", 28000025, 6),
]

# Note: Mirror (id=28000006) was present in your JSON but had no "elixirCost" field — omitted above.
# Support items (ids 159000000, 159000001, 159000002, 159000004) also had no elixirCost — omitted.


def deck():
    global elixir_cost
    import random
    build_names = [b[0] for b in buildings]
    build_ids = [b[1] for b in buildings]
    build_elixirs = [b[2] for b in buildings]
    name1, id1, elixir1 = random.choice(list(zip(build_names, build_ids, build_elixirs)))

    spell_names = [s[0] for s in spells]
    spell_ids = [s[1] for s in spells]
    spell_elixirs = [s[2] for s in spells]
    (name2, id2, elixir2), (name3, id3, elixir3) = random.sample(
        list(zip(spell_names, spell_ids, spell_elixirs)), 2
    )

    troop_names = [t[0] for t in troops]
    troop_ids = [t[1] for t in troops]
    troop_elixirs = [t[2] for t in troops]
    (name4, id4, elixir4), (name5, id5, elixir5), (name6, id6, elixir6), (name7, id7, elixir7) = random.sample(
        list(zip(troop_names, troop_ids, troop_elixirs)), 4
    )

    wincon_names = [wc[0] for wc in winConditions]
    wincon_ids = [wc[1] for wc in winConditions]
    wincon_elixirs = [wc[2] for wc in winConditions]
    name8, id8, elixir8 = random.choice(
        list(zip(wincon_names, wincon_ids, wincon_elixirs))
    )

    avg_elixir = round((elixir1 + elixir2 + elixir3 + elixir4 + elixir5 + elixir6 + elixir7 + elixir8) / 8, 1)
    if chose_elixir:
        while avg_elixir != elixir_cost:
            deck()
            break
        if avg_elixir == elixir_cost:
            link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
            st.write("link", link)
            st.write(avg_elixir)
            st.write(name1)
            st.write(name2)
            st.write(name3)
            st.write(name4)
            st.write(name5)
            st.write(name6)
            st.write(name7)
            st.write(name8)
    elif elixir_cost == False:
        link = f"https://link.clashroyale.com/deck/en?deck={id1};{id2};{id3};{id4};{id5};{id6};{id7};{id8}&l=Royals&slots=0;0;0;0;0;0;0;0&tt=159000000"
        st.write("link", link)
        st.write(avg_elixir)
        st.write(name1)
        st.write(name2)
        st.write(name3)
        st.write(name4)
        st.write(name5)
        st.write(name6)
        st.write(name7)
        st.write(name8)


if balanced_deck:
    deck()
if random_deck:
    if elixir_cost == False:
        randoms()
    else:
        if 6.4> elixir_cost >= 5.5:
            big_deck()
        elif elixir_cost >= 6.4:
            bigger_deck()
        elif elixir_cost <= 2.4:
            small_deck()
    if 2.5 <= elixir_cost <5.5:
        randoms()




