#Christine Gilbert
#CTI-110
#10/11/2026
#P3HW2 
# an exercise in formatting, make a program to ask a user
#declare and get variables
total_pay = 0
overtimep=0
overtimeh = 0
regular_pay = 0
name =input("Please enter your name: ")
hours_worked = float(input("Please enter how many hours you worked: "))
pay_rate = float(input("Please enter your pay rate: "))

#determine whether they get overtime and how much they get paid
if hours_worked > 40:
    overtimeh = hours_worked - 40
    overtimep = overtimeh * (1.5 * pay_rate)
    regular_pay = (hours_worked - overtimeh) * pay_rate
    total_pay = regular_pay + overtimep
else:
    overtimeh = 0
    overtimep = 0
    regular_pay = hours_worked * pay_rate
    total_pay = regular_pay 
    
print("-"*45)
print(f"Employee name: {name:>10}")
print()
print(f"Hours Worked{"Pay Rate":>15}{"OverTime":>15}{"OverTime Pay":>15}{"RegHour Pay":>15}{"Gross Pay":>15}")
print("-"*90)
print(f"{hours_worked:.1f}{pay_rate:>20.1f}{overtimeh:>15.2f}{overtimep:>15.2f}{regular_pay:>15.2f}{total_pay:>15.2f}")
