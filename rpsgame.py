import pyfiglet
from random import randint
art_msg=pyfiglet.figlet_format("Rock Paper Scissors")
print("\n\t\t----thund3rstorm----")
print(art_msg)
mode=input("Press m for Multiplayer or any key for VS COM\n")
print("Rock Paper Scissors!!!")
if mode=="m":

	p1_name=input("Enter Player 1 name: ")
	p2_name=input("Enter Player 2 name: ")

	print("Ready! Please Enter R for Rock(Stone), P for Paper and S for Scissors")

	p1=input(p1_name+ "\'s Choice: ")
	print("*******\n\n" * 20)
	p2=input(p2_name+ "\'s Choice: ")

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
else:
	p1_name=input("Enter Your name: ")
	print("Ready! Please Enter R for Rock(Stone), P for Paper and S for Scissors")

	p1=input(p1_name+ "\'s Choice: ")

	rand_num = randint(0,2)
	if rand_num == 0:
		p2 = "R"
	elif rand_num == 1:
		p2 = "P"
	else:
		p2 = "S"

	print("Computer Chose {}".format(p2))
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
		print("{} Won".format(p1_name) )

	elif p1=='S' and p2=="R":
		print("{} Won".format(p2_name) )
