# num = int(input("Number enter karein: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
# Reverse Numbers
# num = input("Enter a number: ")

# print(num[::-1])


balance = 10000  # starting balance

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Choose option: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Money deposited. New balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw successful. Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid option")