
import tkinter as tk
import random
from tkinter import messagebox

# -----------------------------
# Game Setup
# -----------------------------
board = [" "] * 9
current_player = "X"  # Player starts first

# -----------------------------
# Check Winner Function
# -----------------------------
def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "Tie"
    return None

# -----------------------------
# Computer Move (Smarter Random)
# -----------------------------
def computer_move():
    empty = [i for i in range(9) if board[i] == " "]

    # Try to win
    for move in empty:
        board[move] = "O"
        if check_winner() == "O":
            return move
        board[move] = " "

    # Try to block player
    for move in empty:
        board[move] = "X"
        if check_winner() == "X":
            board[move] = "O"
            return move
        board[move] = " "

    # Otherwise, pick random
    move = random.choice(empty)
    board[move] = "O"
    return move

# -----------------------------
# Handle Player Move
# -----------------------------
def player_move(index):
    global current_player

    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled", disabledforeground="#89b4fa")

        winner = check_winner()
        if winner:
            end_game(winner)
            return

        # Computer turn
        comp_index = computer_move()
        buttons[comp_index].config(text="O", state="disabled", disabledforeground="#f38ba8")

        winner = check_winner()
        if winner:
            end_game(winner)

# -----------------------------
# End Game Function
# -----------------------------
def end_game(winner):
    if winner == "X":
        messagebox.showinfo("Result", "✅ You Win!")
    elif winner == "O":
        messagebox.showinfo("Result", "❌ Computer Wins!")
    else:
        messagebox.showinfo("Result", "🤝 It's a Tie!")

    # Disable all buttons after game ends
    for btn in buttons:
        btn.config(state="disabled")

# -----------------------------
# Restart Game Function
# -----------------------------
def restart_game():
    global board
    board = [" "] * 9
    for btn in buttons:
        btn.config(text=" ", state="normal")

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Tic Tac Toe (AI Smart)")
root.geometry("360x430")
root.config(bg="#1e1e2e")

title = tk.Label(root, text="🎮 Tic Tac Toe (AI Smart)",
                 font=("Helvetica", 18, "bold"), bg="#1e1e2e", fg="#f8f8f2")
title.pack(pady=20)

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Helvetica", 20, "bold"),
                    width=5, height=2, bg="#313244", fg="white",
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

restart_btn = tk.Button(root, text="🔁 Restart Game", font=("Helvetica", 12, "bold"),
                        bg="#a6e3a1", fg="black", command=restart_game)
restart_btn.pack(pady=20)

root.mainloop()

