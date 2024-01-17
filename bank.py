# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = 0

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        choice_dep = int(input("Enter the amount you would like to deposit:"))
        balance = balance + choice_dep
        print("your balance is:" + str(balance))
    
        # papildini kodu šeit
     
    elif choice == '2':
        choice_with = int(input("Enter the amount you would like to withdraw:"))
        if balance < choice_with:
            print("You don't have sufficient funds")
        else:
            balance = balance - choice_with
            print("your balance is:" + str(balance))

        if balance < choice_with:
            print("You don't have sufficient funds")
            # papildini kodu šeit
     
    elif choice == '3':
        print("Your balance is" + str(balance))
        # papildini kodu šeit
        pass
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
