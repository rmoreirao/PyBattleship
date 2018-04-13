from random import randint


class Battleship(object):
    CHAR_WATER = '~~~'
    CHAR_BOAT = '<0>'
    CHAR_EXPLODE = '<X>'
    CHAR_MISSED = '~X~'
    CHAR_UNKNOWN = '???'

    def __init__(self, user1: str, user2: str, maxTries: int, rows: int, cols: int, boats: int):
        self.maxTries = maxTries
        self.user1 = user1
        self.user2 = user2
        self.rows = rows
        self.cols = cols
        self.boats = boats

        self.currentRound = 1
        self.usersBoard = {user1: self.getNewBoard(), user2: self.getNewBoard()}

    def getRandRowColIndex(self):
        return (randint(0, self.rows - 1), randint(0, self.cols - 1))

    def getNewBoard(self):
        board = [[self.CHAR_WATER for x in range(self.cols)] for y in range(self.rows)]
        for i in range(self.boats):
            row, col = self.getRandRowColIndex()
            while board[row][col] == self.CHAR_BOAT:
                row, col = self.getRandRowColIndex()

            board[row][col] = self.CHAR_BOAT
        return board

    def getUserInputFromPrompt(self, user):
        # TODO
        return (1, 1)

    def getUserInputRandom(self, user):
        row, col = self.getRandRowColIndex()
        print("User " + user + " selected (row,col) = (" + str(row + 1) + "," + str(col + 1) + ")")
        return row + 1, col + 1

    def getOtherUser(self, currentUser):
        if (currentUser == self.user1):
            return self.user2
        else:
            return self.user1

    def updateBoardWithInputAndReturnNextPlayer(self, currentUser, row, column):
        otherUser = self.getOtherUser(currentUser)

        value = self.usersBoard[otherUser][row - 1][column - 1]
        newValue = {
            self.CHAR_WATER: self.CHAR_MISSED,
            self.CHAR_MISSED: self.CHAR_MISSED,
            self.CHAR_BOAT: self.CHAR_EXPLODE,
            self.CHAR_EXPLODE: self.CHAR_EXPLODE
        }.get(value)
        self.usersBoard[otherUser][row - 1][column - 1] = newValue
        self.currentRound += 1
        if value == self.CHAR_BOAT:
            print("Nice! You destroyed one boat of " + otherUser + "!")
            return currentUser;

        print("Oh noh! You missed! Give a chance to " + otherUser + "...")
        return otherUser

    def drawUserBoards(self, currentUser):
        print("\n--------> Current Player [" + currentUser + "] Round [" + str(self.currentRound) + "]<--------")
        print("Board of [" + currentUser + "] Safe Boats [" + str(
            self.countLiveBoatsForUser(currentUser)) + "]:")
        self.drawUserBoard(currentUser, True)

        self.drawOtherUserBoard(currentUser)

    def drawOtherUserBoard(self, currentUser):
        otherUser = self.getOtherUser(currentUser)
        print("[" + currentUser + "\'s] view of [" + otherUser + "] Sinked Boats [" + str(
            self.boats - self.countLiveBoatsForUser(otherUser)) + "]:")
        self.drawUserBoard(otherUser, False)

    def drawUserBoard(self, currentUser, ownUserBoard: bool):
        board = self.usersBoard[currentUser]
        title = "\t"
        for i in range(self.cols):
            title += str(i + 1) + "\t"

        print(title)

        for i in range(len(board)):
            rowStr = str(i + 1) + "\t"
            for j in range(len(board[i])):
                if ownUserBoard:
                    rowStr += board[i][j] + "\t"
                else:
                    rowStr += {
                                  self.CHAR_WATER: self.CHAR_UNKNOWN,
                                  self.CHAR_MISSED: self.CHAR_MISSED,
                                  self.CHAR_BOAT: self.CHAR_UNKNOWN,
                                  self.CHAR_EXPLODE: self.CHAR_EXPLODE
                              }.get(board[i][j]) + "\t"

            print(rowStr)

    def countLiveBoatsForUser(self, user):
        return sum(x.count(self.CHAR_BOAT) for x in self.usersBoard[user])

    def getWinner(self):
        winners = []

        if self.countLiveBoatsForUser(self.user1) == 0:
            winners.append(self.user1)

        if self.countLiveBoatsForUser(self.user2) == 0:
            winners.append(self.user2)

        if len(winners) == 0:
            return None
        else:
            return ",".join(winners)
