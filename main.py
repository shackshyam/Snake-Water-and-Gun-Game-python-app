
import random

indexfile = ["SNAKE", "WATER" , "GUN"]
UserInput = int(input("Enter '0' for SNAKE , '1' For WATER and '2' For Gun : "))
Comlist = [0,1,2]
ComSel = random.choice(Comlist)

UserSelection = indexfile[UserInput]
ComSelection = indexfile[ComSel]
# print(ComSelection)
# print(random.choice(Comlist))
   
def Winner(UserInput, ComSel):
    if UserInput == ComSel:
        return "Game is Tie"
    elif (UserInput == 0 and ComSel == 1) or \
         (UserInput == 1 and ComSel == 2) or \
         (UserInput == 2 and ComSel == 0):
             return "Congress, You have Won the Game! :>"  
    else:
        return "Ohh! You Lose the Game :<"

winner = Winner(UserInput, ComSel)
print(winner)
       

print(f"You Have Selected {UserSelection} and Computer Selected {ComSelection}")
