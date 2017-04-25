#   MaxCalester Program All Restaurants
#   Developed By: Andy Han
#   Data Provided By: Ibrahima Dieye and Lang Li
#   March 29th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis

# This file has the most extensive comments out of all of the Python files for each restaurant. Use this as a reference.

import csv

all_restaurants_best_combo = {}
all_restaurants_best_combo_price_calorie = {}  # This dictionary will have different price point as its keys
# and the list of the best combination items for the price point as its values.

# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.

all_restaurants_name = []  # List of the names that are on the all_restaurants Menu.
all_restaurants_price = []  # List of the prices of said items.
all_restaurants_calorie = []  # List of the calories of said items.
all_restaurants_ratio = []  # List of price-to-calorie ratios of said items.

# Below are the lines of code that are responsible for the import of csv data into data points Python can work with.
# A great thing about our data set is that they are already well-organized and sorted by the calorie-price ratio.
# However, we do have sorting in place in case the data isn't perfect as in a real life, data will always be added.

with open('final_all_items.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        all_restaurants_name.append(row[0])
        all_restaurants_price.append(float(row[1]))
        all_restaurants_calorie.append(float(row[2]))
        all_restaurants_ratio.append(float(row[3]))

# Now, we then make dictionaries that match the various variables to each other in order to identify things later on.

ratio_price_dict = dict(zip(all_restaurants_ratio, all_restaurants_price))
ratio_name_dict = dict(zip(all_restaurants_ratio, all_restaurants_name))

name_calorie_dict = dict(zip(all_restaurants_name, all_restaurants_calorie))
name_price_dict = dict(zip(all_restaurants_name, all_restaurants_price))

calorie_price_dict = dict(zip(all_restaurants_calorie, all_restaurants_price))
calorie_name_dict = dict(zip(all_restaurants_calorie, all_restaurants_name))

# We make sorted lists of the ratio, calorie, and price to ensure the smoothness of the program.

sorted_ratio_list = sorted(all_restaurants_ratio, reverse=True)
sorted_calorie_list = sorted(all_restaurants_calorie, reverse=True)
sorted_price_list = sorted(all_restaurants_price, reverse=True)

all_restaurants_item_list = []  # The list of items you should buy to maximize caloric count.


def all_restaurants_main_driver(budget):
    if all_restaurants_best_combo.get(budget):  # Checks to see if a value already exists in the dictionary. Saves time.
        return print("For the budget of $" + str(budget) +
                     ", here is the list of items you should buy to maximize how much calorie you are getting: "
                     + str(all_restaurants_best_combo.get(budget)))
    else:
        greedy_algorithm(budget)


def greedy_algorithm(budget):
    length = len(sorted_ratio_list)  # The length of the ratio_list to determine the number of comparisons to make
    total_calorie_count = 0  # A running tally of the calorie count based on the items purchased
    total_price = 0  # A running tally of how much you spent so far

    if budget < sorted_price_list[length - 1]:  # If budget is less than the price of the cheapest item of the list...
        print("Your budget is not big enough to buy anything from the all_restaurants menu we have. Tough luck!")
        return

    if calorie_price_dict.get(sorted_calorie_list[0]) <= budget <= ratio_price_dict.get(sorted_ratio_list[1]) * 2:

        all_restaurants_item_list.append("1 " + calorie_name_dict.get(sorted_calorie_list[0]) + " for the price of $"
                                         + str(calorie_price_dict.get(sorted_calorie_list[0])) +
                                         " with a calorie count of " + str(sorted_calorie_list[0]))

        # Add the results to our "database" dictionary
        all_restaurants_best_combo.update({budget: all_restaurants_item_list})
        all_restaurants_best_combo_price_calorie[budget] = [total_price, total_calorie_count]

        return

    for i in range(length):
        current_ratio = sorted_ratio_list[i]
        item_name = ratio_name_dict.get(current_ratio)
        item_price = ratio_price_dict.get(current_ratio)

        # If what you already spent plus the price of the item you want to purchase is less than the budget.
        if total_price + item_price <= budget:
            total_price = total_price + item_price  # Add the desired item's price on to the total price tally
            total_calorie_count = total_calorie_count + name_calorie_dict.get(item_name)
            # Add the desired item's caloric count to the total caloric tally
            all_restaurants_item_list.append("1 " + item_name + " for the price of $" + str(item_price) +
                                             " with a calorie count of " + str(
                name_calorie_dict.get(item_name)))  # Add the item to the final list

    # We are adding the list of items that is best at the price point to the dict so that future searches are O(1)
    all_restaurants_best_combo[budget] = all_restaurants_item_list
    all_restaurants_best_combo_price_calorie[budget] = [total_price, total_calorie_count]




