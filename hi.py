class Board:
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def getData(self):
        print("{0} {1} {2} \n{3} {4} {5} \n{6} {7} {8}".format(
                   self.board[0][0],
                   self.board[0][1],
                   self.board[0][2],
                   self.board[1][0],
                   self.board[1][1],
                   self.board[1][2],
                   self.board[2][0],
                   self.board[2][1],
                   self.board[2][2])
        )

print("Welcome to Boter, Kaas en Eieren. To play, first enter two user names.")
u1 = input("user 1 (who will play as X:")
u2 = input("user 2 (who will play as O:")

print("Enter two coordinates (x,y, 0-indexed) to place a marker.")


b1 = Board()
b1.getData()


