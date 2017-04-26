#   MaxCalester Program Chipotle
#   Developed By: Andy Han
#   Data Provided By: Ibrahima Dieye and Lang Li
#   March 29th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis

import csv

chipotle_best_combo = {}
chipotle_best_combo_price_calorie = {}

# The above dictionary will have different price point as its keys
# and the list of the best combination items for the price point as its values.

# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.

chipotle_name = []  # List of the names that are on the chipotle Menu.
chipotle_price = []  # List of the prices of said items.
chipotle_calorie = []  # List of the calories of said items.
chipotle_ratio = []  # List of price-to-calorie ratios of said items.

# Below are the lines of code that are responsible for the import of csv data into data points Python can work with.
# A great thing about our data set is that they are already well-organized and sorted by the calorie-price ratio.
# However, we do have sorting in place in case the data isn't perfect as in a real life, data will always be added.

with open('final_chipotle.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        chipotle_name.append(row[0])
        chipotle_price.append(float(row[1]))
        chipotle_calorie.append(float(row[2]))
        chipotle_ratio.append(float(row[3]))

# Now, we then make dictionaries that match the various variables to each other in order to identify things later on.

ratio_price_dict = dict(zip(chipotle_ratio, chipotle_price))
ratio_name_dict = dict(zip(chipotle_ratio, chipotle_name))

name_calorie_dict = dict(zip(chipotle_name, chipotle_calorie))
name_price_dict = dict(zip(chipotle_name, chipotle_price))

calorie_price_dict = dict(zip(chipotle_calorie, chipotle_price))
calorie_name_dict = dict(zip(chipotle_calorie, chipotle_name))

# We make sorted lists of the ratio, calorie, and price to ensure the smoothness of the program.

sorted_ratio_list = sorted(chipotle_ratio, reverse=True)
sorted_price_list = sorted(chipotle_price, reverse=True)

chipotle_item_list = []  # The list of items you should buy to maximize caloric count.


def chipotle_main_driver(budget):
    """ This is what starts this program. It first checks if the budget has been previously searched before."""
    if chipotle_best_combo.get(budget):  # Checks to see if a value already exists in the dictionary. Saves time.
        return print("For the budget of $" + str(budget) +
                     ", here is the list of items you should buy to maximize how much calorie you are getting: "
                     + str(chipotle_best_combo.get(budget)))
    else:
        greedy_algorithm(budget)


def greedy_algorithm(budget):
    """ This function formulates a list of items that would make the best combo by using the greedy property."""
    length = len(sorted_ratio_list)  # The length of the ratio_list to determine the number of comparisons to make
    total_calorie_count = 0  # A running tally of the calorie count based on the items purchased
    total_price = 0  # A running tally of how much you spent so far

    if budget < sorted_price_list[length - 1]:  # If budget is less than the price of the cheapest item of the list...
        print("Your budget is not big enough to buy anything from the chipotle menu we have. Tough luck!")
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
            chipotle_item_list.append("1 " + item_name + " for the price of $" + str(item_price)
                                      + " with a calorie count of " + str(name_calorie_dict.get(item_name)) + " from Chipotle.")
            # Add the item to the final list

    # We are adding the list of items that is best at the price point to the dict so that future searches are O(1)
    chipotle_best_combo[budget] = chipotle_item_list
    chipotle_best_combo_price_calorie[budget] = [total_price, total_calorie_count]






