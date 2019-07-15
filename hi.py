class Board:
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def getData(self):
        print("{0} {1} {2} \n{3} {4} {5} \n{6} {7} {8}".format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2]))


b1 = Board()
b1.getData()
