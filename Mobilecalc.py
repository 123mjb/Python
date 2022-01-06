# 12 Mobile Costs calculator.py


# Display title for program
print("Welcome to the Mobile Phone Costs Calculator")
print("********************************************")

# Add blank line before input using \n print ("\n")I
print("\n")
network = input("Please enter which network you use? ")
# input number of minutes and texts used this month
minutes_used_in_month = input("How many minutes have you used this month? ") 
texts_used_in_month = input("How many texts have you used this month? ")
# arithmetic and rounding
minutes_cost_per_month = round(float(minutes_used_in_month) * 0.10, 2)
texts_cost_per_month = round(float(texts_used_in_month) * 0.05, 2)
# declare new variables and VAT constant
total_bill = minutes_cost_per_month + texts_cost_per_month
VAT_rate = 0.2
VAT_cost = round(total_bill * VAT_rate, 2)
# output
print("\nYour monthly minute costs with", network, "is £", minutes_cost_per_month)
print ("Your monthly text costs with", network, "is £", texts_cost_per_month)
print("\nYour total monthly bill is €", total_bill)
print("VAT = £", VAT_cost) 
print("	")
print("\nYour total monthly bill including VAT is £", round(total_bill + VAT_cost,2))
# Holds the screen until ENTER pressed to read results if using windows console input("\nPress ENTER to exit the program")
