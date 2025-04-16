# Define the Pet class as specified
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 10
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        self.energy = min(10, self.energy + 5)

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Create a pet object and call its methods to test functionality
if __name__ == "__main__":
    pet = Pet("Buddy")
    
    # Test eat method
    pet.eat()
    
    # Test sleep method
    pet.sleep()
    
    # Test play method
    pet.play()
    
    # Test get_status method
    pet.get_status()
    
    # Test train method
    pet.train("roll over")
    
    # Test show_tricks method
    pet.show_tricks()

