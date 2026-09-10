#print(chr(65)) #chr is character and the number is the associated letter or symbol on the keyboard from 36-126 using ASCII, there are things above 126
#5print(ord('A')) #ord is the ASCII value, with a string character after will give you the number of that character
#print(ord('A','D','a','c')) ord only works with one argument (one value at a time)
print("32" + chr(176) + "Farenheit") # Using '+' is another way to add variables and string together in a print statement, but there needs to be a space between the plus and the variable or string
n=(input("Please enter the letter or symbol whose ASCII you wish to know: "))
print(ord(n))
num,num2,fnum = int,int,int
num=7
num2=int(input())
fnum = num - num2  #use spaces inbetween math operands, these operands are +,-,*,/,//,**(exponet),%(remainder)
print(num,"multiplied by",num2,"equals",fnum) #/n is for two line spaces