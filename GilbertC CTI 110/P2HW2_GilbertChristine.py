#Christine Gilbert
#CTI-110
#9/17/2026
#P2HW2

#make a list of input grades for many modules then find the min, max and average
#declare variables for all grades
M1 = float(input("Grade for Module 1: "))
M2 = float(input("Grade for Module 2: "))
M3 = float(input("Grade for Module 3: "))
M4 = float(input("Grade for Module 4: "))
M5 = float(input("Grade for Module 5: "))
M6 = float(input("Grade for Module 6: "))
#Make the list with the input grades
grades = [M1,M2,M3,M4,M5,M6]
#Do the math
average = sum(grades) / len(grades)
grade_sum = sum(grades)
#Print the min and max, average and sum and make it look nice
print("------------Results--------------")
print(f'{"Lowest Grade:":<20}{min(grades):.2f}')
print(f'{"Highest Grade:":<20}{max(grades):.2f}')
print(f'{"Sum of the Grades:":<20}{grade_sum:.2f}')
print(f'{"Average Grade:":<20}{average:.2f}')
print("---------------------------------")