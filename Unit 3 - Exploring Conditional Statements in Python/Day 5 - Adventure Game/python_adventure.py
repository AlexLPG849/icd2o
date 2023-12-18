import random # used to randomly generate a number used to do something when the code is executed
# for example, random.randint picks any number in the given subset, it could be the number itself or a number along the lines of them

# Task 1 (character creator)
def create_character():
    print("")
    print("Welcome to the character creation!")
    print("")
    print("When selecting something, Make sure you have correct spelling and capitals (i.e. 'crouch' to crouch into a small area)")
    print("")
    character_name = input("Enter your character's name: ")
    print("Choose your character class, " + character_name + "!:")
    print("")
    print("1. Warrior")
    print("2. Mage")
    print("3. Mr Miyagi")
    print("")
    class_choice = input("Enter the number corresponding to your class choice (1/2/3): ")
    while class_choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter a valid number.")
        print("")
        class_choice = input("Enter the number corresponding to your class choice (1/2/3): ")
    print("")
    if class_choice == '1':
        character_class = "Warrior"
    elif class_choice == '2':
        character_class = "Mage"
    else:
        character_class = "Mr. Miyagi"
    
    initial_health = input("Enter your character's initial health (between 100 and 150): ")
    while not initial_health.isdigit() or not (100 <= int(initial_health) <= 150):
        print("")
        print("Invalid input. Please enter a valid number between 100 and 150.")
        print("")
        initial_health = input("Enter your character's initial health (between 100 and 150): ")
    
    return character_name, character_class, int(initial_health)

# Task 2 (introduction of the game)
def game_intro(character_name, character_class):
    print("Welcome, " + character_name + ", the " + character_class + "!")
    print("You find yourself in the middle of a jungle.")
    print("Your journey begins now!")
    
    if character_class == "Mage":
        print("Spells: Fireball - 30-80 Damage / Gear: Novice Wand")
    elif character_class == "Warrior":
        print("Attacks: Sword Throw - 20-90 Damage / Gear: Longsword")
    elif character_class == "Mr. Miyagi":
        print("Attacks: Japanese Kung Fu - 40-80 Damage")

# Task 3 (first decision in the adventure)
def make_decision():
    print("You find yourself at a temple.")
    decision = input("Do you want to go in politely or sneak in? (pick 'walk' or 'sneak'): ")
    while decision not in ['walk', 'sneak']:
        print("Invalid choice. Please enter 'Walk' or 'Sneak'.")
        decision = input("Do you want to walk in or sneak in? ")
    
    return decision

# Task 4 (encountering something function)
def encounter_scenario(direction):
    if direction == 'walk':
        print("The monkeys don't recognise you, they attack you and startle the monkey king. Get ready for a battle!")
    else:
        print("The hostile monkeys of the jungle think you're an intruder! Get ready for a battle against the monkey king!")

# Task 5 (health management system)
def manage_health(current_health, damage_taken):
    remaining_health = current_health - damage_taken
    if remaining_health <= 0:
        print("Oh no! Your health is at 0, you are no longer standing. You have been defeated.")
        return 0
    else:
        print("You took " + str(damage_taken) + " damage. Your remaining health is " + str(remaining_health) + ".")

        return remaining_health

# Task 6 (bonus point system)
def bonus_points():
    bonus_points = 0
    
    king_bonus = input("Did you defeat the king? (yes/no): ")
    if king_bonus == 'yes':
        bonus_points += 25
        print("You've earned 25 bonus points for defeating the monkey king!")    
    
    creative_bonus = input("Did you come up with a creative solution during the encounter? (yes/no): ")
    if creative_bonus == 'yes':
        bonus_points += 10
        print("You've earned 10 bonus points for creativity!")

    print("Bonus Points Earned: " + str(bonus_points))
    return bonus_points

def attack_king(current_health, king_health, character_class):
    print("You decide to confront the king!")

    attack_type = None
    player_damage = 0  

    if character_class == "Mage":
        attack_type = "Fireball"
        player_damage = random.randint(30, 80)
    elif character_class == "Warrior":
        attack_type = "Sword Throw"
        player_damage = random.randint(20, 90)
    elif character_class == "Mr. Miyagi":
        attack_type = "Japanese Kung Fu"
        player_damage = random.randint(40, 80)
    
    king_damage = random.randint(10, 50)

    if player_damage > 0:
        king_health -= player_damage
        print(f"You dealt {player_damage} damage to the monkey king using {attack_type}. The king's remaining health: {king_health}")

        king_defeated = king_health <= 0
        if king_defeated:
            print("Congratulations! You defeated the monkey king!")
            king_health = 0
        else:
            attack_again = input("The king is still standing! Do you want to attack again or retreat? (attack/retreat): ")
            while attack_again.lower() not in ['attack', 'retreat']:
                print("Invalid choice. Please enter 'attack' or 'retreat'.")
                attack_again = input("The king is still standing! Do you want to attack again or retreat? (attack/retreat): ")

            if attack_again == 'attack':
                second_attack_type = "Second " + attack_type
                second_player_damage = random.randint(30, 60)
                king_health -= second_player_damage
                print(f"You dealt {second_player_damage} damage to the king using {second_attack_type}. The king's remaining health: {king_health}")

                king_defeated = king_health <= 0
                if king_defeated:
                    print("Congratulations! You defeated the monkey king!")
                    king_health = 0
                else:
                    attack_type = second_attack_type
                    player_damage += second_player_damage
            else:
                print(f"You chose to retreat. The king counter-attacks and deals {king_damage} damage to you.")
                current_health -= king_damage

    return current_health, king_health, player_damage, king_defeated, attack_type

# Task 7 (playing the game)
def play_game():
    character_name, character_class, initial_health = create_character()
    game_intro(character_name, character_class)
    
    current_health = initial_health
    king_health = 100  
    king_defeated = False  

    chosen_direction = make_decision()
    encounter_scenario(chosen_direction)
    
    damage_taken = random.randint(10, 100)
    current_health = manage_health(current_health, damage_taken)
    
    valid_attack_option = False
    while not valid_attack_option:
        attack_option = input("Do you want to attack the king? (yes/no): ").lower()
        if attack_option in ['yes', 'no']:
            valid_attack_option = True
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if attack_option == 'yes':
        current_health, king_health, player_damage, king_defeated, attack_type = attack_king(current_health, king_health, character_class)
        print(f"Your remaining health after attacking the king: {current_health}")
    else:
        player_damage = 0
    
    bonus = bonus_points()

    print("Game Over. Final Score:") # final score/endgame result table
    print("")
    print("")
    print(f"Character Name: {character_name}")
    print(f"Character Class: {character_class}")
    if current_health <= 0:
        print("Final Health: Dead")
    else:
        print(f"Final Health: {current_health}")
    print(f"King's Remaining Health: {king_health}")
    print(f"King Defeated: {king_defeated}")
    print(f"Total Damage Dealt to the monkey king using {attack_type}: {player_damage}")
    print(f"Bonus Points: {bonus}")

if __name__ == "__main__": # checks if Python script is being run as the main program
    play_game()