class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def __repr__(self):
        return(f"Restaurant Name: {self.name}\nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(f"\n{self.name} offers the following ice cream flavors: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

def main():
    flavors = [
        "Unicorn Dream Delight", 
        "Chocolate Dragon Scales", 
        "Strawberry Ninja Surprise", "Minty Elf Magic", 
        "Cookie Monster Mashup", 
        "Rainbow Fairy Swirl", 
        "Alien Goo", "Pirate's Treasure", 
        "Mystic Mermaid Lagoon", 
        "Wizard's Power Potion"
        ]
    ice_cream_stand = IceCreamStand("Whimsical Treats", "Fantasy Desserts", flavors)

    print(ice_cream_stand)
    ice_cream_stand.display_flavors()

if __name__ == "__main__":
    main()