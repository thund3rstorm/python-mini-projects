from random import randint
print("\n\t\t----https://github.com/thund3rstorm----")
print(r""" ____            _      ____                       
|  _ \ ___   ___| | __ |  _ \ __ _ _ __   ___ _ __ 
| |_) / _ \ / __| |/ / | |_) / _` | '_ \ / _ \ '__|
|  _ < (_) | (__|   <  |  __/ (_| | |_) |  __/ |   
|_| \_\___/ \___|_|\_\ |_|   \__,_| .__/ \___|_|   
                                  |_|              
 ____       _                        
/ ___|  ___(_)___ ___  ___  _ __ ___ 
\___ \ / __| / __/ __|/ _ \| '__/ __|
 ___) | (__| \__ \__ \ (_) | |  \__ \
|____/ \___|_|___/___/\___/|_|  |___/
""")


valid_choices = ["R","P","S"]
retry=1
mode=input("Press M for Multiplayer or any key to play against Computer\n").upper()
print("Rock Paper Scissors!!!\n")
if mode=="M":
	p1_name=input("Enter Player 1 name: ")
	p2_name=input("\nEnter Player 2 name: ")
	while retry==1:
		print("\nReady! Please Enter R for Rock(Stone), P for Paper and S for Scissors\n")

		while True:
			p1=input(p1_name+ "\'s Choice: ").upper()	
			if p1 not in valid_choices:
				print("\nInvalid input! Please Enter R for Rock(Stone), P for Paper and S for Scissors")
			else:
				break
		print("*******\n\n" * 20)
		while True:
			p2=input(p2_name+ "\'s Choice: ").upper()
			if p2 not in valid_choices:
				print("\nInvalid input! Please Enter R for Rock(Stone), P for Paper and S for Scissors\n")
			else:
				if p1==p2:
					print("It's a Tie")

				elif p1=='R' and p2=="P":
					print("{} Won".format(p2_name) )

				elif p1=='R' and p2=="S":
					print("{} Won".format(p1_name) )

				elif p1=='P' and p2=="R":
					print("{} Won".format(p1_name) )

				elif p1=='P' and p2=="S":
					print("{} Won".format(p2_name) )
				elif p1=='S' and p2=="P":
					print("{} Won".format(p2_name) )

				elif p1=='S' and p2=="R":
					print("{} Won".format(p2_name) )
				break
		play_again = input("\npress y to play again or any key to exit the game ").upper()
		if play_again =="Y":
			retry=1
		else:
			retry=0
			
else:
	p1_name=input("\nEnter Your name: ")
	while retry==1:
		print("\nReady! Please Enter R for Rock(Stone), P for Paper and S for Scissors\n")
		while True:
			p1=input(p1_name+ "\'s Choice: ").upper()
			if p1 not in valid_choices:
				print("\nInvalid input! Please Enter R for Rock(Stone), P for Paper and S for Scissors")
			else:
				rand_num = randint(0,2)
				if rand_num == 0:
					p2 = "R"
				elif rand_num == 1:
					p2 = "P"
				else:
					p2 = "S"

				print("\nComputer Chose {} \n".format(p2))
				if p1==p2:
					print("It's a Tie")

				elif p1=='R' and p2=="P":
					print("You Lost")

				elif p1=='R' and p2=="S":
					print("{} Won".format(p1_name) )

				elif p1=='P' and p2=="R":
					print("{} Won".format(p1_name) )

				elif p1=='P' and p2=="S":
					print("You Lost")

				elif p1=='S' and p2=="P":
					print("{} Won".format(p1_name) )

				elif p1=='S' and p2=="R":
					print("You Lost")
				break
		play_again = input("\npress y to play again or any key to exit the game ").upper()
		if play_again == "Y":
			retry=1
		else:
			retry=0
