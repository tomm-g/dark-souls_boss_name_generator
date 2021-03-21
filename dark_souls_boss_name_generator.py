import sys, random

print("Welcome to Dark Souls Boss Name Generator v0.1 Accursed Undead\n")

first = ('Accursed', 'Nightborne', 'Burnt', 'Odorous', 'Crucified', 'Putrescent', 'Desolate', 'Queens', 'Emaciated', 'Rotting', 'Forsaken', 'Sunken', 'Gallant', 'Torturer', 'Holy', 'Undying', 'Incorruptible', 'Voiceless', 'Joyless', 'Wayward', 'Knot-ridden', 'Xylophonic', 'Luminous', 'Yellowed', 'Multilated', 'Zygomorphous')

last = ('Child', 'Conflagration', 'Wetch', 'Construct', 'Orphan', 'lord of Sin', 'Beast', 'Deacon', 'grave Robber', 'Executioner', 'Dragonrider', 'Giant', 'Corpse Gatherer', 'Mistake', 'Throne Watcher', 'Conqueror', 'Blacksmith', 'Sorcerer', 'Archivist', 'Gravekeeper', 'Living Mountain', 'Serpent Spawn', 'Bloodletter', 'Centipede', 'Aerobics instructor', 'Pallbearer', 'Archdemon', 'Bone Collective', 'Sun Guardian', 'Golem', 'Magistrate')

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press enter else n to quit)\n ")
    if try_again.lower() == "n":
        break


input("\nPress Enter to exit")
