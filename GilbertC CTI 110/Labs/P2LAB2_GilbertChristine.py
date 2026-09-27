#Christine  Gilbert
#CTI-110
#9/17/2026
#We are making a dictonary, and when you input the right key words you should get the information in the dictionary
#Then calculate how much gas a person would need for that car to drive a certain amount of miles

#Declare the variables and dictonary vaules
Cars = {'Camero':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}
#get the car input from user
keycar = input("Please choose a car to find its miles per gallon value for a 'Camero, Prius, Model S or Silverado': ")
print("The ",keycar," gets ",(Cars[keycar]),"mpg")
#ask how many miles they plan to drive the car for and calculate how many gallons it would be to drive that far
miles = float(input(f"How many miles will you drive the {keycar}? "))
gallons = float(miles / (Cars[keycar]))
#present the final calculation and answer
print(f"{gallons:.2f} gallons is how much you'll need to drive {miles} miles")
#print(Cars['Camero']) how to print the values