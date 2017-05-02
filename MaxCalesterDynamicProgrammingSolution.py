#   MaxCalester - Main Program
#   Developed By: Ibrahima Dieye and Andy Han
#   Data Provided By: Andy Han and Lang Li
#   April 26th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis

# Importing necessary modules and libraries

import csv
import time
from functools import lru_cache


# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.
restaurant_name = []  # List of the names that are on the McDonalds Menu.
restaurant_price = []  # List of the prices of said items.
restaurant_calorie = []  # List of the calories of said items.
restaurant_ratio = []  # List of price-to-calorie ratios of said items.

# Below are the lines of code that are responsible for the import of csv data into data points Python can work with.


def restaurant_picker():
    """"This is the function that is responsible for jump starting the program. """
    print("Welcome to MaxCalester - a dynamic programming program that solves your fast-food restaurants dilemma!")
    print("Given a budget, the program yields a list of items that will have the highest calorie count.")
    print("Our rationale is, the most calorie you get, more value you get for your $$$!")
    print("You get to choose the restaurant or we can pick for you! Or, we can give you a combo of all restaurants!")
    print("The restaurants in our database are: Subway, Chipotle, Domino's, McDonalds, and Taco Bell. Let's go!")
    print("----------------------------------------------------------------------------")
    budget = (input("What is your budget?  "))

    # Catches invalid user inputs
    try:
        budget = float(budget)
    except ValueError:
        print("You entered something that is not a number! Try again. ")
        print("-----------------------------------------------------------------------------")
        restaurant_picker()

    pick = str(input("Please pick a restaurant from one of the following: subway, tacobell, chipotle, mcdonalds, and chipotle."
                     " Please remember that your input must be in all lowercase and no spaces. "))

    choices = ["subway", "tacobell", "mcdonalds", "chipotle", "dominos"]

    if pick not in choices:
        print("You typed an invalid command! Try again.")
        run_again()
        # spelling and case really matter. No capitalization. No spaces.

    if pick == "subway":
        with open('final_subway.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                restaurant_name.append(row[0])
                restaurant_price.append(float(row[1]))
                restaurant_calorie.append(float(row[2]))

        # Now, we then make a dictionary and list that will be useful later on

        calorie_price_seq = list(zip(restaurant_calorie, restaurant_price))
        calorie_name_dict = dict(zip(restaurant_calorie, restaurant_name))

        stomach(calorie_price_seq, budget, calorie_name_dict)

    if pick == "tacobell":
        with open('final_tacobell.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                restaurant_name.append(row[0])
                restaurant_price.append(float(row[1]))
                restaurant_calorie.append(float(row[2]))

        # Now, we then make a dictionary and list that will be useful later on

        calorie_price_seq = list(zip(restaurant_calorie, restaurant_price))
        calorie_name_dict = dict(zip(restaurant_calorie, restaurant_name))

        stomach(calorie_price_seq, budget, calorie_name_dict)

    if pick == "chipotle":
        with open('final_chipotle.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                restaurant_name.append(row[0])
                restaurant_price.append(float(row[1]))
                restaurant_calorie.append(float(row[2]))

        # Now, we then make a dictionary and list that will be useful later on

        calorie_price_seq = list(zip(restaurant_calorie, restaurant_price))
        calorie_name_dict = dict(zip(restaurant_calorie, restaurant_name))

        stomach(calorie_price_seq, budget, calorie_name_dict)

    if pick == "mcdonalds":
        with open('final_mcdonalds.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                restaurant_name.append(row[0])
                restaurant_price.append(float(row[1]))
                restaurant_calorie.append(float(row[2]))

        # Now, we then make a dictionary and list that will be useful later on

        calorie_price_seq = list(zip(restaurant_calorie, restaurant_price))
        calorie_name_dict = dict(zip(restaurant_calorie, restaurant_name))

        stomach(calorie_price_seq, budget, calorie_name_dict)

    if pick == "dominos":
        with open('final_dominos.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                restaurant_name.append(row[0])
                restaurant_price.append(float(row[1]))
                restaurant_calorie.append(float(row[2]))

        # Now, we then make a dictionary and list that will be useful later on

        calorie_price_seq = list(zip(restaurant_calorie, restaurant_price))
        calorie_name_dict = dict(zip(restaurant_calorie, restaurant_name))

        stomach(calorie_price_seq, budget, calorie_name_dict)


def run_again():
    """ This function asks the user if they want to run the program again. """
    print("-------------------------------------------------------------------------")
    more_choices = input(str("Would like to run the program again? Type YES or NO. "))
    if more_choices == "YES":
        restaurant_picker()
    elif more_choices == "NO":
        print("Thank you for using our program. Bye!")
        return
    else:
        print("Invalid command!")
        run_again()


def stomach(items, budget, calorie_dictionary):
    """
    Solves the stomach problem by finding the combination of food items with the highest calorie count
    subsequence of food `items` subject that cost no more than `budget`.

    `items` is a sequence of pairs `(calorie, price)`, where `calorie` is
    a number and `budget` is a non-negative integer.

    Returns a pair whose first element is the sum of calories in the most
    "nutritious" subsequence of food items, and whose second element is the subsequence.

    """

    # Return the calorie of the most "nutritious" subsequence of the first i
    # elements in items whose prices sum to no more than j.

    start_time = time.time()  # Starts the time to measure how fast the algorithm is.

    @lru_cache(maxsize=None)
    def best_value(i, j):
        if i == 0: return 0
        calorie, price = items[i - 1]
        if price > j:
            return best_value(i - 1, j)
        else:
            return max(best_value(i - 1, j),
                       best_value(i - 1, j - price) + calorie)

    j = budget
    result = []
    for i in range(len(items), 0, -1):
        if best_value(i, j) != best_value(i - 1, j):
            result.append(items[i - 1])
            j -= items[i - 1][1]
    result.reverse()

    total_calorie = 0
    total_price = 0

    print("-----------------------------------------------------------------------------")
    print("You should get the following items to achieve the maximum calorie count at your budget of $" + str(budget) + ":")
    print("-----------------------------------------------------------------------------")
    for i in range(len(result)):
        calorie = int(result[i][0])
        price = float(result[i][1])
        total_calorie += calorie
        total_price += price
        print(str(calorie_dictionary.get(calorie)) + " with a calorie of " + str(calorie) + " and price of " +
              str(price) + " dollars")

    print("-----------------------------------------------------------------------------")
    print("Your total calorie count is " + str(total_calorie) + " calories and total price is $" + str(total_price))
    print("It took %s seconds to deliver you this recommendation." % (time.time() - start_time))
    print("Thank you for using our program and have a nice meal!")
    run_again()

restaurant_picker()  # This starts the entire program.
