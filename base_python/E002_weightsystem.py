# see if a weight is in pounds or kilograms, conversion rate = 0.45, print the result

weight = float(input("Your weight: "))
weightSystem = str(input("K for kilograms, L for Pounds: "))

if weightSystem.upper() == "K":
    otherWeightSystem = weight / 0.45
    print("Your weight in Pounds is ", otherWeightSystem)
elif weightSystem.upper() == "L":
    otherWeightSystem = weight * 0.45
    print("Your weight in Kilograms is ", otherWeightSystem)
else:
    print("Wrong Input, try again.")
