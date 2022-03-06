from logique import multi_players,player1
win_lst = [
    {"1", "2", "3"},
    {"4", "5", "6"},
    {"7", "8", "9"},
    {"1", "4", "7"},
    {"2", "5", "8"},
    {"3", "6", "9"},
    {"1", "5", "9"},
    {"3", "5", "7"}
]
lst_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player_checked = set()
plaer2_checked = set()

def two_players(symbol,auto_symbol):
    game_over=0
    is_player1 = False
    is_player2 = False
    while game_over < 9:
        # Player1
        if len(lst_nums)!=0:
            x= player1(symbol)
            player_checked.add(x)
            if x in lst_nums:
                lst_nums.remove(x)
            for i in win_lst:
                if player_checked.issuperset(i):
                    print("\033[1;31m"+"Game over Player1 win !")
                    is_player1 = True
            if is_player1:
                break
        # Player2
        if len(lst_nums)!=0:
            y = multi_players(auto_symbol)
            plaer2_checked.add(y)
            if y in lst_nums:
                lst_nums.remove(y)
            for i in win_lst:
                if plaer2_checked.issuperset(i):
                    print("\033[1;35m"+"Game over Player2 win !")
                    is_player2 = True
            if is_player2:
                break
        if game_over==8:
            print("\033[1;34m"+"Draw ! ")
        game_over+=2
