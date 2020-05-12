class Bank:
	def __init__(self,bal):
		self.__balance=bal
	def deposit(self,amount):
		self.__balance+=amount

	def with_draw(self,amount):
		if self.__balance >=amount:
			self.__balance -=amount
		else:
			print('insufficeint data')

	def get_balance(self):
		return self.__balance
	def __str__(self):
		return 'the balance is {}'.format(self.__balance)

