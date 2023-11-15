class Board:
    
    def __init__(self):
        self.board = [[[]for row in range(8)] for col in range(8)]

    def show(self):
        for row in range(8):
            print(self.board[row])

    def put(self, item, location): #location is a tuple
        row = location[0]
        col = location[1]
        self.board[row][col] = item.name
    
    def move(self, source, destination):
        sr = source[0]
        sc = source[1]
        dr = destination[0]
        dc = destination[1]
        if self.board[sr][sc] != []:
            piece = self.board[sr][sc]
            self.board[dr][dc] = piece
            self.board[sr][sc] = []
        

        
# piece needs to know what kind it is, and where it is located
class Piece:
    def __init__(self, board, piece, name = None, location = None):
        self.board = board
        self.piece = piece
        if piece == 1:
            self.name = "P"
        elif piece == 2:
            self.name = "K"
        elif piece == 3:
            self.name = "B"
        elif piece ==  4:
            self.name = "R"
        elif piece == 5:
            self.name = "Q"
        elif piece == 6:
            self.name = "K"




board = Board()

p1 = Piece(board, 5)
board.put(p1, (0,0))
board.show()
print()
board.move((0, 1),(2, 3))
board.show()
print()
board.move((0, 0),(6, 5))
board.show()
