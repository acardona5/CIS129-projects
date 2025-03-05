# Amy Cardona
# CIS129
# Lab 5: Bottle count

totalBottles = 0 
counter = 0
todayBottles = 0
totalPayout = 0
keepGoing = "y"

while keepGoing == "y":
    counter = 1
    days = 7

    while counter <= days:
        todayBottles = int(input(f"Enter number of bottles for day #{counter}: "))
        totalBottles += todayBottles
        counter += 1

    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE

    print(f"\nThe total number of bottles collected is {totalBottles}")
    print(f"The total paid out is ${totalPayout:.2f}")

    print("\nDo you want to enter another week’s worth of data?")
    print("Enter y or n")
    keepGoing = input()
