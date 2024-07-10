import math

# Initial coodinates
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Print list of coordinates
print("Initial list of coordinates: ")
print(coordinates)

# Prompt user to add a new coordinate (x, y) to the list
new_x = int(input("Enter the x coordinate: "))
new_y = int(input("Enter the y coordinate: "))
new_coordinate = (new_x, new_y)
coordinates.append(new_coordinate)

# Print updated list
print(coordinates)

# Calculate distance of each coordinate from origin (0,0)
distances = [math.sqrt(x**2 + y**2) for x, y in coordinates]

# Find and print the coordinates with the max distance from the origin
max_distance = max(distances)
max_distance_index = distances.index(max_distance)
max_distance_coordinate = coordinates[max_distance_index]

print(f"\nThe coordinate with the max distance from the origin is: {max_distance_coordinate}")

# Print the coordinates along with their distances from the origin in a well-formatted manner
print("\nCoordinates and their distances from the origin: ")
for coordinates, dist in zip(coordinates, distances):
    print(f"{coordinates}, {dist:.2f}")