print("="*30)
print("Welcome to the ATM System")
print("="*30)

blance = 5000
print("Balance: ", blance)

try:
    user_amount = int(input("Enter the amount to withdraw: "))
    if user_amount > blance:
        print("Invalid amount. you cannot withdraw more than your balance.")
    elif user_amount > blance:
        print("Invalid amount. you cannot withdraw more than your balance.")
    else:
        blance -= user_amount
        print("Withdrawal sucessful. your new balance is:  ", blance) 
except ValueError:
    print("Invalid input. Please enter a valid amount.")

finally:
    print("Thank you for using the ATM System.")
    