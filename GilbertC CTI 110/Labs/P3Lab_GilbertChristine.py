#Christine Giibert
#CTI-110
#9/27/2026

#Write a program that shows the smallest number of dollars and coins for an amount of money
def main():
#get the amount from the user
    money = float(input("Please enter how much money you're looking to break down: "))
    money = money*100
#cheack if there is an amount entered
    if money > 0.00:
#check how many dollars can be taken from the amount
        if money >= 100:
            dollar = money//100
            money = money % 100
            if dollar >= 2:
                 print(dollar," Dollars")
            elif dollar == 1:
                 print(dollar," Dollar")
        else:()
#check how many quarters can be taken from the amount
        if money <= 99:
            quarter = money//25
            money = money%25
            if quarter >= 2:
                print(quarter," Quarters")
            elif quarter == 1:
                    print(quarter," Quarter")
        else:()
#check how many dimes can be taken from the amount
        if money <= 99:
            dime = money//10
            money = money%10
            if dime >= 2:
                 print(dime," Dimes")
            elif dime == 1:
                print(dime," Dime")
        else:()
#Check how many nickels can be taken from the amount
        if money <= 99:
            nickel = money//5
            money = money%5
            if nickel >= 2:
                print(nickel," Nickels")
            elif nickel == 1:
                print(nickel," Nickel")
        else:()
#check how many pennies can be taken from the amount
        if money <= 99:
                penny = money//1
                money = money%1
                if penny >= 2:
                    print(penny," Pennies")
                elif penny == 1:
                    print(penny," Penny")
        else:()
    else:
        print("No change")

main()