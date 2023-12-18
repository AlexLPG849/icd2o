import random

def get_player_input(assets):
    while True:
        # Get input for chicken biryani, advertising signs, and price per cup
        while True:
            try:
                biryani_cups = int(input("Enter the number of cups of chicken biryani to make (up to 50): "))
                if biryani_cups < 0 or biryani_cups > 50:
                    print("Number of cups must be between 0 and 50. Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the number of cups.")

        while True:
            try:
                advertising_signs = int(input("Enter the number of advertising signs to buy (up to 10): "))
                if advertising_signs < 0 or advertising_signs > 10:
                    print("Number of advertising signs must be between 0 and 10. Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the number of advertising signs.")
        
        while True:
            try:
                price_per_cup = float(input("Enter the price per cup of chicken biryani (in cents): "))
                if price_per_cup < 0:
                    print("Sell price cannot be negative. Please enter a valid number.")
                elif price_per_cup > 50:
                    print("Sell price per cup cannot exceed 50 cents. Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the sell price.")

        # Check if player has enough assets
        cost_biryani = biryani_cups * 5  # Each cup costs 5 cents to make
        cost_signs = advertising_signs * 15  # Each sign costs 15 cents
        total_cost = cost_biryani + cost_signs

        if total_cost > assets:
            print("Insufficient funds. Cannot afford to make chicken biryani and buy signs. Please try again.")
        else:
            # Updated assets after spending money on cups of biryani and advertising signs
            assets -= total_cost
            return biryani_cups, advertising_signs, price_per_cup, assets

def simulate_day(biryani_cups, advertising_signs, price_per_cup, assets, weather, day_counter):
    # The Zaza Monster attacks on day 6 with a 13% chance
    if day_counter == 6 and random.random() < 0.13:
        print("Oh no! Zaza Monster has attacked you on day 6 and stolen all your money! You're bankrupt!")
        assets = 0
        return 0, 0, assets

    # Adjust the number of cups sold based on weather
    if weather == "sunny":
        cups_sold = max(15, biryani_cups - 5)  # Sell between 15 and the user-inputted amount
    else:
        cups_sold = min(random.randint(10, biryani_cups - 10), biryani_cups)  # Random number from 10 to the amount - 10 given when it's rainy

    # Checks capacity of cups to see if its over 50
    cups_sold = min(cups_sold, 50)

    revenue = cups_sold * min(price_per_cup, 50)  # Ensure sell price does not exceed 50 cents

    # Update assets based on revenue
    assets += revenue

    return cups_sold, revenue, assets

def display_day_costs(biryani_cups, advertising_signs):
    print(f"\nDay Costs:")
    print(f"Cost to make a cup of chicken biryani: {biryani_cups * 5} cents")
    print(f"Cost to buy an advertising sign: {advertising_signs * 15} cents")

def get_weather_intro(weather):
    if weather == "sunny":
        return "The weather is sunny. Many people are likely looking for a delicious meal."
    else:
        return "The weather is rainy. Not many people are looking for a hot meal."

def get_weather():
    # Randomly determine the weather as either "sunny" or "rainy"
    return random.choice(["sunny", "rainy"])

def main():
    # Set initial assets
    starting_assets = 200  # $2 in cents
    # Get starting money from the player
    while True:
        try:
            print("Hi there🖐, welcome to the town of Chicken Biryani Lovers!🥘")
            print("In this small town, you are in charge of a biryani stand and all of its costs.") 
            print("You will need to make 3 decisions daily:")
            print("how many cups you make, how many advertising signs to make, and what price to set the biryani at.")
            print("The profits are the difference between the income and your expenses.")
            print("Keep track of your assets so that you don't spend more than you have.")
            assets = int(input("Enter the amount of money to start with (between $2 and $5, enter in hundreds (100 cent = 1 dollar)): ") or starting_assets)
            if 200 <= assets <= 500:
                break
            else:
                print("Invalid amount. Please enter an amount between $2 and $5 (plz enter in hundreds).")
        except ValueError:
            print("Invalid input. ENTER A PROPER NUMBER!!!")

    print(f"Your starter assets is: ${assets / 100:.2f}")

    # Initialize day counter
    day_counter = 1

    while day_counter <= 15:
        print(f"\nDay {day_counter}")

        # Get the weather for the day, rng of sunny and rainy
        weather = get_weather()
        print(get_weather_intro(weather))

        # Get player input with validation
        biryani_cups, advertising_signs, price_per_cup, assets = get_player_input(assets)

        # Display day costs
        display_day_costs(biryani_cups, advertising_signs)

        # Simulate the day
        cups_sold, revenue, assets = simulate_day(biryani_cups, advertising_signs, price_per_cup, assets, weather, day_counter)

        # Display recap for the day
        print("\nDay Recap:")
        print(f"Cups of chicken biryani made: {biryani_cups}")
        print(f"Advertising signs bought: {advertising_signs}")
        print(f"Cups sold: {cups_sold}")
        print(f"Revenue: ${revenue / 100:.2f}")  # Convert revenue back to dollars
        print(f"Current assets: ${assets / 100:.2f}")  # Convert assets back to dollars

        # Increment the day counter every time you say "yes"
        day_counter += 1

        # Ask if the player wants to continue the game or stop
        user_input = input("\nDo you want to continue to the next day? (yes/no, not entering yes or no will result in an automatic game end): ").lower()
        if user_input != 'yes':
            break

    # Display final results after player chooses to end game or keep going until day 15
    print("\nGame Over! Final Results🎉:")
    print(f"Total cash made: ${assets / 100:.2f}")
    print(f"Total cups of Chicken Biryani made🥘: {biryani_cups * (day_counter - 1)}")
    print(f"Total signs made📋: {advertising_signs * (day_counter - 1)}")
    profit_loss_percentage = ((assets - starting_assets) / starting_assets) * 100
    print(f"Profit/Loss💸💰💶💵💴💷: {profit_loss_percentage:.2f}%")
    print(f"Day reached⏱: {day_counter - 1}")

if __name__ == "__main__":
    main()

# New Functions:

# ValueError -  It is raised when a function receives an argument of the correct data type but with an invalid value. 
#            -  Essentially, it indicates that the function or operation couldn't proceed with the given argument because the value is not appropriate for that context.

# Try/Except - They allow you to catch and handle errors that might occur during the execution of your code.

# \n - \n is used to seperate words/characters in a string, making the separated part on a new line.

# Max/Min    - Max determines a maximum value given in a sequence, Min does the opposite of Max