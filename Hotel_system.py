menu = {
    "Salad": 50,
    "Tea": 80,
    "Paratha": 90,
    "Egg": 60,
    "Bread": 20,
    "Rice": 150
}

def display_menu():
    print("\n-----WELCOME TO QUETTA HOTEL-----")
    print("-" * 35)
    print(f"{'Item':<15} {'Price':>10}")
    print("-" * 35)
    for item, price in menu.items():
        print(f"{item:<15} Rs {price:>7}")
    print("-" * 35)

def take_order():
    order = {}
    total_amount = 0

    while True:
        item = input("\nSelect item to order (or type 'done' to finish): ").strip().title()

        if item == "Done":
            break

        if item in menu:
            quantity = input(f"How many {item}(s) do you want? ").strip()

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
                total_amount += menu[item] * quantity
                print(f"{quantity}x {item} added. Subtotal: Rs {menu[item] * quantity}")
            else:
                print("Invalid quantity. Please enter a positive number.")
        else:
            print(f"Sorry! '{item}' is not available. Please choose from the menu.")

    return order, total_amount

def display_receipt(order, total_amount):
    if not order:
        print("\nNo items ordered. Come back soon!")
        return

    print("\n-----YOUR RECEIPT-----")
    print("-" * 35)
    print(f"{'Item':<15} {'Qty':>5} {'Price':>10}")
    print("-" * 35)
    for item, qty in order.items():
        print(f"{item:<15} {qty:>5} Rs {menu[item] * qty:>7}")
    print("-" * 35)
    print(f"{'TOTAL':<15} {'':>5} Rs {total_amount:>7}")
    print("-" * 35)
    print("\nThank you for dining at Quetta Hotel!")
    print("Please visit again!")

def main():
    display_menu()
    order, total_amount = take_order()
    display_receipt(order, total_amount)

main()