stock = {"banana":6, "apple":0, "orange":32, "pear":15}

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear":3}

total_prices = {}
for fruit_1 in stock:
    for fruit_2 in prices:
        if fruit_1==fruit_2:
            print("The total sum for {} is equal to {}".format(fruit_1, stock[fruit_1]*prices[fruit_1]))
            total_prices.update({fruit_1:stock[fruit_1]*prices[fruit_1]})

print(total_prices)
