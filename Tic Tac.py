import tkinter as tk
import random


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False





def is_full(board):
    return all(cell != " " for row in board for cell in row)
def make_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)
def player_move(row, col):
    global current_player, game_over

    if board[row][col] == " " and not game_over:
        board[row][col] = players[current_player]

        buttons[row][col].config(text=players[current_player], state="disabled")

        if check_win(board, players[current_player]):
            status_label.config(text=f"Player {players[current_player]} wins!")
            game_over = True
        elif is_full(board):
            status_label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 1 - current_player
            if current_player == 1:
                make_computer_move_and_update()

#Computer Move
def make_computer_move_and_update():
    global current_player, game_over

    if not game_over:
        row, col = make_computer_move(board)
        board[row][col] = players[current_player]
        buttons[row][col].config(text=players[current_player], state="disabled")

        if check_win(board, players[current_player]):
            status_label.config(text=f"Player {players[current_player]} wins!")
            game_over = True
        elif is_full(board):

            status_label.config(text="It's a draw!")
            game_over = True
        else:
            current_player = 1 - current_player


board = create_board()
players = ["X", "O"]
current_player = 0
game_over = False

root = tk.Tk()
root.title("Tic Tac Toe THE GAME")
buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ",bg = 'pink',fg = 'blue', font=("normal", 20), width=8, height=3,
                                  command=lambda row=i, col=j: player_move(row, col))
        buttons[i][j].grid(row=i, column=j)
status_label = tk.Label(root, text="Player X's turn", font=("normal", 14))
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
