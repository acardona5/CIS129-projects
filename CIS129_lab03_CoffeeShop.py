# Amy Cardona
# CIS129
# Lab 3: Coffe Shop
#This program calculates the total cost of a coffee order
#based on the number of items ordered and cost per item

#variables
muffin_price = 4
coffee_price = 5
tax = 6
tax_rate = tax / 100
stars = '*' * 35

print(stars)
#input
muffin_qty = int(input("Number of muffins bought\n "))
coffee_qty = int(input("Number of coffees bought?\n "))
print(stars)

print(stars)

#processing
subtotal = (muffin_qty * muffin_price) + (coffee_qty * coffee_price)
addedtax = subtotal * tax_rate
total = subtotal
total = total + addedtax

#output/receipt
print(coffee_qty,'Coffees bought at $', coffee_price, ' each: $', coffee_qty * coffee_price)
print(muffin_qty,'Muffins bought at $', muffin_price, ' each: $', muffin_qty * muffin_price)
print(tax, '% Tax: $', addedtax)
print('---------')
print('Total: $', total)
print(stars)