import streamlit as st
import sys

sys.setrecursionlimit(10000)
st.title('Deck Randomizer')
col1, col2 = st.columns(2)
balanced_deck = col1.button("Balanced Deck")
random_deck = col2.button("Random Deck")
chose_elixir = col2.checkbox("Chose Elixir cost")
if chose_elixir:
    elixir_cost = col2.number_input("elixir cost", min_value=1.3, max_value=7.3 , format="%.1f" , step=0.1)
else:
    elixir_cost = False



cards = [
    ("Knight", 26000000, 3),
    ("Archers", 26000001, 3),
    ("Goblins", 26000002, 2),
    ("Giant", 26000003, 5),
    ("P.E.K.K.A", 26000004, 7),
    ("Minions", 26000005, 3),
    ("Balloon", 26000006, 5),
    ("Witch", 26000007, 5),
    ("Barbarians", 26000008, 5),
    ("Golem", 26000009, 8),
    ("Skeletons", 26000010, 1),
    ("Valkyrie", 26000011, 4),
    ("Skeleton Army", 26000012, 3),
    ("Bomber", 26000013, 2),
    ("Musketeer", 26000014, 4),
    ("Baby Dragon", 26000015, 4),
    ("Prince", 26000016, 5),
    ("Wizard", 26000017, 5),
    ("Mini P.E.K.K.A", 26000018, 4),
    ("Spear Goblins", 26000019, 2),
    ("Giant Skeleton", 26000020, 6),
    ("Hog Rider", 26000021, 4),
    ("Minion Horde", 26000022, 5),
    ("Ice Wizard", 26000023, 3),
    ("Royal Giant", 26000024, 6),
    ("Guards", 26000025, 3),
    ("Princess", 26000026, 3),
    ("Dark Prince", 26000027, 4),
    ("Three Musketeers", 26000028, 9),
    ("Lava Hound", 26000029, 7),
    ("Ice Spirit", 26000030, 1),
    ("Fire Spirit", 26000031, 1),
    ("Miner", 26000032, 3),
    ("Sparky", 26000033, 6),
    ("Bowler", 26000034, 5),
    ("Lumberjack", 26000035, 4),
    ("Battle Ram", 26000036, 4),
    ("Inferno Dragon", 26000037, 4),
    ("Ice Golem", 26000038, 2),
    ("Mega Minion", 26000039, 3),
    ("Dart Goblin", 26000040, 3),
    ("Goblin Gang", 26000041, 3),
    ("Electro Wizard", 26000042, 4),
    ("Elite Barbarians", 26000043, 6),
    ("Hunter", 26000044, 4),
    ("Executioner", 26000045, 5),
    ("Bandit", 26000046, 3),
    ("Royal Recruits", 26000047, 7),
    ("Night Witch", 26000048, 4),
    ("Bats", 26000049, 2),
    ("Royal Ghost", 26000050, 3),
    ("Ram Rider", 26000051, 5),
    ("Zappies", 26000052, 4),
    ("Rascals", 26000053, 5),
    ("Cannon Cart", 26000054, 5),
    ("Mega Knight", 26000055, 7),
    ("Skeleton Barrel", 26000056, 3),
    ("Flying Machine", 26000057, 4),
    ("Wall Breakers", 26000058, 2),
    ("Royal Hogs", 26000059, 5),
    ("Goblin Giant", 26000060, 6),
    ("Fisherman", 26000061, 3),
    ("Magic Archer", 26000062, 4),
    ("Electro Dragon", 26000063, 5),
    ("Firecracker", 26000064, 3),
    ("Mighty Miner", 26000065, 4),
    ("Elixir Golem", 26000067, 3),
    ("Battle Healer", 26000068, 4),
    ("Skeleton Dragons", 26000080, 4),
    ("Mother Witch", 26000083, 4),
    ("Electro Spirit", 26000084, 1),
    ("Electro Giant", 26000085, 7),
    ("Phoenix", 26000087, 4),
    ("Little Prince", 26000093, 3),
    ("Goblin Demolisher", 26000095, 4),
    ("Goblin Machine", 26000096, 5),
    ("Suspicious Bush", 26000097, 2),
    ("Rune Giant", 26000101, 4),


    # buildings / structures
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
    ("Goblin Drill", 27000013, 4),

    # spells
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
elif random_deck:
    randoms()


