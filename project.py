
# --- Restaurant Menu (using dictionary & tuple) ---
menu = {
    1: ("Pizza", 500),
    2: ("Burger", 250),
    3: ("Biryani", 300),
    4: ("Fries", 150),
    5: ("Cold Drink", 100)
}

# --- Orders list to keep track of placed orders ---
orders = []

# --- Function to display the menu (sorted by price using lambda) ---
def show_menu():
    print("\n--- Restaurant Menu ---")
    # Sort menu items by price using lambda as key function
    sorted_menu = sorted(menu.items(), key=lambda x: x[1][1])
    for item_no, (item_name, price) in sorted_menu:
        print(f"{item_no}. {item_name} - Rs. {price}")

# --- Lambda function to format order line ---
format_order_line = lambda name, qty, price: f"{qty} x {name} = Rs. {qty * price}"

# --- Function to take order from user ---
def take_order():
    while True:
        try:
            show_menu()
            choice = int(input("Enter the item number to order (0 to finish): "))
            
            if choice == 0:
                break

            if choice not in menu:
                print("❌ Invalid item number. Please try again.")
                continue
            
            quantity = int(input(f"Enter quantity for {menu[choice][0]}: "))
            
            if quantity <= 0:
                print("❌ Quantity must be at least 1.")
                continue

            item = menu[choice]
            orders.append({"name": item[0], "price": item[1], "quantity": quantity})
            print(f"✅ Added {quantity} x {item[0]} to your order.")

        except ValueError:
            print("⚠️ Please enter a valid number.")
        except Exception as e:
            print("⚠️ An unexpected error occurred:", e)

# --- Function to calculate and display bill ---
def show_bill():
    if not orders:
        print("\n🛒 No items in your order.")
        return

    print("\n🧾 --- Final Bill ---")
    total = 0
    for order in orders:
        print(format_order_line(order['name'], order['quantity'], order['price']))
        total += order["price"] * order["quantity"]
    
    print(f"Total Amount: Rs. {total}")

# --- Main script (with loop and options) ---
def main():
    print("🍴 Welcome to Food Restaurant 🍴")

    while True:
        print("\n1. Show Menu")
        print("2. Place Order")
        print("3. View Bill")
        print("4. Exit")

        try:
            option = int(input("Choose an option: "))
            
            if option == 1:
                show_menu()
            elif option == 2:
                take_order()
            elif option == 3:
                show_bill()
            elif option == 4:
                print("🙏 Thank you for visiting! Goodbye.")
                break
            else:
                print("❌ Invalid choice. Please select 1-4.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
        except Exception as e:
            print("⚠️ Something went wrong:", e)

# --- Run the program ---
if __name__ == "__main__":
    main()