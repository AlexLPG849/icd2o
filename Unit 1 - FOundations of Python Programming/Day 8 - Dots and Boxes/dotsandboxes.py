name = input("Enter your name here: ")
opponents_name1 = "Abraham"
opponents_name2 = "Arees"
opponents_name3 = "Ishaan"
opponents_name4 = "Brandon"
your_total = int(input("Enter total here: "))
opponents_total = int(input("Enter opponents total here: "))
overall = your_total + opponents_total
round_one = int(input("Input your round one points here: "))
round_two = int(input("Input your round two points here: "))
round_three = int(input("Input your round three points here: "))
round_four = int(input("Input your round four points here: "))
opp_r_four = int(input("Input opponents round four points here: "))
opp_r_three = int(input("Input opponents round three points here: "))
opp_r_two = int(input("Input opponents round two points here: "))
opp_r_one = int(input("Input opponents round one points here: "))
bp = int(round_one + opp_r_one)
bp2 = int(round_two + opp_r_two)
bp3 = int(round_three + opp_r_three)
bp4 = int(round_four + opp_r_four)



print(" ")
print(" ")
print (f"{name}'s results: ")
print(" ")
print(" ")
print("Game #1: ")
print(f"Opponents Name: {opponents_name1}")
print("Your points: 19 ")
print("Opponents Points: 17 ")
print(f"Who won game 1: {name}")
print(" ")
print(" ")
print("Game #2: ")
print(f"Opponents Name: {opponents_name2}")
print("Your points: 13 ")
print("Opponents Points: 23 ")
print(f"Who won game 2: {opponents_name2} ")
print(" ")
print(" ")
print("Game #3: ")
print(f"Opponents Name: {opponents_name3}")
print("Your points: 16 ")
print("Opponents Points: 20 ")
print(f"Who won game 3: {opponents_name3}")
print(" ")
print(" ")
print("Game #4: ")
print(f"Opponents Name: {opponents_name4}")
print("Your points: 18 ")
print("Opponents Points: 18 ")
print("Who won game 4: Tie ")
print(" ")
print(" ")
print("Dots and Boxes Table Tracker:")
print(" ")
print(f"Player Name: {name}")

print("Opponent         Your Points          Opponents Points                    Total ")
print("===============================================================================")
print(f"{opponents_name1} {round_one:>20} {opp_r_one:>26} {bp:>23}")
print(f"{opponents_name2} {round_two:>22} {opp_r_two:>26} {bp2:>23}")
print(f"{opponents_name3} {round_three:>21} {opp_r_three:>26} {bp3:>23}")
print(f"{opponents_name4} {round_four:>20} {opp_r_four:>26} {bp4:>23}")
print("===============================================================================")
print(" ")
print("Summary: ")
print(" ")
print(f"Your Total Points: {your_total}")
print(f"Total Opponent Points: {opponents_total}")
print(f"Total Points: {overall}")