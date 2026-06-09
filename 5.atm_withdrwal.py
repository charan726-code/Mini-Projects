print("======ATM Withdrawl=======")
balance = 100000
count = 0
while count <3:
    withdrawl_amount = int(input("Enter amount to withdraw:"))
    if withdrawl_amount<=balance:
        print("Transaction is successfull...")
        balance-=withdrawl_amount
        balance_display = input("Do you want check your balance(yes/no):")
        if balance_display=='yes':
            print('balance amount :',balance)
        else:
            print("Thank You...")
            break
    else:
        print("Insufficient balance!...")
        continue