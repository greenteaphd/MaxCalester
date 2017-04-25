#   MaxCalester Program Tacobell
#   Developed By: Andy Han
#   Data Provided By: Ibou Dieye and Lang Li
#   March 29th, 2017
#   Macalester College
#   COMP 221 - Algorithm Design and Analysis


import csv

tacobell_best_combo = {}
tacobell_best_combo_price_calorie = {}  # This dictionary will have different price point as its keys and the list of
# the best combination items for the price point as its values.

# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.

tacobell_name = []  # List of the names that are on the tacobell Menu.
tacobell_price = []  # List of the prices of said items.
tacobell_calorie = []  # List of the calories of said items.
tacobell_ratio = []  # List of price-to-calorie ratios of said items.

# Below are the lines of code that are responsible for the import of csv data into data points Python can work with.
with open('final_tacobell.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        tacobell_name.append(row[0])
        tacobell_price.append(float(row[1]))
        tacobell_calorie.append(int(row[2]))
        tacobell_ratio.append(float(row[3]))

# Now, we then make dictionaries that match the various variables to each other in order to identify things later on.

ratio_price_dict = dict(zip(tacobell_ratio, tacobell_price))
ratio_name_dict = dict(zip(tacobell_ratio, tacobell_name))

name_calorie_dict = dict(zip(tacobell_name, tacobell_calorie))
name_price_dict = dict(zip(tacobell_name, tacobell_price))

calorie_price_dict = dict(zip(tacobell_calorie, tacobell_price))
calorie_name_dict = dict(zip(tacobell_calorie, tacobell_name))

# We make sorted lists of the ratio, calorie, and price to ensure the smoothness of the program.

sorted_ratio_list = sorted(tacobell_ratio, reverse=True)
sorted_calorie_list = sorted(tacobell_calorie, reverse=True)
sorted_price_list = sorted(tacobell_price, reverse=True)


tacobell_item_list = []  # The list of items you should buy to maximize caloric count.


def tacobell_main_driver(budget):
    if tacobell_best_combo.get(budget):
        return print("For the budget of $" + str(budget) +
                     ", here is the list of items you should buy to maximize how much calorie you are getting: "
                     + str(tacobell_best_combo.get(budget)))
    else:
        greedy_algorithm(budget)


def greedy_algorithm(budget):
    length = len(sorted_ratio_list)  # The length of the ratio_list to determine the number of comparisons to make
    total_calorie_count = 0  # A running tally of the calorie count based on the items purchased
    total_price = 0  # A running tally of how much you spent so far

    if budget < sorted_price_list[length - 1]:  # If budget is less than the price of the cheapest item of the list...
        print("Your budget is not big enough to buy anything from the tacobell menu we have. Tough luck!")
        return

    for i in range(length):
        current_ratio = sorted_ratio_list[i]
        item_name = ratio_name_dict.get(current_ratio)
        item_price = ratio_price_dict.get(current_ratio)

        if total_price + item_price <= budget:  # If what you spent already plus the price of the item you want to purchase is less than the budget...
            total_price = total_price + item_price  # Add the desired item's price on to the total price tally
            total_calorie_count = total_calorie_count + name_calorie_dict.get(
                item_name)  # Add the desired item's caloric count to the total caloric tally
            tacobell_item_list.append("1 " + item_name + " for the price of $" + str(item_price) +
                             " with a calorie count of " + str(
                name_calorie_dict.get(item_name)))  # Add the item to the final list

    tacobell_best_combo[budget] = tacobell_item_list  # Add the list of items that is best at the price point to dictionary so that future searches are O(1)
    tacobell_best_combo_price_calorie[budget] = [total_price, total_calorie_count]



