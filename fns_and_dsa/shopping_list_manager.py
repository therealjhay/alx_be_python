def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager application.
    It initializes the shopping list and handles user interactions via a menu.
    """
    shopping_list = [] # Initialize an empty list to store shopping items

    while True:
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ").strip() # Get user's choice and remove leading/trailing whitespace

        if choice == '1':
            # Option to add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            # Option to remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue # Go back to the beginning of the loop

            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        elif choice == '3':
            # Option to display the shopping list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            print("--------------------------")
        elif choice == '4':
            # Option to exit the application
            print("Goodbye! Thank you for using the Shopping List Manager.")
            break # Exit the while loop
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main() # Run the main function when the script is executed
