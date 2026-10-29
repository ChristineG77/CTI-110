#Christine Giibert
#CTI-110
#10/29/2026
import random
#Write a program that works as a self checkout machine. 
def disperse_change(changed_owed):
    money = 0.0
#get the amount from the user
# input float
#return nothing
    print(f"Change is: ${changed_owed:.2f}")
    print()
    money = changed_owed*100
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
        
        
def main():
    cost = 0.0
    amount_paid = 0.0
    changed_owed = 0.0
    print("Welcome to the self checkout sim.")
    #make a random float value for the total value of the products bought
    #ask the user how much they'll be paying
    #subtract the two and put the remainder through the disperse_change function
    cost = round(random.uniform(0.01, 100.00),2)
    print(f"You owe: ${cost:.2f}")
    amount_paid = float(input("How much money do you put in the self checkout? $"))
    changed_owed = cost - amount_paid
    disperse_change(changed_owed)
    


main()