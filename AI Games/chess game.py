
import tkinter as tk
from tkinter import messagebox

# Chess board setup
board = [
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bP"]*8,
    [""]*8,
    [""]*8,
    [""]*8,
    [""]*8,
    ["wP"]*8,
    ["wR","wN","wB","wQ","wK","wB","wN","wR"]
]

# Piece unicode characters for display
pieces = {
    "wK":"\u2654", "wQ":"\u2655", "wR":"\u2656", "wB":"\u2657", "wN":"\u2658", "wP":"\u2659",
    "bK":"\u265A", "bQ":"\u265B", "bR":"\u265C", "bB":"\u265D", "bN":"\u265E", "bP":"\u265F",
    "":""
}

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.turn = "w"  # White starts
        self.selected = None  # Selected piece
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()

    def create_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if (i+j)%2==0 else "gray"
                btn = tk.Button(self.root, text=pieces[board[i][j]], font=("Arial",24), width=4, height=2,
                                bg=color, command=lambda x=i, y=j: self.click_square(x,y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def click_square(self, x, y):
        global board
        piece = board[x][y]
        if self.selected:
            sx, sy = self.selected
            selected_piece = board[sx][sy]

            # Move only if it's correct color
            if selected_piece[0] == self.turn:
                # For simplicity, we won't check valid moves here
                board[x][y] = selected_piece
                board[sx][sy] = ""
                self.update_board()
                self.turn = "b" if self.turn=="w" else "w"
            self.selected = None
        else:
            if piece != "" and piece[0]==self.turn:
                self.selected = (x, y)

    def update_board(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j]["text"] = pieces[board[i][j]]

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGUI(root)
    root.mainloop()

