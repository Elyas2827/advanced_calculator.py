# ============================================
# Advanced Calculator Application
# Developed by Elyas Gul
# ============================================

import math

# Global history list
history = []


# ---------- Utility Functions ----------

def print_line():
    print("=" * 50)


def show_menu():
    print_line()
    print("        ADVANCED PYTHON CALCULATOR")
    print_line()
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root")
    print("9. View History")
    print("10. Clear History")
    print("0. Exit")
    print_line()


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# ---------- Calculator Operations ----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b


def square_root(a):
    if a < 0:
        return "Error! Negative number."
    return math.sqrt(a)


# ---------- History Management ----------

def add_to_history(operation):
    history.append(operation)


def show_history():
    if not history:
        print("No history available.")
    else:
        print_line()
        print("Calculation History:")
        for item in history:
            print(item)
        print_line()


def clear_history():
    history.clear()
    print("History cleared successfully!")


# ---------- Main Program ----------

def main():
    while True:
        show_menu()

        choice = input("Select an option: ")

        if choice == "0":
            print("Thank you for using calculator!")
            break

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            elif choice == "5":
                result = power(num1, num2)
                operation = f"{num1} ^ {num2} = {result}"

            elif choice == "6":
                result = modulus(num1, num2)
                operation = f"{num1} % {num2} = {result}"

            elif choice == "7":
                result = floor_division(num1, num2)
                operation = f"{num1} // {num2} = {result}"

            print("Result:", result)
            add_to_history(operation)

        elif choice == "8":
            num = get_number("Enter number: ")
            result = square_root(num)
            operation = f"√{num} = {result}"
            print("Result:", result)
            add_to_history(operation)

        elif choice == "9":
            show_history()

        elif choice == "10":
            clear_history()

        else:
            print("Invalid choice! Please select valid option.")


# Run Program
if __name__ == "__main__":
    main()
