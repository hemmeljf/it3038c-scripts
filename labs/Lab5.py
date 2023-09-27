#Guess Game

import random

def number_game():

	
	getAuto = random.randint(1, 200)

print('Pick a number between 1 and 200')
	
while True: 
		
		
		guess = int(input("What is your guess: "))
	 
		if guess < getAuto:
			print('Higher. Guess again.')

		elif guess < getAuto:
			print('Lower. Guess again.')

		else:
			print('Congratulations, you guessed the right number')

	

			
	