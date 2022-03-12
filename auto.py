from logique import Game
import random
class Auto:
    def __init__(self,symbol:str,game:Game) -> None:
        self.__symbol=symbol
        self.__game=game
    @property
    def symbol(self)->str:
        return self.__symbol
    @symbol.setter
    def symbol(self,nv_symbol:str)->None:
        self.__symbol=nv_symbol
    @property
    def game(self)->str:
        return self.__game
    @game.setter
    def game(self,nv_game:str)->None:
        self.__game=nv_game
    def auto_play(self,list_win:list[set],list_player:set,list_auto:set):
        list_choices=["1","2","3","4","5","6","7","8","9"]
        for lst_player in list(list_player):
            list_choices.remove(lst_player)
        for lst_auto in list(list_auto):
            list_choices.remove(lst_auto)
        if len(list_player)>1:
            for lst in list_win:
                if lst.issuperset(list_player):
                    list_choices_d=lst.difference(list_player)
                    place =random.choice(list(list_choices_d))
                    return place
        place =random.choice(list(list_choices))
        return place
    def playing(self,list_player,game,player_win,list_win,lst_auto):
        place=self.auto_play(list_win,list_player,lst_auto)
        # Add place to set
        lst_auto.add(place)
        self.__game.play(place,self.__symbol)
        for st in list_win:
            if st==lst_auto or st.issubset(lst_auto):
                print("auto win !")
                player_win=True
                break
        print(game)
        return player_win
