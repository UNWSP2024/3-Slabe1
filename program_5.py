# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

cost = 3.5

chili_dog = input("Would you like a chili dog? (y or n) ")

if chili_dog == 'y':
    cost += 1

cheese = input("Would you like cheese? (y or n) ")

if cheese == 'y':
    cost += 0.5

peppers = input("Would you like peppers? (y or n) ")

if peppers == 'y':
    cost += 0.75

grilled_onions = input("Would you like grilled onions? (y or n) ")

if grilled_onions == 'y':
    cost += 1

print(f"Cost of Hot Dog: {cost}")

tax = cost*0.07

print(f"tax: {tax:.2f}")

total_cost = tax + cost

print(f"total cost: {total_cost:.2f}")



