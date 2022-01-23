from enum import Enum, auto

class Color(Enum):
    WHITE = auto()
    BLACK = auto()
          
class Piece():
    def __init__(self, color):
        self.name = ""
        self.color = color
        
    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return "\033[91m" + self.name + "\033[0m"

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "r"
        
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "n"
        
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "b"
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "q"

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "k"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "p"
        
class Board():
    def __init__(self):
        self.board = [
            [
                Rook(Color.BLACK),
                Knight(Color.BLACK),
                Bishop(Color.BLACK),
                Queen(Color.BLACK),
                King(Color.BLACK),
                Bishop(Color.BLACK),
                Knight(Color.BLACK),
                Rook(Color.BLACK),
            ],
            [Pawn(Color.BLACK) for _ in range(8)],
            *[[None] * 8 for _ in range(4)],
            [Pawn(Color.WHITE) for _ in range(8)],
            [
                Rook(Color.WHITE),
                Knight(Color.WHITE),
                Bishop(Color.WHITE),
                Queen(Color.WHITE),
                King(Color.WHITE),
                Bishop(Color.WHITE),
                Knight(Color.WHITE),
                Rook(Color.WHITE),
            ],
        ]
        
class Chess():
    def __init__(self):
        self.board = Board().board
        self.turn = Color.WHITE
        
    def move(self, start, end):
        self.board[end[0]][end[1]], self.board[start[0]][start[1]] = self.board[start[0]][start[1]], None
        
    def print_board(self):
        for i in range(len(self.board)):
            tmp_str = "\033[94m" + str(-i + 8) + " \033[0m"
            for k, j in enumerate(self.board[i]):
                if j == None:
                    tmp_str += "[ ] "
                else:
                    tmp_str += ("[" + str(j) + "] ")
            print(tmp_str)
        print("\033[94m#  A   B   C   D   E   F   G   H\033[0m") 
        
if __name__ == "__main__":
    chess = Chess()
    chess.move([6, 4], [4, 4])
    chess.print_board()