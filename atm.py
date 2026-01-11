# *atm with otp*

import random

balance = 1000  # fixed balance

for i in range(100):   # infinite loop

    print("\n----- ATM MENU -----")

    # Generate OTP
    otp = random.randint(1000, 9999)
    print("Your OTP is:", otp)

    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("✅ OTP Verified")

        print("\nPress 1 for Deposit")
        print("Press 2 for Withdrawal")
        print("Press 3 for Check Balance")
        print("Press 4 for Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("✅ Amount Deposited")
            print("Current Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            if amount > balance:
                print("❌ Insufficient Balance")
            else:
                balance -= amount
                print("✅ Withdrawal Successful")
                print("Remaining Balance:", balance)

        elif choice == 3:
            print("💰 Current Balance:", balance)

        elif choice == 4:
            print("🙏 Thank you for using ATM")
            break

        else:
            print("❌ Invalid Choice")

    else:
        print("❌ Invalid OTP")         