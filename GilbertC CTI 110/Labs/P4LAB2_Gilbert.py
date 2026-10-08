#Christine Gilbert
#10/8/2026
#warmups
""""
for number in (1,2,3,4):
    print(number)
for number in range (5):
    print(number)
for beer in range (99,0,-1):
    print(beer,"bottles of beer on the wall!")  
"""
#counting loop
"""print("7's times table")
for mult in range (1,13):
    print(7*mult)"""
#set up variables ask the user for their chosen integer (0-12) validate loop
multiplier = int(input("Enter a number 0-12: "))
#print the times table header, print the times table loop
while multiplier < 0 or multiplier > 12:
    print("That is not a valid number")
    multiplier = int(input("Enter a number 0-12: "))

print("Multiplication Table")
print("-"*20)

for number in range (1,13):
    print(f"{multiplier} * {number} = {number*multiplier}")
    #print(number,"\t",number*multiplier)