#   MaxCalester Program - McDonald's
#   Developed By: Andy Han
#   Data Provided By: Ibrahima Dieye and Lang Li
#   April 26th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis
#   Questions? Contact us at dhan@macalester.edu

import csv

mcdonalds_best_combo = {}
mcdonalds_best_combo_price_calorie = {}

# The above dictionaries will have different price point as its keys
# and the list of the best combination items and calorie for the price point as its values.

# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.

mcdonalds_name = []  # List of the names of all of the items in our combined database of restaurant items.
mcdonalds_price = []  # List of the prices of said items.
mcdonalds_calorie = []  # List of the calories of said items.
mcdonalds_ratio = []  # List of price-to-calorie ratios of said items.

mcdonalds_item_list = []  # The list of items you should buy to maximize caloric count. Items will be added soon.

# Below are the lines of code that are responsible for the importing of csv data into data points Python can work with.
# The program goes through a lot of sorting to ensure the greedy property can be implemented.
# The data lists are sorted by the price-calorie ratio calculated in the program.

# The csv file is a list of items. Each row has a item name, item's price, and item's calorie.
# Items are added to three different lists based on the csv import.


# CSV File Import
with open('final_mcdonalds.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        mcdonalds_name.append(row[0])
        mcdonalds_price.append(float(row[1]))
        mcdonalds_calorie.append(float(row[2]))

# Below, the calorie to price ratio is created and each ratio is added to the list created earlier.
for i in range(len(mcdonalds_name)): # a ratio for every item
    ratio = mcdonalds_calorie[i] / mcdonalds_price[i]
    mcdonalds_ratio.append(ratio)

# We make sorted lists of the ratio, price, and calorie to ensure the smoothness of the program.
sorted_ratio_list = sorted(mcdonalds_ratio, reverse=True)

sorted_price_list = mcdonalds_price
sorted_calorie_list = mcdonalds_calorie
sorted_name_list = mcdonalds_name

# We can use the newly sorted ratio list to sort the other lists. Nifty feature in Python.
sorted_ratio_list, sorted_price_list, sorted_calorie_list, sorted_name_list = map(list, zip(*sorted(zip(mcdonalds_ratio, sorted_price_list, sorted_calorie_list, sorted_name_list), reverse=True)))

# Now, we then make dictionaries that match the various variables to each other in order to identify things later on.
ratio_price_dict = dict(zip(sorted_ratio_list, sorted_price_list))
ratio_name_dict = dict(zip(sorted_ratio_list, sorted_name_list))
name_calorie_dict = dict(zip(sorted_name_list, sorted_calorie_list))


def mcdonalds_main_driver(budget):
    """ This is what starts this program."""
    greedy_algorithm(budget)


def greedy_algorithm(budget):
    """ This function creates a list of items that would make the best combo by using the greedy property."""
    sorted_price = sorted(mcdonalds_price)

    if budget < sorted_price[0]:  # Base Case: If the budget is less than the price of the cheapest item of the list.
        print("Your budget is not big enough to buy anything from the database. Tough luck!")
        return

    length = len(sorted_ratio_list)  # The length of the ratio_list to determine the number of comparisons to make
    total_calorie_count = 0  # A running tally of the calorie count based on the items "purchased"
    total_price = 0  # A running tally of how much "spent" so far based on the items added

    for i in range(length):
        current_ratio = sorted_ratio_list[i]
        item_name = ratio_name_dict.get(current_ratio)  # This is why we created the dictionaries earlier.
        item_price = ratio_price_dict.get(current_ratio)

        # If what you already spent plus the price of the item you want to purchase is less than the budget...
        if total_price + item_price <= budget:
            total_price = total_price + item_price  # Add the desired item's price on to the total price tally
            total_calorie_count = total_calorie_count + name_calorie_dict.get(item_name)
            # Above, add the desired item's caloric count to the total caloric tally
            mcdonalds_item_list.append("1 " + item_name + " for the price of $" + str(item_price) +
                                       " with a calorie count of " + str(
                name_calorie_dict.get(item_name)))  # Add the item to the final list. We initialized this list earlier.
        else:
            break

    # We are adding the list of items that is best at the price point to the dict so that future searches are O(1)
    # In addition, the Main Program imports these variables below when coming up with the recommendation.

    mcdonalds_best_combo[budget] = mcdonalds_item_list
    mcdonalds_best_combo_price_calorie[budget] = [total_price, total_calorie_count]

# --------------------------------------------------- END OF PROGRAM ---------------------------------------------------







