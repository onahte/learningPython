# This program takes your weight in lbs or kg and converts the measurement.

weight = int(input("What is your weight? "))
if weight < 1 or weight > 2000:
    print("Please enter a valid weight.")
    quit()

weight_unit = input("(L)bs or (K)g: ")

while weight > 1 and weight < 2000:
    if weight_unit.lower() == "l":
        weight *= .453
        weight_unit = "kg"
        print(f"Your weight is {weight} {weight_unit}")
    elif weight_unit.lower() == "k":
        weight /= .453
        weight_unit = "lbs"
        print(f"Your weight is + {weight} {weight_unit}")
    else:
        print("Please enter a valid unit of weight.")
        break