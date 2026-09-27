#Christine Giibert
#CTI-110
#9/27/2026

#Write a program that shows the smallest number of dollars and coins for an amount of money
def main():
#get the amount from the user
    money = float(input("Please enter how much money you're looking to break down: "))
    money = money*100
#check how many dollars can be taken from the amount
    if money > 0.00:
        if money >= 100:
            dollar = money//100
            money = money % 100
            print(dollar," Dollars")
        elif money <= 199:
            dollar = money//100
            money = money % 100
            print(dollar," Dollar")
        else:()

        if money <= 99:
            quarter = money//25
            money = money%25
            print(quarter," Quarters")
        elif money == 25:
            print("1 Quarter")
        else:()
        if money <= 99:
            dime = money//10
            money = money%10
            print(dime," Dimes")
        elif money == 10:
            print("1 Dime")
        else:()
        if money <= 99:
            quarter = money//5
            money = money%5
            print(quarter," Nickels")
        elif money == 5:
            print("1 Nickel")
        else:()
        if money <= 99:
                penny = money//1
                money = money%1
                print(penny," Pennies")
        elif money == 1:
                print("1 Penny")
        else:()
    else:
        print("You didn't enter an amount")

#check how many quarters can be taken from the amount

#check how many dimes can be taken from the amount

#Check how many nickels can be taken from the amount

#check how many pennies can be taken from the amount

#display how much of each coin or dollar 
main()