class User:
    def __init__(self, first_name, last_name, age, occupation, city, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.city = city
        self.country = country
    
    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")
        print(f"Location: {self.city}, {self.country}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

users = [
    User("John", "Miller", "35", "Teacher", "London", "UK"),
    User("Sarah", "Walker", "56", "Baker", "Chicago", "USA"),
    User("Debbie", "Goode", "23", "Student", "New York", "USA")
]

for user in users:
    user.describe_user()
    user.greet_user()
    print()