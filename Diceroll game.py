name = input ("enter user id.")
if name == ("user1"):
    pwd= input ("enter password.")
    if pwd == ("password"):
        print ("Welcome", name)
    else:
        print ("wrong password reopen program")
        exit(5)
name = input ("enter user id player2")
if name == ("user2"):
    pwd= input ("enter password.")
    if pwd == ("password"):
        print ("Welcome", name)
    else:
            print (" Incorrect login, check details and try again")
            time.sleep(1)
            exit(1)
else:
    print("Incorrect Username Please Try Again")

import random
import time
lowestValue=1
highestValue=6

value1=random.randint(lowestValue, highestValue)
value2=random.randint(lowestValue, highestValue)

roll_again = input("would you like to play yes or no?")
if roll_again == "yes":

        print("COMPUTER-IS-PROCESSING-GAME")




print("user1 rolled",value1)
print("user2 rolled",value2)
print(" Good Game")
playAgain = input("would you like to play again yes or no?")

value3=random.randint(lowestValue, highestValue)
value4=random.randint(lowestValue, highestValue)
if playAgain == "no":
    exit(1)
if playAgain == "yes":
   
    print("user1 rolled",value3)
    print("user2 rolled",value4)
    print(" Good Game")
   


   
playAgain = input("would you like to play again yes or no?")

value5=random.randint(lowestValue, highestValue)
value6=random.randint(lowestValue, highestValue)
if playAgain == "no":
    exit(1)
if playAgain == "yes":
   
    print("user1 rolled",value5)
    print("user2 rolled",value6)
    print(" Good Game")
   

   
playAgain = input("would you like to play again yes or no?")

value7=random.randint(lowestValue, highestValue)
value8=random.randint(lowestValue, highestValue)
if playAgain == "no":
    exit(1)
if playAgain == "yes":
   
    print("user1 rolled",value7)
    print("user2 rolled",value8)
    print(" Good Game")
       


playAgain = input("would you like to play again yes or no?")

value9=random.randint(lowestValue, highestValue)
value10=random.randint(lowestValue, highestValue)
if playAgain == "no":
    exit(1)
if playAgain == "yes":
   
    print("user1 rolled",value9)
    print("user2 rolled",value10)
    print(" Good Game")
   
if playAgain == "no":
    exit(1)


user1score=(value1+value3+value5+value7+value9)
user2score=(value1+value3+value5+value7+value9)

print(" user1 you scored",user1score)
print(" user2 you scored",user2score)

if (user1score>user2score):
    print("user1 won")

if (user2score>user1score):
    print("user2won")

settleScore = input("well done its a draw would you like to settle this with a tiebreaker yes or no")
if settleScore == "no":
    print("Thanks for playing")
    exit(1)
if settleScore == "yes":

    import random
print("user1 you are HEADS")
print("user2 you are TAILS")
time.sleep(2)
tiebreaker = ["HEADS","TAILS"]
result = random.choice(tiebreaker)
print("---COMPUTER-IS-ROLLING---")
time.sleep(2)
print (result)
if result == "HEADS":
        print("user1 is the winner")
        print("Congratulatuions!")
else:
        print("user2 is the winner")
        print("Congratulatuions!")


#keeps ending in draw needed to use coin flip to get a winner
#2023
#need to add variables for users and passwords to make it so that any userid cn be used
#need to tell reopen prgrme at every wrong input
