weight = input("What is your weight? ")
lbs_or_kg = input("lbs or kg? ")

if lbs_or_kg.lower() == "lbs":
    convented = int(weight) * 0.45
    print(f"You weight is {convented} kg")

if lbs_or_kg.lower() == "kg":
    convented = int(weight) / 0.45
    print(f"You weight is {convented} lbs")