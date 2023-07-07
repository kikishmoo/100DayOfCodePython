# Day 2 Project
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = float(input("Welcome to the tip calculator.\nWhat was the tatal bill? $"))
percent = float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))
total_with_tip = total * (1 + percent)
# bill_per_person = round(total_with_tip/people, 2)
bill_per_person = "{:.2f}".format(total_with_tip/people)
print(f"Each person should pay: ${bill_per_person}")
