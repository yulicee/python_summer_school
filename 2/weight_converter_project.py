weight = int(input("Enter the weight to be converted: "))
unit = input("(k)g or (l)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
elif unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in kg: " + str(converted))
else:
    print("Invalid input")