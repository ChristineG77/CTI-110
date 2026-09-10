# Christine Gilbert
# CTI 110
# 9/8/2026
# Calculating someone's vacation expenses

#Remember to keep all the numbers together
Budget = float(input("What is your budget for this trip: "))
Locale = input("Please enter your vacation destination: ")
Gas = float(input("How much will you be spending on gas: "))
Board = float(input("How much will you be spending on food: "))
Room = float(input("How much will you be spending on your accommodations: "))
Total = float(Gas + Board + Room) #error due to accidentally adding locale
Leftovers = float(Budget - Total) #now for the output
#make it look nice, use print() for spaces between lines
print("----Travel Expenses----")
print()
print(f"Destination: {Locale}")
print(f"Starting budget: ${Budget:.2f}")
print(f"Gas: ${Gas:.2f}")
print(f"Accommodations: ${Room:.2f}")
print(f"Food: ${Board:.2f}")
print()
print(f"At the end of your vacation at {Locale},you will have ${Leftovers:.2f} left in your budget.")
#figure out way to get the $ closer to the numbers, Answer: use f{}