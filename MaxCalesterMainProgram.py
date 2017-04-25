#   MaxCalester Main Program
#   Developed By: Andy Han
#   Data Provided By: Ibou Dieye and Lang Li
#   March 29th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis

import time
from MaxCalesterProgramAllRestaurants import*
from MaxCalesterProgramChipotle import*
from MaxCalesterProgramDominos import*
from MaxCalesterProgramMcDonalds import*
from MaxCalesterProgramSubway import*
from MaxCalesterProgramTacoBell import*


def restaurant_picker():
    """"This is the function that is responsible for jump starting the program. """
    print("Welcome to MaxCalester - a program designed to give you a selection of items to buy at fast food restaurants")
    print("Given a budget, we make our choice by giving you a list of items that would yield the highest calorie count.")
    print("The restaurants in our database are: Subway, Chipotle, Domino's, McDonalds, and Taco Bell. Let's go!")
    print("----------------------------------------------------------------------------")
    budget = int(input("What is your budget? "))
    user_input = str(input("Would you like to have a recommendation based on all of the items in our database"
                           " or just items from a single restaurant? "
                           "Type YES for a cross-selection and NO for a single-selection. "))
    print("----------------------------------------------------------------------------")

    if user_input == "YES":
        start_time = time.time()
        all_restaurants_main_driver(budget)
        all_restaurant_max_cal = all_restaurants_best_combo_price_calorie[budget][1]
        all_restaurant_max_price = all_restaurants_best_combo_price_calorie[budget][0]

        print("At your budget of $" + str(budget) +
              ", to get the most bang for your buck in terms of highest net calorie count, ")
        print("You should purchase the following items across all five restaurants to obtain a total caloric count of ")
        print(str(all_restaurant_max_cal) + " calories" + " for the price of $" + str(all_restaurant_max_price))
        print("----------------------------------------------------------------------------")
        print(*all_restaurants_item_list, sep="\n")
        print("Thank you for using our program and happy eating!")
        print("----------------------------------------------------------------------------")
        print("It took %s seconds to get the optimal." % (time.time() - start_time))

    elif user_input == "NO":
        print("You chose NO. Would you like to choose the single restaurant you would like a recommendation from or"
              "the restaurant with the best recommendation in terms of calorie count?")
        restaurant_choice = input(str("Please type BEST for the best pick or the name of the restaurant "
                                      "you would like to choose from. Please, all lower case and no spaces. "))
        if restaurant_choice == "BEST" or "subway" or "tacobell" or "mcdonalds" or "chipotle" or "dominos":
            start_time = time.time()
            subway_main_driver(budget)
            tacobell_main_driver(budget)
            mcdonalds_main_driver(budget)
            chipotle_main_driver(budget)
            dominos_main_driver(budget)

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

            if restaurant_dictionary.get(max_cal) == "subway" or restaurant_choice == "subway":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Subway and purchase the following items to obtain a total caloric count of ")
                print(str(subway_max_cal) + " calories" + " for the price of $" + str(subway_max_price))
                print("----------------------------------------------------------------------------")
                print(*subway_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_dictionary.get(max_cal) == "mcdonalds" or restaurant_choice == "mcdonalds":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print(
                    "You should go to McDonalds and purchase the following items to obtain a total caloric count of ")
                print(str(mcdonalds_max_cal) + " calories" + " for the price of $" + str(mcdonalds_max_price))
                print("----------------------------------------------------------------------------")
                print(*mcdonalds_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_dictionary.get(max_cal) == "chipotle" or restaurant_choice == "chipotle":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Chipotle and purchase the following items to obtain a total caloric count of ")
                print(str(chipotle_max_cal) + " calories" + " for the price of $" + str(chipotle_max_price))
                print("----------------------------------------------------------------------------")
                print(*chipotle_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_dictionary.get(max_cal) == "dominos" or restaurant_choice == "dominos":
                print("At your budget of $" + str(
                    budget) + ", to get the highest net calorie count, ")
                print("You should go to Domino's and purchase the following items to obtain a total caloric count of ")
                print(str(dominos_max_cal) + " calories" + " for the price of $" + str(dominos_max_price))
                print("----------------------------------------------------------------------------")
                print(*dominos_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            elif restaurant_dictionary.get(max_cal) == "tacobell" or restaurant_choice == "tacobell":
                print("At your budget of $" + str(budget) + ", to get the highest net calorie count, ")
                print("You should go to Taco Bell and purchase the following items to obtain a total caloric count of ")
                print(str(tacobell_max_cal) + " calories" + " for the price of $" + str(tacobell_max_price))
                print("----------------------------------------------------------------------------")
                print(*tacobell_item_list, sep="\n")
                print("Thank you for using our program and happy eating!")

            print("----------------------------------------------------------------------------")
            print("It took %s seconds to get the optimal." % (time.time() - start_time))

        else:
            print("You typed an invalid command. Try again!")
            restaurant_picker()

restaurant_picker()

