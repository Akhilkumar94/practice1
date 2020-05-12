import bank_account
def main():
	#acc=bank_account.Bank()

	start_bal=float(input("enter the balnce amount:"))

	savings=bank_account.Bank(start_bal)

# Deposit the amount to account
	pay=float(input("how much were u paid in this week:"))
	print("deposited amount")
	savings.deposit(pay)

	print("your acount balance is {}".format(savings.get_balance(),'.2f'),sep='')

#### withdraw the amount from account

	cash=float(input(" enter the amount to withdraw"))
	savings.with_draw(cash)
	print("the remaining balance in ur acount is {}".format(savings.get_balance(),'.2f'),sep='')

	print(savings)

main()
