print("Rana Bilal")



balance = 5000

print(" ATM Machine")

print("1. Balance Check")
print("2. Deposit")
print("3. Withdraw")

choice = input("Option select karein: ")

if choice == "1":
    print(" Balance:", balance)

elif choice == "2":
    amount = int(input("Deposit amount: "))
    balance = balance + amount
    print(" New Balance:", balance)

elif choice == "3":
    amount = int(input("Withdraw amount: "))

    if amount <= balance:
        balance = balance - amount
        print(" Remaining Balance:", balance)
    else:
        print(" Balance kam hai")

else:
    print(" Invalid option")