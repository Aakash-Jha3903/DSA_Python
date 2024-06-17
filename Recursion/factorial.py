def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


try:
    num = float(input("Enter a whole number to finds its factorial : "))
    if num >= 0:
        print(f"The factorial of {num} is {fact(num)}")
    else:
        print("Invalid input try again")
except Exception as e:
    print(f"Oops an error occured !\n{str(e)} \nTry again ")
finally:
    print("\nDhanyavad ji , fhir milengee ....")
    print("Created by")
    print("Aakash Jha")
