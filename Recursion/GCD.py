# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# Tower of Hanoi using Recursion:
# The idea is to use the Auxiliary node to reach the destination using recursion. Below is the pattern for this problem:

# 1) Shift ‘N-1’ disks from ‘A’ to ‘B’, using C.
# 2)Shift last disk from ‘A’ to ‘C’.
# 3)Shift ‘N-1’ disks from ‘B’ to ‘C’, using A.
# where A--> Source peg
# B--> Source peg
# C--> Source peg

def tower_of_hanoi(n, source, auxiliary, target):
    # if n == 1:
        # print(f"Move disk 1 from {source} to {target}")
    if n == 0:
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

def main():
    while True:
        print("\nMenu:")
        print("1. Solve Tower of Hanoi")
        print("2. Display minimum number of steps")
        print("3. Exit")

        choice = input("Enter your choice: ")
        while choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        print("")

        choice = int(choice)
        if choice == 1:
            try:
                n = int(input("Enter the number of disks: "))
                if n <= 0:
                    print("Invalid input. Please enter a positive integer.")
                else:
                    print(f"\nSolution for {n} disks:")
                    tower_of_hanoi(n, 'A', 'B', 'C')
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 2:
            try:
                n = int(input("Enter the number of disks: "))
                if n <= 0:
                    print("Invalid input. Please enter a positive integer.")
                else:
                    min_steps = 2**n - 1
                    print(f"The minimum number of steps for {n} disks is {min_steps}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 3:
            print("Exiting the program.....\nDhanyavad ji, phir milenge...")
            print("Created by")
            print("Aakash Jha")
            break

if __name__ == "__main__":
    main()