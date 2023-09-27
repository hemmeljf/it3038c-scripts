#Guess Game

import random

def getAuto():

	return random.randint(1, 100)

print('Pick a number between 1 and 100')

auto_number = getAuto()
	
while True: 
		
		
		guess = int(input("What is your guess: "))
	 
		if guess < auto_number:
			print('Higher. Guess again.')

		elif guess > auto_number:
			print('Lower. Guess again.')

		else:
			print('Congratulations, you guessed the right number')

	

			
	
