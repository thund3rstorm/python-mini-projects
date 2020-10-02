from random import randint
import random

print("\n\t\t----https://github.com/thund3rstorm----")
print(r"""  ____      _      _    _____ _   
 / ___|_ __/ | ___| | _|___ /| |_ 
| |   | '__| |/ __| |/ / |_ \| __|
| |___| |  | | (__|   < ___) | |_ 
 \____|_|  |_|\___|_|\_\____/ \__|
                                  
""")

help = input("\nPress h for rules or press any key to START playing!! ").lower()
if help == "h":
    print("""\nIf you have played thumb cricket, then you already know the rules
While you are batting:
You have to choose a number between 1 and 6(except 5).
The computer then also chooses a number randomly, if your choice is different from computers then
your number will be added to your score and if computer's choice and your choice of numbers are the same then
you will be declared as OUT!
While Batting:
you have to guess the number what the computer may have chosen, if the number matches then the computer will be declared as OUT!\n
You score just have to be higher than computer's in order to win the match.""")


overs=int(input("\nEnter number of overs: \n"))
balls = overs * 6
valid=["H","T"]
print("Ready for Toss\n")
decision = 0
valid_hits= [1,2,3,4,6]
while True:
    toss = input("press H for HEADS, T for TAILS\n").upper()
    if toss in valid:
        coin = randint(1,2)
        if coin == 1:
            toss_result = "H"
        if coin == 2:
            toss_result = "T"
        if toss == toss_result:
            print("You have won the toss!\n")
            while True:
                decision = input("Press 1 To Bat First or Press 2 to Bowl First: ")
                if decision.isnumeric()==True:
                    decision=int(decision)
                    if decision == 1:
                        break
                    elif decision == 2:
                        break
                else:
                    print("\nInvalid Choice!") 
        else:
            print("You have lost the toss!")
            decision = randint(1,2)
            if decision == 1:
                print("The Computer chose to BAT first\n")
            else:
                print("The Computer chose to BOWL first\n")
        break
    else:
        print("\nInvalid Input!")

def player_bats(chase):
    global balls
    p_balls=balls
    score=0
    print("\nStart batting! Enter a number between 1 to 6 (except 5)\n")
    while True:
        bat_hit=input("\n")
        if bat_hit.isnumeric():
            bat_hit=int(bat_hit)
            if bat_hit in valid_hits:
                bowl_hit=random.choice(valid_hits)
                print("\nComputer's choice: ", bowl_hit)
                if bat_hit==bowl_hit:
                    print("\nOUT! Your Final score: ", score)
                    return score
                    break
                else:
                    score += bat_hit
                    p_balls -= 1
                    print("\nYour current score: {} \t Balls Remaining: {} ".format(score,p_balls))
                    if score > chase:
                        return score
                        break
                    if p_balls == 0:
                        print("\nYour Final score: ", score)
                        return score
                        break
            else:
                print("\nInvalid input!")
        else:
            print("\nInvalid input!")
def comp_bats(chase):
    global balls
    c_balls=balls
    score=0
    print("\nStart bowling! Enter a number between 1 to 6 (except 5)\n")
    while True:
        bat_hit=random.choice(valid_hits)
        bowl_hit=input("\n")
        if bowl_hit.isnumeric():
            bowl_hit=int(bowl_hit)
            if bowl_hit in valid_hits:
                print("\nComputer's choice: ", bat_hit)
                if bat_hit==bowl_hit:
                    print("\nOUT! Computer's Final score: ", score)
                    return score
                    break
                else:
                    score += bat_hit
                    c_balls -= 1
                    print("\nComputer's current score: {} \t Balls Remaining: {} ".format(score,c_balls))
                    if score > chase:
                        return score
                        break
                    if c_balls == 0:
                        print("\nComputer's Final score: ", score)
                        return score
                        break
            else:
                print("\nInvalid input!")
        else:
            print("\nInvalid input!")


if decision == 1:
    player_score = player_bats(9999)
    print("\n*******INNINGS BREAK*******\n")
    print("Computer needs {} runs to win the match".format(player_score+1))
    comp_score = comp_bats(player_score)
elif decision == 2:
    comp_score = comp_bats(9999)
    print("\n*******INNINGS BREAK*******\n")
    print("You need {} runs to win the match".format(comp_score+1))
    player_score = player_bats(comp_score)

if player_score > comp_score:
    print("\nCongrats! You have won the match")
elif comp_score > player_score:
    print("\nOops! You have lost the match")
else:
    print("MATCH TIED!")
