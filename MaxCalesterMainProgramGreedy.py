#   MaxCalester - Main Program
#   Developed By: Andy Han
#   Data Provided By: Ibrahima Dieye and Lang Li
#   April 26th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis

# Importing other Python files and time library

import time

from MaxCalesterAllRestaurantsGreedy import*
from MaxCalesterChipotleGreedy import*
from MaxCalesterDominosGreedy import*
from MaxCalesterMcDonaldsGreedy import*
from MaxCalesterSubwayGreedy import*
from MaxCalesterTacoBellGreedy import*


def restaurant_picker():
    """"This is the function that is responsible for jump starting the program. """
    print("Welcome to MaxCalester - a greedy algorithm program that solves your fast-food restaurants dilemma!")
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
        run_again()

    sorted_price = sorted(all_restaurants_price)  # Sorted list in ascending order of all the prices of items.

    if float(budget) < sorted_price[0]:
        print("You cannot purchase anything from our menu with your budget. Please bring more money!")
        return

    user_input = str(input("Would you like to have a recommendation based on all of the items in our database"
                           " or just items from a single restaurant? "
                           "Type YES for a cross-selection and NO for a single-selection. "))
    print("----------------------------------------------------------------------------")

    if user_input == "YES":  # If the user wants a cross-selection of items.
        start_time = time.time()

        all_restaurants_main_driver(budget)  # Calls the main driver of the Python file for this option
        all_restaurant_max_cal = all_restaurants_best_combo_price_calorie[budget][1]  # The total calorie count
        all_restaurant_max_price = all_restaurants_best_combo_price_calorie[budget][0]  # The total price

        print("At your budget of $" + str(budget) +
              ", to get the most bang for your buck in terms of highest net calorie count, ")
        print("You should purchase the following items across all five restaurants to obtain a total caloric count of ")
        print(str(all_restaurant_max_cal) + " calories" + " for the price of $" + str(all_restaurant_max_price))
        print("----------------------------------------------------------------------------")
        print(*all_restaurants_item_list, sep="\n")  # Prints all of the items in the recommendation
        print("Thank you for using our program and happy eating!")
        print("----------------------------------------------------------------------------")
        print("It took %s seconds to calculate this recommendation." % (time.time() - start_time))

        run_again()

    elif user_input == "NO":  # If the user does not want a cross-selection of restaurants.

        print("You chose NO. Would you like to choose the single restaurant you would like a recommendation from or"
              "the restaurant with the best recommendation in terms of calorie count?")

        restaurant_choice = input(str("Please type BEST for the best option or the name of the restaurant "

                                      "you would like to choose from. Please, all lower case and no spaces. "))

        choices = ["BEST", "subway", "tacobell", "mcdonalds", "chipotle", "dominos"]

        if restaurant_choice not in choices:
            print("You typed an invalid command! Try again.")
            run_again()
            # spelling and case really matter. No capitalization. No spaces.
        else:
            start_time = time.time()  # We don't want to count the time the user spends typing.

            # What's happening below is that we test the budget for every restaurant and
            # See which restaurant has the best combo that would yield the highest calorie count

            subway_main_driver(budget)
            tacobell_main_driver(budget)
            mcdonalds_main_driver(budget)
            chipotle_main_driver(budget)
            dominos_main_driver(budget)

            # Below are the variables that will hold the numbers for total calorie and price
            # for each each respective restaurants. Good use of double arrays.
            # Most of the heavy lifting is done by the other files, we even carry over the variables.
            # Do note again that adding new restaurants means making new files for them.

            subway_max_cal = subway_best_combo_price_calorie[budget][1]
            tacobell_max_cal = tacobell_best_combo_price_calorie[budget][1]
            mcdonalds_max_cal = mcdonalds_best_combo_price_calorie[budget][1]
            chipotle_max_cal = chipotle_best_combo_price_calorie[budget][1]
            dominos_max_cal = dominos_best_combo_price_calorie[budget][1]

            subway_max_price = subway_best_combo_price_calorie[budget][0]
            tacobell_max_price = tacobell_best_combo_price_calorie[budget][0]
            mcdonalds_max_price = mcdonalds_best_combo_price_calorie[budget][0]
            chipotle_max_price = chipotle_best_combo_price_calorie[budget][0]
            dominos_max_price = dominos_best_combo_price_calorie[budget][0]

            restaurant_dictionary = {}
            restaurant_dictionary.update({subway_max_cal: "subway", mcdonalds_max_cal: "mcdonalds",
                                          tacobell_max_cal: "tacobell", chipotle_max_cal: "chipotle",
                                          dominos_max_cal: "dominos"})

            max_cal = max(subway_max_cal, tacobell_max_cal, mcdonalds_max_cal, chipotle_max_cal, dominos_max_cal)

            # Obviously, the max_cal will be equal to one of the five restaurants' numbers or
            # the user will specifically ask for Subway out of the five restaurants.
            # We cannot emphasize how case sensitive the program is.
            # The conditionals below reflect what the program will say if our winner is a certain restaurant.

            if  restaurant_choice == "subway" or restaurant_dictionary.get(max_cal) == "subway":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Subway and purchase the following items to obtain a total caloric count of ")
                print(str(subway_max_cal) + " calories" + " for the price of $" + str(subway_max_price))
                print("----------------------------------------------------------------------------")
                print(*subway_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_choice == "mcdonalds" or restaurant_dictionary.get(max_cal) == "mcdonalds":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print(
                    "You should go to McDonalds and purchase the following items to obtain a total caloric count of ")
                print(str(mcdonalds_max_cal) + " calories" + " for the price of $" + str(mcdonalds_max_price))
                print("----------------------------------------------------------------------------")
                print(*mcdonalds_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_choice == "chipotle" or restaurant_dictionary.get(max_cal) == "chipotle":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Chipotle and purchase the following items to obtain a total caloric count of ")
                print(str(chipotle_max_cal) + " calories" + " for the price of $" + str(chipotle_max_price))
                print("----------------------------------------------------------------------------")
                print(*chipotle_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_choice == "dominos" or restaurant_dictionary.get(max_cal) == "dominos":
                print("At your budget of $" + str(
                    budget) + ", to get the highest net calorie count, ")
                print("You should go to Domino's and purchase the following items to obtain a total caloric count of ")
                print(str(dominos_max_cal) + " calories" + " for the price of $" + str(dominos_max_price))
                print("----------------------------------------------------------------------------")
                print(*dominos_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_choice == "tacobell" or restaurant_dictionary.get(max_cal) == "tacobell":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Taco Bell and purchase the following items to obtain a total caloric count of ")
                print(str(tacobell_max_cal) + " calories" + " for the price of $" + str(tacobell_max_price))
                print("----------------------------------------------------------------------------")
                print(*tacobell_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            print("----------------------------------------------------------------------------")
            print("It took %s seconds to calculate this recommendation." % (time.time() - start_time))

    else:
        print("You typed an invalid command!")
        run_again()


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


restaurant_picker()  # This starts the entire program.

