from battleship import Battleship

MAX_TRIES = 20

gameFinished = False

user1 = "Rodrigo"
user2 = "Felipe"

battleship = Battleship(user1,user2,MAX_TRIES,2,2,1)

currentUser = user1

battleship.drawUserBoards(currentUser)

winner = None
while winner is None:
    row,column = battleship.getUserInputRandom(currentUser)
    nextUser = battleship.updateBoardWithInputAndReturnNextPlayer(currentUser,row,column)
    battleship.drawOtherUserBoard(currentUser);
    winner = battleship.getWinner()
    if winner is None:
        currentUser = nextUser
        battleship.drawUserBoards(currentUser)

print("\nCongrats " + currentUser + "! You won the game on Round [" + str(battleship.currentRound) + "]!!!")