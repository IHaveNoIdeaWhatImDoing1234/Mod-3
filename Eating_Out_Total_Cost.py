totalMealCost = float(input("Please enter the total charge for the food: ")) #User input total cost of the food purchased
tipAmount = totalMealCost * 0.18 #Multiply totalMealCost by 18% for tip
salesTax = totalMealCost * 0.07 #Multiply totalMealCost by 7% for sales tax
totalCost = (totalMealCost + tipAmount + salesTax) #Calculate the total cost to be charged by adding together totalMealCost, tipAmount, and Sales Tax

print("Cost of the meal:$",format(totalMealCost,",.2f")) #Print value entered by user for cost of meal, formatted to 2 decimal places
print("Tip Amount:$",format(tipAmount,",.2f")) #Print value of tip applied, formatted to 2 decimal places
print("Sales Tax:$",format(salesTax,",.2f")) #Print value of sales tax applied, formatted to 2 decimal places
print("Total cost to be charged:$",format(totalCost,",.2f")) #Print value total value of cost of meal, tip, and sales tax added together, formatted to 2 decimal places
