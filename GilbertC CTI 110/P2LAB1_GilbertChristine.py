# Christine Gilbert
# CTI - 100
# 9/10/2026
# Let's do geometry and math with circles!

# Display the equation for the different Circle Formulas
print("Diameter = 2r (where r is the radius)")
print("Circumference = 2pi r (where pi is 3.14)")
print("Area = pir^2")
# Ask the user for the radius of the circle in whole numbers or decimal, no radians (try coding radians later?)
radius = float(input("Please enter your value of pi in whole numbers or decimal, no radians please: "))
# Show your work
Dia = float(2 * radius)
Cir = float(2 * 3.14 * radius)
Area = float(3.14 * radius ** 2)
# Present the math
print(f"Diameter is {Dia:.2f}, Circumference is {Cir:.2f}, and the Area is {Area:.2f}, using this radius value and rounding up to the second decimal space.")
# Explain the math!