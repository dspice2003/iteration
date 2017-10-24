import random



guess = input("Please enter a number 0 between 1000\n:")
guess = int(guess)

secret = random.randint(0,1000)

while(guess > 1000):
	print("I cant convert that")
	guess = input("Please enter a number 0 between 1000\n:")
	guess = int(guess)


while(guess > secret):
	print("Too High")
	guess = input("Please enter a number 0 between 1000\n:")
	guess = int(guess)

while(guess < secret):
	print("Too Low")
	guess = input("Please enter a number 0 between 1000\n:")
	guess = int(guess)

if(guess == "secret"):
	print("You got it!")

