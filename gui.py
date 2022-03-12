from tkinter import messagebox as mb
import tkinter as tk
def set_win(lst_wins, lst_x, lst_o):
    draw = False
    for st in lst_wins:
        if st == lst_o or st.issubset(lst_o):
            mb.showinfo("Game over", "Player   O   win !")
            draw = True
    for st in lst_wins:
        if st == lst_x or st.issubset(lst_x):
            mb.showinfo("Game over", "Player   X   win !")
            draw = True
    if (len(lst_o) == 5 or len(lst_x) == 5) and draw == False:
        mb.showinfo("Game Over", " Draw !")


lst_wins = [
    {"1", "2", "3"},
    {"1", "4", "7"},
    {"1", "5", "9"},
    {"2", "5", "8"},
    {"3", "6", "9"},
    {"3", "5", "7"},
    {"4", "5", "6"},
    {"7", "8", "9"},
]
lst_x = set()
lst_o = set()


def set_symbol1():
    if user.get() == "X":
        symbol1.set("O")
        user.set("O")
        lst_o.add("1")
    else:
        symbol1.set("X")
        user.set("X")
        lst_x.add("1")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol2():
    if user.get() == "X":
        symbol2.set("O")
        user.set("O")
        lst_o.add("2")
    else:
        symbol2.set("X")
        user.set("X")
        lst_x.add("2")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol3():
    if user.get() == "X":
        symbol3.set("O")
        user.set("O")
        lst_o.add("3")
    else:
        symbol3.set("X")
        user.set("X")
        lst_x.add("3")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol4():
    if user.get() == "X":
        symbol4.set("O")
        user.set("O")
        lst_o.add("4")
    else:
        symbol4.set("X")
        user.set("X")
        lst_x.add("4")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol5():
    if user.get() == "X":
        symbol5.set("O")
        user.set("O")
        lst_o.add("5")
    else:
        symbol5.set("X")
        user.set("X")
        lst_x.add("5")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol6():
    if user.get() == "X":
        symbol6.set("O")
        user.set("O")
        lst_o.add("6")
    else:
        symbol6.set("X")
        user.set("X")
        lst_x.add("6")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol7():
    if user.get() == "X":
        symbol7.set("O")
        user.set("O")
        lst_o.add("7")
    else:
        symbol7.set("X")
        user.set("X")
        lst_x.add("7")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol8():
    if user.get() == "X":
        symbol8.set("O")
        user.set("O")
        lst_o.add("8")
    else:
        symbol8.set("X")
        user.set("X")
        lst_x.add("8")
    set_win(lst_wins, lst_x, lst_o)


def set_symbol9():
    if user.get() == "X":
        symbol9.set("O")
        user.set("O")
        lst_o.add("9")
    else:
        symbol9.set("X")
        user.set("X")
        lst_x.add("9")
    set_win(lst_wins, lst_x, lst_o)


app = tk.Tk()
app.title(" X | O ")
user = tk.StringVar(app, value="X")
symbol1 = tk.StringVar(app, value=" ")
symbol2 = tk.StringVar(app, value=" ")
symbol3 = tk.StringVar(app, value=" ")
symbol4 = tk.StringVar(app, value=" ")
symbol5 = tk.StringVar(app, value=" ")
symbol6 = tk.StringVar(app, value=" ")
symbol7 = tk.StringVar(app, value=" ")
symbol8 = tk.StringVar(app, value=" ")
symbol9 = tk.StringVar(app, value=" ")
btn1 = tk.Button(app, height=10, width=15, command=set_symbol1, bg="#bdc3c7", fg="red",
                 textvariable=symbol1).grid(column=0, row=2)
btn2 = tk.Button(app, height=10, width=15, command=set_symbol2, bg="#bdc3c7", fg="red",
                 textvariable=symbol2).grid(column=1, row=2)
btn3 = tk.Button(app, height=10, width=15, command=set_symbol3, bg="#bdc3c7", fg="red",
                 textvariable=symbol3).grid(column=2, row=2)
btn4 = tk.Button(app, height=10, width=15, command=set_symbol4, bg="#bdc3c7", fg="red",
                 textvariable=symbol4).grid(column=0, row=3)
btn5 = tk.Button(app, height=10, width=15, command=set_symbol5, bg="#bdc3c7", fg="red",
                 textvariable=symbol5).grid(column=1, row=3)
btn6 = tk.Button(app, height=10, width=15, command=set_symbol6, bg="#bdc3c7", fg="red",
                 textvariable=symbol6).grid(column=2, row=3)
btn7 = tk.Button(app, height=10, width=15, command=set_symbol7, bg="#bdc3c7", fg="red",
                 textvariable=symbol7).grid(column=0, row=4)
btn8 = tk.Button(app, height=10, width=15, command=set_symbol8, bg="#bdc3c7", fg="red",
                 textvariable=symbol8).grid(column=1, row=4)
btn9 = tk.Button(app, height=10, width=15, command=set_symbol9, bg="#bdc3c7", fg="red",
                 textvariable=symbol9).grid(column=2, row=4)
app.mainloop()
