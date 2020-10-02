from random import randint

print("\n\t\t----https://github.com/thund3rstorm----")
print(r"""  ____                       _   _          
 / ___|_   _  ___  ___ ___  | |_| |__   ___ 
| |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \
| |_| | |_| |  __/\__ \__ \ | |_| | | |  __/
 \____|\__,_|\___||___/___/  \__|_| |_|\___|
                                            
                       _               
 _ __  _   _ _ __ ___ | |__   ___ _ __ 
| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| | | | |_| | | | | | | |_) |  __/ |   
|_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
""")


help = input("\nPress h for rules or press any key to START playing!! ").lower()
if help == "h":
	print("""\n\nGuess the number is a game where you will try to guess the number which Computer has chosen randomly
First you have to choose a range of numbers in between which you are willing to guess, 
then the computer will choose a number in that range and you have to guess it!
The computer will tell you if your guess is higher or lower than actual number.
If the difference in your guess and the actual number is less or greater than 4 the computer will tell you that you are close.
There is an attempt counter in the game to check how many attempts you have taken. Try to guess the number in fewer attempts. GOOD LUCK!\n\n""")

print("\nEnter the range of numbers for the game\n")
min_no = int(input("Enter starting number "))
max_no = int(input("\nEnter last number "))
attempts=0
answer = randint(min_no,max_no)
print("\nComputer chose a number")

while True:
	guess = input("\nGuess the number in between {} and {}\n".format(min_no,max_no))
	if guess.isnumeric()==False or int(guess) not in range(min_no,max_no+1):
		print("Invalid input! Please enter a NUMBER in between the RANGE.\n")
	else:
		attempts+=1
		guess=int(guess)		
		if guess==answer:
			print("Congratulations! You guessed it right!!\t Attempts taken: {}".format(attempts))
			break
		elif guess>answer:
			diff = guess-answer
			if diff<=4:
				print("You are close!\t Attempts taken: {}".format(attempts))
			else:
				print("Too high! Try again\t Attempts taken: {}".format(attempts))
		elif guess<answer:
			diff = answer-guess
			if diff<=4:
				print("You are close!\t Attempts taken: {}".format(attempts))
			else:
				print("Too low! Try again\t Attempts taken: {}".format(attempts))

