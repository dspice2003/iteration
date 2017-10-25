import random




print("Please write a number down 0 between 1000")


secret = random.randint(0,1000)

print(secret)

guess = input("is this it yes or no\n:")

if(guess == "yes"):
	print("I found it!!")

secret = random.randint(0,1000)

while(guess == "no"):
	print(secret)
	secret = random.randint(0,1000)
	guess = input("Is this it yes or no\n:")

if(guess == "yes"):
	print("I found it!!")
