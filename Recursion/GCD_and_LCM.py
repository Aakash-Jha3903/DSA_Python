# Greatest Common Divisor (GCD)
# largest number that divides two or more numbers without leaving a remainder
# It is also called the highest common factor (HCF)

# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
# LCM(a,b)=  ∣a×b∣ / GCD(a,b)

# import math
# print(math.gcd(100,200)) # 100  😂😂
# print(math.lcm(4,6))  #12  😂😂

def HCF(a, b):
    if (b == 0):
        return abs(a)
    else:
        return HCF(b, a % b)
    # while b != 0:
    # a, b = b, a % b
    # return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // HCF(a, b)
        # return (a // HCF(a,b))* b


def main():
    while True:
        print("\nMenu:")
        print("1. Calculate GCD")
        print("2. Calculate LCM")
        print("3. Exit")

        choice = input("Enter your choice: ")
        while choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        print("")

        choice = int(choice)
        if choice == 1:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = HCF(num1, num2)
                print(f"The greatest common divisor (GCD) of {
                      num1} and {num2} is {result}")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        elif choice == 2:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                result = lcm(num1, num2)
                print(f"The least common multiple (LCM) of {
                      num1} and {num2} is {result}")
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        elif choice == 3:
            print("Exiting the program.....")
            print("Dhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break


if __name__ == "__main__":
    main()
