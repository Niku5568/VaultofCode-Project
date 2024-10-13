import time
import random

class VirtualPet:
    def __init__(self, name):
        print("Welcome to VirtualPet Care Simulator")
        self.name = name
        self.happiness = 50
        self.hunger = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger = max(self.hunger - 10, 0)
            self.happiness = max(self.happiness - 2, 0)
            print(f"{self.name} is eating. Hunger decreases, but happiness slightly decreases.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        if self.happiness < 100:
            self.happiness = min(self.happiness + 10, 100)
            self.hunger = min(self.hunger + 5, 100)
            print(f"You played with {self.name}. Happiness increases, but hunger slightly increases.")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Happiness: {self.happiness}/100")
        print(f"Hunger: {self.hunger}/100")
        if self.hunger > 80:
            print(f"{self.name} is getting really hungry and is feeling sad!")
        if self.happiness < 20:
            print(f"{self.name} is feeling very sad!")

    def pass_time(self):
        self.hunger = min(self.hunger + random.randint(1, 5), 100)
        self.happiness = max(self.happiness - random.randint(1, 3), 0)

    def is_game_over(self):
        if self.hunger >= 100:
            print(f"{self.name} has become too hungry! Game Over.")
            return True
        elif self.happiness <= 0:
            print(f"{self.name} has become too sad! Game Over.")
            return True
        return False

def pet_simulator():
    pet_name = input("Name your virtual pet: ")
    pet = VirtualPet(pet_name)
    
    actions_count = 0
    
    while True:
        print("\nPet Care Menu:")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check your pet's status")
        print("4. Quit")
        
        choice = input("Choose an action (1/2/3/4): ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.check_status()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

        actions_count += 1
        if actions_count % 3 == 0: 
            pet.pass_time()

        if pet.is_game_over():
            break

pet_simulator()
