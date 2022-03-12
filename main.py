
from logique import Game,Player
from auto import Auto
import termcolor as tr
def head_game(game:Game):
    print(tr.colored("\n            Welcome To the X | O game",color="blue",attrs=["underline","bold"]))
    print(tr.colored("\nplease enter number of the place you want to play",color="green",attrs=["blink","bold"]))
    print(tr.colored(game,color="white",on_color="on_green",attrs=["bold"]))
def playing(plyaer,lst_player,game,player_win):
    place=input(f"enter the place player: ")
    # Add place to set
    lst_player.add(place)
    plyaer.player_play(place)
    for st in lst_wins:
        if st==lst_player or st.issubset(lst_player):
            print("player 1 win !")
            player_win=True
            break
    print(game)
    return player_win
# List Win
lst_wins=[
    {"1","2","3"},
    {"1","4","7"},
    {"1","5","9"},
    {"2","5","8"},
    {"3","6","9"},
    {"3","5","7"},
    {"4","5","6"},
    {"7","8","9"},
]
lst_player1=set()
lst_player2=set()
lst_auto=set()
# Playing
game=Game()
head_game(game)
p1_symbol=tr.colored(input("choose the Symbol X or O : "),color="green",attrs=["bold"])
if p1_symbol=="X":
    p2_symbol=tr.colored("O",color="red",attrs=["bold"])
else:
    p2_symbol=tr.colored("X",color="blue",attrs=["bold"])
player_win=False
auto=Auto(p2_symbol,game)
# play  with auto
counter=0
def play_with_auto():
    while counter<9:
        p1=Player(p1_symbol,game)
        # p1 play
        is_over1=playing(p1,lst_player1,game,player_win)
        if is_over1 or counter==9:
            break
        # auto play
        is_over2=auto.playing(lst_player1,game,player_win,lst_wins,lst_auto)
        if is_over2 or counter==9:
            break
def multi_player():
    while Player.counter<9:
        p1=Player(p1_symbol,game)
        # p1 play
        is_over1=playing(p1,lst_player1,game,player_win)
        if is_over1 or Player.counter==9:
            break
        # p2 play
        p2=Player(p2_symbol,game)
        is_over2=playing(p2,lst_player2,game,player_win)
        if is_over2  or Player.counter==9:
            break
play_with=input("If you want to play with your friend enter Y or N : ")
if play_with.lower()=="y":
    multi_player()
else:
    play_with_auto()
