import coin

def main():
	mycoin1=coin.Coin()

	print("the side is up:",mycoin1.get_toss())
	for count in range(10):
		mycoin1.toss()
		print(mycoin1.get_toss())

main()