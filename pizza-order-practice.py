# Day 3 Exercise

# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

price = 0
if size.upper() == "S":
    price = 15
    # print(f"It's small, Your bill is: ${price}.")
    if add_pepperoni.upper() == "Y":
        price += 2
        # print(f"Add pepperoni to small, Your bill is: ${price}.")

elif size.upper() == "M":
    price = 20
    # print(f"It's medium, Your bill is: ${price}.")

elif size.upper() == "L":
    price = 25
    # print(f"It's large, Your bill is: ${price}.")

if add_pepperoni.upper() == "Y":
    price += 3
    # print(f"Add pepperoni to medium or large, Your bill is: ${price}.")

if extra_cheese.upper() == "Y":
    price += 1
    # print(f"Add cheese, Your bill is: ${price}.")

print(f"Your final bill is: ${price}.")

