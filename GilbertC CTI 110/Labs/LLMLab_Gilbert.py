
def get_whole_number(prompt):
    """Get a valid whole number from the user."""
    while True:
        user_input = input(prompt)

        try:
            number = int(user_input)

            if number < 0:
                print("Error: Negative numbers are not allowed. Try again.")
            else:
                return number

        except ValueError:
            print("Error: Please enter a valid whole number (0 or greater).")


def calculator():
    while True:
        print("\n===== BASIC ARITHMETIC CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        # Get the two numbers from the user
        num1 = get_whole_number("Enter the first whole number: ")
        num2 = get_whole_number("Enter the second whole number: ")

        # Perform the selected operation
        if choice == "1":
            result = num1 + num2
            operator = "+"
        elif choice == "2":
            result = num1 - num2
            operator = "-"
        elif choice == "3":
            result = num1 * num2
            operator = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue

            result = num1 / num2
            operator = "/"

        # Display the complete equation and answer
        print(f"\nEquation: {num1} {operator} {num2} = {result}")


# Run the calculator
calculator()