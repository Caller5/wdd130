import random

die_sides = int(input("How many sides do you want the die to be? "))

while die_sides != 4 and die_sides != 6 and die_sides != 8 and die_sides != 10 and die_sides != 12 and die_sides != 20:
    print("Please choose either a 4, 6, 8, 10, 12, or 20 sided die.")
    die_sides = int(input("How many sides do you want the die to be? "))

dice = random.randint (1, die_sides)
#print(dice)
if dice <= 9:
    print(f"""
                 ___________
                |           |
                |           |
                |     {dice}     |
                |           |
                |___________| 

                """)
else:
    print(f"""
                 ___________
                |           |
                |           |
                |    {dice}     |
                |           |
                |___________| 

                """)