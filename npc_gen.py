# NPC GENERATOR (SO TUFF TRUSTTT)

import random
# lines 5 and 6 set up the name list and the user input
name = ["slipper", "fitch", "jimmy", "dora", "bind", "forker", "eclair", "kavin", "nemo", "acrd", "horse", "turk", "area (length x width)", "angulo", "utensil", "kaiser", "lavinho", "gojo"]
amount_of_npcs = (int(input("Enter how many NPCs you want: ")))
print()

# lines 10 - 22 make the code loop the amount of times the user wants and make the variables change every time the code is looped to make unique NPCs each time. They alao set up the format of the print and the print itself, along with the conditional, which makes the algorithm print a certain phrase when ATK is lower than 50.
for amount in range(0, amount_of_npcs):
    npc_name = random.choice(name) + "'s"
    hp = random.randint(1,100)
    defense = random.randint(1,100)
    atk = random.randint(1,100)
    spd = random.randint(1,100)
    height = int(random.uniform(0, 10.0))
    npc = f" {npc_name} HP is: {hp}\n {npc_name} DEF is: {defense}\n {npc_name} ATK is: {atk}\n {npc_name} SPD is: {spd}\n Height is: {height} meters"
    if atk < 50:
        print(npc + "\n This one's weak.")
    else:
        print(npc)
    print()