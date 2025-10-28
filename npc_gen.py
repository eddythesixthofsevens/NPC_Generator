# NPC GENERATOR (SO TUFF TRUSTTT)

import random
name = ["slipper", "fitch", "jimmy", "dora", "bind", "forker", "eclair", "kavin", "nemo", "acrd", "horse", "turk", "area (length x width)", "angulo", "utensil", "kaiser", "lavinho", "gojo"]
hp = random.randint(1,101)
defense = random.randint(1,101)
atk = random.randint(1,101)
spd = random.randint(1,101)
height = int(random.uniform(0, 10.0))
amount_of_npcs = (int(input("Enter how many NPCs you want: ")) + 1)

for amount in range(0, amount_of_npcs):
    npc_name = random.choice(name) + "'s"
    atk = random.randint(1,101)
    npc = f" {npc_name} HP is: {hp}\n {npc_name} DEF is: {defense}\n {npc_name} ATK is: {atk}\n {npc_name} SPD is: {spd}\n Height is: {height} meters"
    if atk < 50:
        print(npc + "\n This one's weak.")
    else:
        print(npc)
    print()