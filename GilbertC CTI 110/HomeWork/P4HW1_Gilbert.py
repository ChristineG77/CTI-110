#Christine Gilbert
#10/25/2026
#P4HW1
#Write a program that uses a loop to ask how many scores a person wants to enter
#Then loops that many times and validates the scores that were entered
#make a variable that asks the user how many times they want to add a score
#loop for that makny iterations with an if statement check inside to validate
#add the checked score to a list

ques = int(input("How many scores do you want to enter? "))
score = []
for num in range(ques):
    scores = input("Enter score #",num+1,": ")
    if scores < 0 or scores > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        while scores <0 or scores > 100:
            scores = input("Enter score #",num+1,":")
            if scores > 0 and score < 100:
                score.append(scores)
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
    else:
        score.append(scores)
    num += 1
    
    
