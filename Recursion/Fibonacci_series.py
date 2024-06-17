def fibo_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def print_fibonacci_series(n, method):
    print("Fibonacci series up to", n, "terms:")
    for i in range(n):
        if method == 'recursive':
            print(fibo_recursive(i))
        else:
            print(fibo_iterative(i))


def get_fibonacci_term(n, method):
    if method == 'recursive':
        return fibo_recursive(n)
    else:
        return fibo_iterative(n)


def main():
    while True:
        print("\nMenu:")
        print("1. Print Fibonacci series up to n terms")
        print("2. Get the nth term of the Fibonacci series")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        while choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        print("")

        if choice == '1':
            n = int(input("Enter the number of terms: "))
            method = input("Choose method (recursive/iterative): ").lower()
            if method in ['recursive', 'iterative']:
                print_fibonacci_series(n, method)
            else:
                print("Invalid method. Please choose 'recursive' or 'iterative'.")

        elif choice == '2':
            n = int(input("Enter the term number: "))
            method = input("Choose method (recursive/iterative): ").lower()
            if method in ['recursive', 'iterative']:
                print(f"The {n}th term is {get_fibonacci_term(n, method)}")
            else:
                print("Invalid method. Please choose 'recursive' or 'iterative'.")

        elif choice == '3':
            print("Exiting the program.....")
            print("\nDhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
