import random
import time

class VirtualPlant:
    def __init__(self, name):
        self.name = name
        self.water_level = 5
        self.health = 10
        self.growth_stage = 0

    def water_plant(self, amount):
        self.water_level += amount
        print(f"\n{self.name} was watered with {amount} units of water!")
        self._update_health()

    def prune_plant(self):
        self.health += 2
        print(f"\n{self.name} was pruned and looks tidier now!")

    def replant(self):
        self.health += 2
        print(f"\n{self.name} was replanted into a new pot!")

    def fertilize(self):
        self.health += 2
        self.water_level += 2
        print(f"\n{self.name} was fertilized. Health and water level increase!\n")

    def decorate(self):
        self.health += 1
        print(f"\n{self.name} was decorated and looks even nicer now!\n")

    def use_special_water(self):
        self.water_level += 5
        print(f"\n{self.name} was watered with special water. Water level increases significantly!\n")

    def _update_health(self):
        if self.water_level > 3:
            self.health += 1
            self.growth_stage += 1
            if self.growth_stage > 5:
                self.growth_stage = 5
            print(f"{self.name} looks healthier and grew a bit!\n")
        elif self.water_level < 3:
            self.health -= 1
            print(f"{self.name} looks unhealthy due to low water.\n")

    def _random_events(self):
        events = {
            'pests': [-2, -1, "Oh no! Pests have attacked your plant, reducing its health and water level!"],
            'disease': [-3, 0, "Uh-oh! Your plant caught a disease, reducing its health!"],
            'rain': [0, 2, "Yay! It rained, and your plant got some extra water!"],
            'sunny': [1, 0, "Nice! The sunny weather made your plant healthier!"]
        }
        event_probability = random.randint(1, 5)
        if event_probability == 1:
            event = random.choice(list(events.keys()))
            self.health += events[event][0]
            self.water_level += events[event][1]
            print(f"\nRandom Event: {events[event][2]}\n")

    def pass_time(self):
        self.water_level -= 1
        self._update_health()
        self._random_events()

def main():
    print("Welcome to the Virtual Plant Care App!\n")
    plant_name = input("What would you like to name your plant? ")
    my_plant = VirtualPlant(plant_name)

    currency = 10
    pesticide = 1
    medicine = 1
    fertilizer = 1
    decor = 1
    special_water = 1

    while my_plant.health > 0:
        print(f"{my_plant.name}'s current water level: {my_plant.water_level}")
        print(f"{my_plant.name}'s current health: {my_plant.health}")
        print(f"{my_plant.name}'s growth stage: {my_plant.growth_stage}")
        print(f"Your current balance: {currency} coins")
        print(f"Your resources - Pesticide: {pesticide}, Medicine: {medicine}, Fertilizer: {fertilizer}, Decor: {decor}, Special Water: {special_water}\n")

        action = input("What would you like to do? (water/prune/replant/pesticide/medicine/fertilize/decorate/special_water/shop/nothing) ").lower()

        if action == "water":
            water_amount = int(input("How much would you like to water your plant? "))
            my_plant.water_plant(water_amount)
        elif action == "prune":
            my_plant.prune_plant()
        elif action == "replant":
            my_plant.replant()
        elif action == "pesticide":
            if pesticide > 0:
                pesticide -= 1
                my_plant._update_health()
            else:
                print("\nYou have no pesticide left. Visit the shop to buy more.\n")
        elif action == "medicine":
            if medicine > 0:
                medicine -= 1
                my_plant._update_health()
            else:
                print("\nYou have no medicine left. Visit the shop to buy more.\n")
        elif action == "fertilize":
            if fertilizer > 0:
                fertilizer -= 1
                my_plant.fertilize()
            else:
                print("\nYou have no fertilizer left. Visit the shop to buy more.\n")
        elif action == "decorate":
            if decor > 0:
                decor -= 1
                my_plant.decorate()
            else:
                print("\nYou have no decor items left. Visit the shop to buy more.\n")
        elif action == "special_water":
            if special_water > 0:
                special_water -= 1
                my_plant.use_special_water()
            else:
                print("\nYou have no special water left. Visit the shop to buy more.\n")
        elif action == "shop":
            print(f"\nWelcome to the shop! Your current balance: {currency} coins.")
            print("1. Pesticide: 5 coins")
            print("2. Medicine: 7 coins")
            print("3. Fertilizer: 4 coins")
            print("4. Decor: 3 coins")
            print("5. Special Water: 6 coins")
            shop_action = input("What would you like to buy? (pesticide/medicine/fertilizer/decor/special_water/exit) ").lower()
            if shop_action == "pesticide" and currency >= 5:
                pesticide += 1
                currency -= 5
                print("\nYou bought pesticide!\n")
            elif shop_action == "medicine" and currency >= 7:
                medicine += 1
                currency -= 7
                print("\nYou bought medicine!\n")
            elif shop_action == "fertilizer" and currency >= 4:
                fertilizer += 1
                currency -= 4
                print("\nYou bought fertilizer!\n")
            elif shop_action == "decor" and currency >= 3:
                decor += 1
                currency -= 3
                print("\nYou bought decor!\n")
            elif shop_action == "special_water" and currency >= 6:
                special_water += 1
                currency -= 6
                print("\nYou bought special water!\n")
            elif shop_action == "exit":
                print("\nYou left the shop.\n")
            else:
                print("\nInsufficient coins or invalid option.\n")
        elif action == "nothing":
            print(f"\nYou chose not to do anything with {my_plant.name}.\n")

        print("Time passes...\n")
        my_plant.pass_time()
        if my_plant.health > 0:
            currency += 1
        time.sleep(2)

        # Additional Special Event Logic
        event_probability = random.randint(1, 10)
        if event_probability == 1:
            print("\nSpecial Event: A rare meteor shower is visible tonight!")
            wish_action = input("Do you want to make a wish for your plant? (yes/no) ").lower()
            if wish_action == "yes":
                wish_effect = random.choice(["health", "water", "currency"])
                if wish_effect == "health":
                    my_plant.health += 3
                    print("Your wish was heard! Your plant looks healthier!")
                elif wish_effect == "water":
                    my_plant.water_level += 3
                    print("Your wish was heard! Rain showered your plant with extra water!")
                elif wish_effect == "currency":
                    currency += 5
                    print("Your wish was heard! You found some extra coins!")
            else:
                print("You chose not to make a wish.\n")

    print(f"Oh no! {my_plant.name} has perished due to lack of care.")

if __name__ == "__main__":
    main()
