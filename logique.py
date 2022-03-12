class Game:
    def __init__(self) -> None:
        self.a="1"
        self.b="2"
        self.c="3"
        self.d="4"
        self.e="5"
        self.f="6"
        self.i="7"
        self.g="8"
        self.k="9"
    def __str__(self) -> str:
        return f"""
+-------+-------+-------+
|   {self.a}   |   {self.b}   |   {self.c}   |
|_______|_______|_______|
|   {self.d}   |   {self.e}   |   {self.f}   |
|_______|_______|_______|
|       |       |       |
|   {self.i}   |   {self.g}   |   {self.k}   |
+-------+-------+-------+
"""
    def play(self,place,symbol):
        if place=="1":
            self.a=symbol
        elif place=="2":
            self.b=symbol
        elif place=="3":
            self.c=symbol
        elif place=="4":
            self.d=symbol
        elif place=="5":
            self.e=symbol
        elif place=="6":
            self.f=symbol
        elif place=="7":
            self.i=symbol
        elif place=="8":
            self.g=symbol
        elif place=="9":
            self.k=symbol
class Player:
    counter=0
    def __init__(self,symbol:str,game:Game) -> None:
        self.symbol=symbol
        self.game=game
        Player.counter+=1
    def player_play(self,place):
        self.game.play(place,self.symbol)



