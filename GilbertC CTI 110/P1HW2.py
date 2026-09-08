# Christine Gilbert
# CTI 110
# 9/8/2026
# Calculating someone's vacation expenses

Budget = float(input("What is your budget for this trip: "))
Locale = input("Please enter your vacation destination: ")
Gas = float(input("How much will you be spending on gas: "))
Board = float(input("How much will you be spending on food: "))
Room = float(input("How much will you be spending on your accommodations: "))
Total = float(Gas + Board + Room)
Leftovers = float(Budget - Total)
print("----Travel Expenses----")
print()
print("Destination: ",Locale)
print("Starting budget: $",Budget)
print("Gas: $",Gas)
print("Accommodations: $",Room)
print("Food: $",Board)
print()
print("At the end of your vacation at",Locale,",you will have $",Leftovers,"left in your budget.")