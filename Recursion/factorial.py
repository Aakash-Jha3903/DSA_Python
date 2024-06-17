def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)


def fact_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    while True:
        print("\nMenu:")
        print("1. Calculate Factorial (Recursive)")
        print("2. Calculate Factorial (Iterative)")
        print("3. Exit")

        choice = input("Enter your choice: ")
        while choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        print("")

        choice = int(choice)
        if choice == 1:
            num = float(input("Enter a whole number to find its factorial: "))
            print(f"The factorial of {num} (recursive) is {
                fact_recursive(num)}")
        elif choice == 2:
            num = int(input("Enter a whole number to find its factorial: "))
            print(f"The factorial of {num} (iterative) is {
                fact_iterative(num)}")
        elif choice == 3:
            print("Exiting the program. Dhanyavad ji, phir milenge...")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid input. Please enter a non-negative whole number.")


if __name__ == "__main__":
    main()
