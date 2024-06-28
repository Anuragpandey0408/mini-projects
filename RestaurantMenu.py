menu = {
    'Pizza': 99,
    'Burger': 49,
    'White Sauce Pasta': 70,
    'Coffee': 60,
    'Normal Thali': 50,
    'Delux Thali': 100,
    'Special Thali': 149,
}

# Greet
print("Welcome to PYTHON Restaurant")
print(" Pizza : 99Rs\n Burger : 49Rs\n White Sauce Pasta : 70Rs\n Coffee : 60Rs\n Normal Thali : 50Rs\n Delux Thali : 100Rs\n Special Thali : 149Rs")

order_total = 0

# First Item
item_1 = input("Enter the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available!")

# Another Item
another_item = input("Do you want to add another item? (Yes/No): ")
if another_item.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available!")
else:
    print("No additional items added.")

# Total Amount
print(f"The total amount to pay is {order_total} Rs.")


    