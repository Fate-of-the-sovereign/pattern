import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class ChessPiece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def __str__(self):
        return f"{self.color} {self.piece_type}"

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Pawn")

class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Rook")

class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Knight")

class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Bishop")

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "Queen")

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color, "King")

class ChessPieceFactory:
    @staticmethod
    def create_piece(color, piece_type):
        if piece_type == "Pawn":
            return Pawn(color)
        elif piece_type == "Rook":
            return Rook(color)
        elif piece_type == "Knight":
            return Knight(color)
        elif piece_type == "Bishop":
            return Bishop(color)
        elif piece_type == "Queen":
            return Queen(color)
        elif piece_type == "King":
            return King(color)
        else:
            raise ValueError(f"Unknown piece type: {piece_type}")

class ChessBoard:
    def __init__(self, root):
        self.root = root
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.images = {}
        self.cell_size = 50  # Размер клетки
        self.initialize_board()
        self.create_gui()

    def initialize_board(self):
        # Initialize pawns
        for i in range(8):
            self.board[1][i] = ChessPieceFactory.create_piece("White", "Pawn")
            self.board[6][i] = ChessPieceFactory.create_piece("Black", "Pawn")

        # Initialize other pieces
        pieces = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for i in range(8):
            self.board[0][i] = ChessPieceFactory.create_piece("White", pieces[i])
            self.board[7][i] = ChessPieceFactory.create_piece("Black", pieces[i])

    def create_gui(self):
        self.canvas = tk.Canvas(self.root, width=self.cell_size * 8, height=self.cell_size * 8)
        self.canvas.pack()

        for row in range(8):
            for col in range(8):
                x0, y0 = col * self.cell_size, row * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

                piece = self.board[row][col]
                if piece:
                    image_path = f"images/{piece.color}_{piece.piece_type.lower()}.png"
                    if image_path not in self.images:
                        self.images[image_path] = self.load_and_resize_image(image_path)
                    self.canvas.create_image(x0 + self.cell_size // 2, y0 + self.cell_size // 2, image=self.images[image_path])

    def load_and_resize_image(self, image_path):
        # Загрузка изображения и изменение его размера
        image = Image.open(image_path)
        image = image.resize((self.cell_size, self.cell_size), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chess Board")
    chess_board = ChessBoard(root)
    root.mainloop()