# Shopping Cart System

# Dictionary containing 25 grocery products and their prices
products = {
    "Apple": 100,
    "Milk": 60,
    "Bread": 40,
    "Chocolate": 50,
    "Chips": 30,
    "Rice": 80,
    "Sugar": 45,
    "Salt": 20,
    "Flour": 50,
    "Eggs": 70,
    "Butter": 55,
    "Cheese": 90,
    "Banana": 40,
    "Orange": 60,
    "Potato": 30,
    "Tomato": 35,
    "Onion": 40,
    "Cooking Oil": 150,
    "Biscuits": 25,
    "Juice": 60,
    "Tea": 120,
    "Coffee": 180,
    "Yogurt": 35,
    "Carrot": 40,
    "Cucumber": 30
}

# List to store items in the cart
cart = []

# Tuple containing payment methods
payment_methods = ("Cash", "UPI", "Card")


# Function using *args, **kwargs, and a default argument
def show_bill(*items, discount=0, **details):

    total = 0

    print("\n========== YOUR BILL ==========")

    # Calculate the price of each item
    for item, quantity in items:

        price = products[item] * quantity

        total += price

        print(item, "x", quantity, "=", price)

    # Apply discount to the total
    total = total - (total * discount / 100)

    print("-------------------------------")
    print("Discount:", discount, "%")
    print("Total Amount: Rs.", round(total, 2))
    print("Customer Details:", details)


# Display available groceries
print("========== GROCERY SHOP ==========")

print("\nAvailable Groceries:")

for item, price in products.items():

    print(item, "- Rs.", price)


# Take user input and handle errors
try:

    number = int(input("\nHow many different products do you want to buy? "))

    if number <= 0:
        raise ValueError

    # Ask the user to enter products
    for i in range(number):

        item = input("\nEnter grocery name: ").title()

        if item not in products:
            print("Product not available!")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity!")
            continue

        # Add the product and quantity to the cart
        cart.append((item, quantity))

    # Display the shopping cart
    print("\nYour Cart:", cart)

    # Display payment methods
    print("\nPayment Methods:", payment_methods)

    payment = input("Choose payment method: ").title()

    if payment not in payment_methods:
        payment = "Cash"
        print("Invalid payment method. Cash selected.")

    # Generate the final bill
    if cart:

        show_bill(
            *cart,
            discount=10,
            customer="Guest",
            payment_method=payment
        )

    else:

        print("\nYour cart is empty.")

except ValueError:

    print("\nInvalid input! Please enter a valid number.")

# End of the program
print("\nThank you for shopping!")