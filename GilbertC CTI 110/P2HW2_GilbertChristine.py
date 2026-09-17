#Christine Gilbert
#CTI-110
#9/17/2026

#make a list of input grades for many modules then find the min, max and average
#declare variables for all grades
M1 = float(input("Grade for module 1: "))
M2 = float(input("Grade for module 2: "))
M3 = float(input("Grade for module 3: "))
M4 = float(input("Grade for module 4: "))
M5 = float(input("Grade for module 5: "))
M6 = float(input("Grade for module 6: "))
grades = {M1,M2,M3,M4,M5,M6}
print(f'{"Lowest Grade":<20}{min(grades)}')