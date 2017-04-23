import csv
from functools import lru_cache
import time


# Below, we create the various lists of name, prices, calories, and ratios the program will add to as data is imported.

mcdonalds_name = []  # List of the names that are on the McDonalds Menu.
mcdonalds_price = []  # List of the prices of said items.
mcdonalds_calorie = []  # List of the calories of said items.
mcdonalds_ratio = []  # List of price-to-calorie ratios of said items.

# Below are the lines of code that are responsible for the import of csv data into data points Python can work with.
with open('final_mcdonalds.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        mcdonalds_name.append(row[0])
        mcdonalds_price.append(float(row[1]))
        mcdonalds_calorie.append(float(row[2]))
        mcdonalds_ratio.append(float(row[3]))

# Now, we then make dictionaries that match the various variables to each other in order to identify things later on.


calorie_price_seq = list(zip(mcdonalds_calorie, mcdonalds_price))
calorie_name_dict = dict(zip(mcdonalds_calorie, mcdonalds_name))
name_price_dict = dict(zip(mcdonalds_name, mcdonalds_price))


def stomach(items, budget):
    """
    Solve the stomach problem by finding the combination of food items with the highest calorie count
    subsequence of food `items` subject that cost no more than
    `budget`.

    `items` is a sequence of pairs `(calorie, price)`, where `calorie` is
    a number and `budget` is a non-negative integer.

    `budget` is a non-negative integer.

    Return a pair whose first element is the sum of calories in the most
    "nutritious" subsequence of food items, and whose second element is the subsequence.

    """

    # Return the calorie of the most "nutritious" subsequence of the first i
    # elements in items whose prices sum to no more than j.
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
    # print(best_value(len(items), budget), result)

    total_calorie = 0
    total_price = 0
    print("You should get the following items to achieve maximum calorie at your budget:")
    for i in range(len(result)):
        calorie = int(result[i][0])
        price = float(result[i][1])
        total_calorie += calorie
        total_price += price
        print(str(calorie_name_dict.get(calorie)) + " with a calorie of " + str(calorie) + " and price of " +
              str(price) + " dollars")
    print("Your total calorie count is " + str(total_calorie) + " and total price is $" + str(total_price))

start_time = time.time()
stomach(calorie_price_seq, 5)
print("It took %s seconds to get the optimal." % (time.time() - start_time))

## Takes 36 seconds if I print the item prices and calories
## If I only print the total number of calories, it takes 3 seconds:
## Andy's McDonald's only program is super fast! Wut??
## Result different from Andy's solution.
