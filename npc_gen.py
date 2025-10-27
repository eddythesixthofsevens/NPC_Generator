# NPC GENERATOR (SO TUFF TRUSTTT)

import random
name = ["habibi", "fitch", "jimmy", "dora", "haleeb", "forker", "eclair", "kavin", "nemo", "obcd", "horse", "turk", "area (length x width)", "angulo", "utensil", "kaiser", "lavinho"]
npc_name = random.choice(name) + "'s"
hp = random.randint(1,101)
defense = random.randint(1,101)
atk = random.randint(1,101)
spd = random.randint(1,101)
amount_of_npcs = int(input("Enter how many NPCs you want: "))

npc = f" {npc_name} HP is: {hp}\n {npc_name} DEF is: {defense}\n {npc_name} ATK is: {atk} \n {npc_name} SPD is: {spd}"
for amount in range(0, amount_of_npcs):
    print(npc)
    print()