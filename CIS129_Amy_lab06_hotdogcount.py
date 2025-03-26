#Amy Cardona
#CIS 129 lab 6
#Hot Dog Cookout Calculator
#Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
#Design a modular program that calculates the number of packages of hot dogs and the number of 
#packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 

#input number of hot dogs needed
import math

# Main module
def main():
    total = get_total_hot_dogs()
   
    DOGS = 10  # Hot dogs in a package
    BUNS = 8   # Hot dog buns in a package

    hotdogs_left = (DOGS - total % DOGS) % DOGS# leftover hot dogs.

    min_hotdogs = math.ceil(total / DOGS) # min pachages of hotdogs

    buns_left = (BUNS - total % BUNS) % BUNS #buns leftover

    min_buns = math.ceil(total / BUNS) #minimum buns

    show_results(hotdogs_left, min_hotdogs, buns_left, min_buns)


def get_total_hot_dogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs for each person: "))
    total = people * hot_dogs_per_person
    return total


def show_results(hotdogs_left, min_hotdogs, buns_left, min_buns):
    print(f"Minimum packages of hot dogs needed: {min_hotdogs}") #min packages of hot dogs needed

    print(f"Minimum packages of hot dog buns needed: {min_buns}")#min packages of buns needed

    print(f"Hot dogs left over: {hotdogs_left}")#hot dogs left over

    print(f"Hot dog buns left over: {buns_left}")#hot dog buns left over

#main function
if __name__ == "__main__":
    main()