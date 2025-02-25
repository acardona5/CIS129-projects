# Module 4 Lab-4
# Amy Cardona
# 02-25-2025
# This program calculates the bonus amount for employees and store based on monthly sales and sales increase
# The program will ask the user to enter the monthly sales and sales increase
# The program will then calculate the bonus amount for the store and employees

# declare local variables
monthly_sales = int(input("Enter the Monthly sales as a whole number: "))      # store monthly sales
sales_increase = float(input("Enter the sales increase in demical form: "))     # store sales increase

emp_bonus = 0
store_bonus = 0

#Deducts the bonus amount based on the monthly sales
if monthly_sales >= 110000:
    store_bonus = 6000
elif monthly_sales >= 100000:
    store_bonus = 5000
elif monthly_sales >= 90000:
    store_bonus = 4000
elif monthly_sales >= 80000:
    store_bonus = 3000
else:
    store_bonus = 0


#deducts employee amount based on sales increase
if sales_increase >= 0.05:
    emp_bonus = 75
elif sales_increase >= 0.04:
    emp_bonus = 50
elif sales_increase >= 0.03:
    emp_bonus = 40
else:
    emp_bonus = 0

#output
print('The store bonus amount is: $'+str(store_bonus))
print('The employee bonus amount is: $'+str(emp_bonus))
if store_bonus == 6000 and emp_bonus == 75:
    print('Congratulations! you have earned the highest bonus amount!')
