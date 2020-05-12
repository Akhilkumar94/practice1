import random
class Coin():
    def __init__(self):
        self.side_up= 'Heads'
    def toss(self):
        ''' o for heads and 1 for tails make use of randint'''
        if random.randint(0,1)==0:
            self.side_up="Heads"
            #print("its heads")
        else:
            self.side_up="Tails"
            #print("tails")
    def get_toss(self):
        return self.side_up

mycoin=Coin()

print("this side of coin is upside is :",mycoin.get_toss())

print("are u ready for toss")

print("spin the coin:")

for count in range(10):
    mycoin.toss()
    print("up_side of coin is:",mycoin.get_toss())

print("this is for testing in git hub...no neeed to panic")

