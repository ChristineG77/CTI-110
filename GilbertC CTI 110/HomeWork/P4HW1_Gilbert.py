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
    print("Enter score #",num+1,": ")
    scores = int(input())
    if scores < 0 or scores > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        while scores < 0 or scores > 100:
            print("Enter score #",num+1,":")
            scores = int(input())
            if scores > 0 and scores < 100:
                score.append(scores)
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
    else:
        score.append(scores)
    num += 1
print("------------Results--------------")
print(f'{"Lowest Grade:":<20}{min(score):.2f}')
# drop the lowest score off the list
score.remove(min(score))
print(f'{"Score List:":<20}{score}')
average = sum(score) / len(score)
print(f'{"Average Grade:":<20}{average:.2f}')
#letter grade
if average > 90:
    grade = "A"
elif average <90 and average > 79:
    grade = "B"
elif average < 80 and average > 69:
    grade = "C"
elif average < 70 and average > 59:
    grade = "D"
else:
    grade = "F"
print(f'{"Grade":<20}{grade}')
print("---------------------------------")
    
