# Amy Cardona
# CIS129
# Lab 3: Coffee Shop
#This program calculates the total cost of a coffee order
#based on the number of items ordered and cost per item

#variables
muffin_price = 4
coffee_price = 5
chocolateChipCookie_price = 1
icedTea_price = 3.50
tax = 6   #percentage
tax_rate = tax / 100
stars = '*' * 35

print(f'-My Coffee and Muffin Shop Receipt-')
print(stars)
#input
muffin_qty = int(input("Number of muffins bought?\n "))
coffee_qty = int(input("Number of coffees bought?\n "))
chocolateChipCookie_qty = int(input("Number of chocolate chip cookies bought?\n "))
icedTea_qty = int(input("Number of iced teas bought?\n "))
print(stars)

print(stars)

#processing
subtotal = (muffin_qty * muffin_price) + (coffee_qty * coffee_price) + (chocolateChipCookie_qty * chocolateChipCookie_price) + (icedTea_qty * icedTea_price)
addedtax = subtotal * tax_rate
total = subtotal
total = total + addedtax

#output/receipt
print(str(coffee_qty) + 'Coffees bought at $' + str(coffee_price) + 'each: $' + str(coffee_qty * coffee_price))
print(muffin_qty,'Muffins bought at $', muffin_price, 'each: $', float(muffin_qty * muffin_price))
print(chocolateChipCookie_qty,'Chocolate Chip Cookies bought at $', chocolateChipCookie_price, 'each: $', float(chocolateChipCookie_qty * chocolateChipCookie_price))
print(icedTea_qty,'Iced Teas bought at $', icedTea_price, 'each: $', float(icedTea_qty * icedTea_price))

print('---------')
print('Subtotal: $', float(subtotal))
print(tax, '% Tax: $',float(addedtax))
print('---------')
print('Total: $', total)
print('Enoy your sweet treats! ^0^')
print('Please come again!')
print(stars)
