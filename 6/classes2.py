class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restuarant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
    def set_number_served(self, number):
        self.set_number_served = number
        print(f"Number of customers served set to: {self.number_served}")
    
    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"Number of customers served incremented by {increment}. Total: {self.number_served}")

McDonalds = Restaurant("McDonalds", "Fast Food")

print(f"Restaurant Name: {McDonalds.restaurant_name}, cuisine type: {McDonalds.cuisine_type}")

print(f"Number of customers served: {McDonalds.number_served}")

McDonalds.number_served = 50
print(f"Number of customers served: {McDonalds.number_served}")

McDonalds.set_number_served(100)

McDonalds.increment_number_served(30)

