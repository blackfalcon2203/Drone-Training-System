import random

# List of 6 items
items = [1, 2, 3, 4, 5, 6]

# Custom shuffle function (like random.shuffle)
def custom_shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

# Shuffle the list using the custom function
custom_shuffle(items)

# Simulate 6 tries where each item is chosen exactly once
for i in range(6):
    chosen_item = items[i]
    print(f"{chosen_item}")