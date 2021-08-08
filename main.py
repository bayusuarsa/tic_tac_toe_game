from tkinter import *
from tkinter import messagebox

# Todo 5. Quit Button
def quit_game():
    global window
    window.destroy()

# Todo 4. Reset Button
def reset():
    global window
    window.destroy()
    count = 0
    play()


# Todo 3. Check the Winner
def winner():
    global board
    if (board[0][0] == board[0][1] == board[0][2] == sign[0] or  # This 3 lines are Horizontals
            board[1][0] == board[1][1] == board[1][2] == sign[0] or
            board[2][0] == board[2][1] == board[2][2] == sign[0] or
            board[0][0] == board[1][0] == board[2][0] == sign[0] or  # This 3 Lines are Verticals
            board[0][1] == board[1][1] == board[2][1] == sign[0] or
            board[0][2] == board[1][2] == board[2][2] == sign[0] or
            board[0][0] == board[1][1] == board[2][2] == sign[0] or  # This 2 lines are Diagonals
            board[0][2] == board[1][1] == board[2][0] == sign[0]):
        messagebox.showinfo("Congrats!!", f"You are the Winner Player 1 with sign {sign[0]}")

    elif (board[0][0] == board[0][1] == board[0][2] == sign[1] or  # This 3 lines are Horizontals
          board[1][0] == board[1][1] == board[1][2] == sign[1] or
          board[2][0] == board[2][1] == board[2][2] == sign[1] or
          board[0][0] == board[1][0] == board[2][0] == sign[1] or  # This 3 Lines are Verticals
          board[0][1] == board[1][1] == board[2][1] == sign[1] or
          board[0][2] == board[1][2] == board[2][2] == sign[1] or
          board[0][0] == board[1][1] == board[2][2] == sign[1] or  # This 2 lines are Diagonals
          board[0][2] == board[1][1] == board[2][0] == sign[1]):
        messagebox.showinfo("Congrats!!", f"You are the Winner Player 2 with sign {sign[1]}")
    elif count == 9:
        messagebox.showinfo("It's Tie", "Let's go play another round")


# Todo 2. Change the Button with X or O
def checksign(button, row, column):
    global board, sign, count
    count += 1
    if button["text"] == "":
        if count % 2 != 0:
            button["text"] = sign[0]
            button.config(state=DISABLED, disabledforeground="Tomato",  font=('arial', 15, 'bold'))
            board[row][column] = sign[0]
            winner()
        else:
            button["text"] = sign[1]
            button.config(state=DISABLED, disabledforeground="Yellow",  font=('arial', 15, 'bold'))
            board[row][column] = sign[1]
            winner()
    else:
        messagebox.showerror("This Error", f"This Fields already have a Mark {sign[0]}or{sign[1]}")


# Todo 1. UI Setup for Tic Tac Toe Game
count = 0
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
sign = ["X", "O"]


def play():
    global window
    window = Tk()
    window.title("Tic Tac Toe Game")

    player_1 = Label(window, text="Player 1 : X", font="Times 15 bold").grid(row=0, column=1)
    player_2 = Label(window, text="Player 2 : O", font="Times 15 bold").grid(row=0, column=2)

    b1 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b1, 0, 0))
    b2 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b2, 0, 1))
    b3 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b3, 0, 2))
    b4 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b4, 1, 0))
    b5 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b5, 1, 1))
    b6 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b6, 1, 2))
    b7 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b7, 2, 0))
    b8 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b8, 2, 1))
    b9 = Button(window, text="", height=5, width=10, bg="dodgerblue", font=('arial', 15, 'bold'),
                relief="sunken", bd=3, command=lambda: checksign(b9, 2, 2))

    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)

    reset_button = Button(window, text="Reset", font="Times 15 bold", command=reset)
    reset_button.grid(row=4, column=1)

    quit_button = Button(window, text="Quit Game", font="Times 15 bold", command=quit_game)
    quit_button.grid(row=5, column=1)
    window.mainloop()


play()
