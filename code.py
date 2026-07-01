print("Rana Bilal")


cash = 5000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Cash")
    print("4. Exit")

    choice = input("OPTION SELECT KAREIN: ")

    if choice == "1":
        print("Your balance is:", cash)

    elif choice == "2":
        amount = int(input("Deposit amount: "))
        cash += amount
        print("Money deposited. New balance:", cash)

    elif choice == "3":
        amount = int(input("Withdraw amount: "))
        if amount <= cash:
            cash -= amount
            print("Please collect cash. Remaining balance:", cash)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you! Exit ho raha hai...")
        break

    else:
        print("Invalid option! Try again.")