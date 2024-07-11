def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                item = input("Enter the item to add: ").strip().lower()
                shopping_list.append(item)
                if item == "":
                    shopping_list.pop()
                    break
            print(shopping_list)
            print(len(shopping_list))
        elif choice == "2":
            while True:
                if len(shopping_list) == 0:
                    print("No items in your list")
                    break
                elif len(shopping_list) > 0:
                    print(f"Items in the shopping list: {shopping_list}")
                    item = input("remove an item (hit the 'Enter' key twice when you're done): ").strip().lower()
                    if item == "":
                        break
                    else:
                        shopping_list.remove(item)
            print(shopping_list)
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
