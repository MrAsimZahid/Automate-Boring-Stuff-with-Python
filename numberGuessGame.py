#This is a guess the number game
import random
print('Hello, What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guess in range(1, 7):
	print('Take a guess')
	nGuess = int(input())

	if nGuess < secretNumber:
		print('your guess is too low')
	elif nGuess > secretNumber:
		print('your guesss is too high.')
	else:
		break
if nGuess == secretNumber:
	print('Good job, ' + name + '! you guessed my number was ' + str(guess))
else:
	print('Nope. The number I was thinking of was ' +str(secretNumber))
