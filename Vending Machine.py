#This is the vending machine program.
#It lets users buy snacks and drinks, and gives change back.

#Store all items in the machine.
#Each item has a code (like A1), name, price, category, and how many are left.
items = {
    'A1': {'name': 'Coca Cola', 'price': 2.00, 'category': 'Drinks', 'stock': 5},  # Cola drink option
    'A2': {'name': 'Sprite', 'price': 2.00, 'category': 'Drinks', 'stock': 0},     # Sprite drink option (not in stock)
    'A3': {'name': 'Water', 'price': 1.00, 'category': 'Drinks', 'stock': 5},      # Water option
    'B1': {'name': 'Lays Chips', 'price': 1.50, 'category': 'Snacks', 'stock': 5}, # Chips option
    'B2': {'name': 'Doritos', 'price': 2.50, 'category': 'Snacks', 'stock': 5},    # Doritos option
    'B3': {'name': 'Pringles', 'price': 2.50, 'category': 'Snacks', 'stock': 5},   # Pringles option
    'C1': {'name': 'Mars Bar', 'price': 1.50, 'category': 'Chocolate', 'stock': 5}, # Mars chocolate
    'C2': {'name': 'Snickers', 'price': 3.00, 'category': 'Chocolate', 'stock': 5}, # Snickers chocolate
    'C3': {'name': 'Coffee', 'price': 3.50, 'category': 'Hot Drinks', 'stock': 5},  # Hot coffee
    'C4': {'name': 'Tea', 'price': 2.00, 'category': 'Hot Drinks', 'stock': 5}      # Hot tea
}

#This tells the machine what else to recommend when someone purchases anything.
#For example, if someone buys coffee, suggest chocolate to go with it
suggestions = {
    'Coffee': ['C1', 'C2'],        # Suggest chocolate with coffee
    'Tea': ['C1', 'C2'],          # Suggest chocolate with tea
    'Lays Chips': ['A1', 'A2'],   # Suggest drinks with chips
    'Doritos': ['A1', 'A2'],      # Suggest drinks with doritos
    'Pringles': ['A1', 'A2']      # Suggest drinks with pringles
}

def display_menu():
    """This function shows all items available in the machine"""
    #Print the title of the menu
    print("\n=== VENDING MACHINE MENU ===")
    
    #Make groups of items by their category (drinks, snacks, etc.)
    categories = {}
    for code, item in items.items():
        category = item['category']
        if category not in categories:
            categories[category] = []
        categories[category].append((code, item))
    
    #Show each category and its items
    for category, category_items in categories.items():
        print(f"\n--- {category} ---")  # Print category name
        for code, item in category_items:
            #Show if item is in stock or not
            stock_status = "In Stock" if item['stock'] > 0 else "Out of Stock"
            #Print item details: code, name, price, and stock status
            print(f"{code}: {item['name']} - £{item['price']:.2f} - {stock_status}")

def get_money():
    """This function asks the user to put in money and checks if it's valid"""
    while True:  #Continue asking till we receive valid money.
        try:
            #Ask user to input money amount
            money = float(input("\nPlease insert money (£): "))
            if money > 0:  #Check if amount is more than 0
                return money
            print("Please insert a valid amount.")
        except ValueError:  #If user types letters instead of numbers
            print("Please enter a valid number.")

def suggest_item(item_name):
    """This function suggests other items to buy based on what was bought"""
    #Check if we have suggestions for this item
    if item_name in suggestions:
        #Get the codes of suggested items
        suggested_codes = suggestions[item_name]
        print("\nYou might also like:")
        #Show each suggested item if it's in stock
        for code in suggested_codes:
            if items[code]['stock'] > 0:
                print(f"{items[code]['name']} (Code: {code}) - £{items[code]['price']:.2f}")

def process_purchase(code, money):
    """This function handles the purchase and gives change back"""
    #Get the item details
    item = items[code]
    
    #Check if item is in stock
    if item['stock'] <= 0:
        print(f"Sorry, {item['name']} is out of stock.")
        return money, False
    
    #Check if enough money was inserted
    if money >= item['price']:
        #Calculate change
        change = money - item['price']
        #Reduce stock by 1
        items[code]['stock'] -= 1
        #Tell user item is being dispensed and show change
        print(f"\nDispensing {item['name']}...")
        print(f"Change: £{change:.2f}")
        return change, True
    else:
        print("Insufficient funds.")
        return money, False

def main():
    """This is the main program that runs everything"""
    while True:  #Keep running until user wants to exit
        #Show the menu
        display_menu()
        
        #Ask user to choose an item
        code = input("\nEnter item code (or 'exit' to quit): ").upper()
        if code.lower() == 'exit':
            break
            
        #Check if code exists
        if code not in items:
            print("Invalid code. Please try again.")
            continue
            
        #Get money and process the purchase
        money = get_money()
        remaining_money, purchase_successful = process_purchase(code, money)
        
        #If purchase worked, suggest other items
        if purchase_successful:
            suggest_item(items[code]['name'])
            
            #Ask if they want to buy more with leftover money
            if remaining_money > 0:
                buy_more = input("\nWould you like to buy anything else with your change? (yes/no): ")
                if buy_more.lower() == 'yes':
                    continue
        
        #Give back any leftover money
        if remaining_money > 0:
            print(f"\nReturning remaining money: £{remaining_money:.2f}")
        
        #Ask if they want to buy something else
        another = input("\nWould you like to make another purchase? (yes/no): ")
        if another.lower() != 'yes':
            break

    #Say goodbye when finished
    print("\nThank you for using our vending machine!")

#This starts the program when we run it
if __name__ == "__main__":
    main()