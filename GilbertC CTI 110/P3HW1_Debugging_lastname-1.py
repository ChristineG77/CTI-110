#Christine Gilbert
#10/4/2026
#P3HW1
#Debugging a program
# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules


mod_1 = int(input("Enter grade for Module 1: "))
mod_2 = int(input("Enter grade for Module 2: "))
mod_3 = int(input("Enter grade for Module 3: "))
mod_4 = int(input("Enter grade for Module 4: "))
mod_5 = int(input("Enter grade for Module 5: "))
mod_6 = int(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1,mod_2, mod_3, mod_4, mod_5,mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
Sum = sum(grades)
avg = Sum / len(grades)


# determine letter grade for average
print("-"*12,"Results","-"*12)
print("Lowest Grade: ", low)
print("Highest Grade: ", high)
print("Sum of Grades: ", Sum)
print("Average: ", avg)
print("-"*31)

if avg >= 90:
 print('Your grade is: A')
elif avg > 80 and avg < 90 :
 print('Your grade is: B')
elif avg > 70 and avg < 80 :
 print('Your grade is: C')
elif avg > 60 and avg < 70 :
 print('Your grade is: D')
else:
 print('Your grade is: F') # TO DO: finish this





