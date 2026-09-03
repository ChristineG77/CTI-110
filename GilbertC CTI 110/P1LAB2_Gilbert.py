#Christine Gilbert
#CTI 110
#9/3/2026

#Fictional Store --  pick three things
# product_name, product_count,product_cost

#Change these to own values
#this below is hardcoding, and it sets vaules directly
#product_name = "Squeeb"     #string are characters
#product_count = 50          #integers are whole numbers
#product_cost = 25.30        #double have decimal

#now ask for the user input
print("STORE_STARTUP")
print("_" * 10) # ten _ in a row
#processing
product_name=input("Enter product name: ")
product_count=int(input("Enter product count: "))
product_cost=float(input("Enter unit cost: "))
#output
print("CUSTOMER INTERFACE")
print("_" * 10)
print("Welcome to the",product_name,"store!")
# for later -- f string with {vsriable:.2f} is the magic word to get 2 decimals. You have to put it infront of whereever the {} is being used or use {} for all the variables
print("We have",product_count,product_name,f"at ${product_cost:.2f} each.")
total = product_count * product_cost
print(f"Total is: ${total:.2f}.")