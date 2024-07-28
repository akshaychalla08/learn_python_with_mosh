weight = int(input("Please enter weight: "))
units = input("(L)bs or (K)g: ")

if units.upper() == "L":
    print(f"Weight is {weight * 0.5} kg")
elif units.upper() == "K":
    print(f"Weight is {weight * 1.5} pounds")
else:
    print("Please select valid unit")
