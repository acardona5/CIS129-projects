# Amy Cardona
# CIS129
# Lab 3: Coffe Shop
#This program calculates the total cost of a coffee order
#based on the number of items ordered and cost per item

#variables
muffin_price = 4
coffee_price = 5
chocolateChipCookie_price = 3
tax = 6   #percentage
tax_rate = tax / 100
stars = '*' * 35

print(f'-My Coffee and Muffin Shop Receipt-')
print(stars)
#input
muffin_qty = int(input("Number of muffins bought?\n "))
coffee_qty = int(input("Number of coffees bought?\n "))
chocolateChipCookie_qty = int(input("Number of chocolate chip cookies bought?\n "))
print(stars)

print(stars)

#processing
subtotal = (muffin_qty * muffin_price) + (coffee_qty * coffee_price) + (chocolateChipCookie_qty * chocolateChipCookie_price)
addedtax = subtotal * tax_rate
total = subtotal
total = total + addedtax

#output/receipt
print(coffee_qty,'Coffees bought at $', coffee_price, 'each: $', float(coffee_qty * coffee_price))
print(muffin_qty,'Muffins bought at $', muffin_price, 'each: $', float(muffin_qty * muffin_price))
print(chocolateChipCookie_qty,'Chocolate Chip Cookies bought at $', chocolateChipCookie_price, 'each: $', float(chocolateChipCookie_qty * chocolateChipCookie_price))
print('---------')
print('Subtotal: $', float(subtotal))
print(tax, '% Tax: $',addedtax)
print('---------')
print('Total: $', total)
print('Enoy your sweet treats! ^0^')
print(stars)
