from auto import auto_player
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
    print("\033[1;32m"+"\n\t\tWelcom to X|O Game \nEnter the number of the position you want to play in")
    print(table_game())
    print("Game Starting ..... ",end=" ")
head_game()
choice=input("\nif you want to play with your friend enter Y or N if you want to play with auto play : ")
symbol= input("X or O : ")
if symbol.upper() == "X":
    auto_symbol = "O"
else:
    auto_symbol = "X"
if choice.lower()=="y":
    two_players(symbol,auto_symbol)
else:
    auto_player(symbol,auto_symbol)