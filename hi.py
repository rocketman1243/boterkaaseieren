def inputIsFalse(a, b):
    if a < 0 or a > 2 or b < 0 or b > 2:
        print("Wrong input! Should be either 0, 1, or 2. Pls type again!")
        return True
    else:
        print("all ok")
        print( a < 0 or a > 2 or b < 0 or b > 2 )
        return False

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
                   self.board[2][2]
        )) 

print("Welcome to Boter, Kaas en Eieren. To play, first enter two user names.")
u1 = input("user 1 (who will play as X:")
u2 = input("user 2 (who will play as O:")

b1 = Board()
print("Initial board:")
b1.getData()

print(inputIsFalse(2, 100))

print("Enter two coordinates (x,y, 0-indexed) to place a marker.")

finished = False
while (not finished):
    u1x = int(input("User 1 x:"))
    u1y = int(input("User 1 y:"))
    while inputIsFalse(u1x, u1y):
        u1x = int(input("User 1 x:"))
        u1y = int(input("User 1 y:"))
   
    
    # b1 = updateBoard(u1x, u1y)
    # finished = check(b1)

    b1.getData()

    u2x = int(input("User 2 x:"))
    u2y = int(input("User 2 y:"))
    while inputIsFalse(u2x, u2y):
        u2x = int(input("User 2 x:"))
        u2y = int(input("User 2 y:"))

    # b1 = updateBoard(u2x, u2y)
    # finished = check(b1)
    
    b1.getData()


# utility functions

