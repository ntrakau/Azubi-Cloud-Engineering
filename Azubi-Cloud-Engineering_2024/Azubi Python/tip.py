#Prompt the user for input = Charge for food

x = float(input("Charge for food = $"))

#Declare variables = Tip and Sales tax

y = float((18 * x ) / 100)
z = float((7 * x)/ 100)

#Calculate the percentages

print(f"Tip = ${y:.2f}")
print(f"Sales tax = ${z:.2f}")
#Create a variable tha sums all the calculated variables together print = Grand Total

print(f"Grand total = ${x + y + z:.2f}")