#Christine Gilbert
#10/25/2026
#P4HW1
#Make a program to input employees names, hours and work rate pay then cauclate the total amount of overtime and reagular pay for the week
total_pay = 0
overtimep=0
overtimeh = 0
regular_pay = 0
total_over = 0
total_regular = 0
employee_count = 0
name = "empty"
#determine whether they get overtime and how much they get paid
while name != "Done":
    name =input("Please enter your name: ")
    if name  == "Done":
        break
    hours_worked = float(input("Please enter how many hours you worked: "))
    pay_rate = float(input("Please enter your pay rate: "))
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
    employee_count =+ 1
    total_over += overtimep
    total_regular += regular_pay
print("Total number of employess entered:",employee_count)
print(f"Total amount paid for overtime: {total_over:.2f}")
print(f"Total amount paid for regular hours: {total_regular:.2f}")
gross_total = total_over + total_regular
print(f"Total amount paid in gross: {gross_total:.2f}")
print("Thank you for using the employee portal.")