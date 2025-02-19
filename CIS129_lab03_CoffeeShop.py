# Amy Cardona
# CIS129
# Lab 3: Coffe Shop
#This program calculates the total cost of a coffee order
#based on the number of items ordered and cost per item

#variables
muffin_price = 4
coffee_price = 5
tax = 6   #percentage
tax_rate = tax / 100
stars = '*' * 35

print(f'-My Coffee and Muffin Shop Receipt-')
print(stars)
#input
muffin_qty = int(input("Number of muffins bought?\n "))
coffee_qty = int(input("Number of coffees bought?\n "))
print(stars)

print(stars)

#processing
subtotal = (muffin_qty * muffin_price) + (coffee_qty * coffee_price)
addedtax = subtotal * tax_rate
total = subtotal
total = total + addedtax

#output/receipt
print(str(coffee_qty) + 'Coffees bought at $' + str(coffee_price) + 'each: $' + str(float(coffee_qty * coffee_price)))
print(str(muffin_qty) + 'Muffins bought at $' + str(muffin_price) + 'each: $' + str(float(muffin_qty * muffin_price)))
print('---------')
print('Subtotal: $' + str(float(subtotal)))
print(str(tax) + '% Tax: $' + str(float(addedtax)))
print('---------')
print('Total: $' + str(total))
print('Enoy your sweet treats! ^0^')
print(stars)
