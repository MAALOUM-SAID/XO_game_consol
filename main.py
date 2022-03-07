from auto import auto_player
import termcolor as tc
from multi_players import two_players
def table_game(a=1,b=2,c=3,d=4,e=5,f=6,i=7,g=8,k=9):
    return "\033[1;33m"+f"""
        +-------+-------+-------+
        |   {a}   |   {b}   |   {c}   |
        |_______|_______|_______|
        |   {d}   |   {e}   |   {f}   |
        |_______|_______|_______|
        |       |       |       |
        |   {i}   |   {g}   |   {k}   |
        +-------+-------+-------+
    """
def head_game():
    print(tc.colored("\n\t\tWelcom to X|O Game \nEnter the number of the position you want to play in",color="green"))
    print(table_game())
    print(tc.colored("Game Starting ..... ",color="red"),end=" ")
head_game()
choice=input(tc.colored("\nif you want to play with your friend enter Y or N if you want to play with auto play: ",color="blue"))
symbol=input(f" {tc.colored('X',color='green')} or {tc.colored('O',color='red')} : ")
if symbol.upper() == "X":
    auto_symbol =tc.colored("O",color="red")
else:
    auto_symbol = tc.colored("X",color="yellow")
if choice.lower()=="y":
    two_players(tc.colored(symbol,color="green"),auto_symbol)
else:
    auto_player(tc.colored(symbol,color="green"),auto_symbol)
