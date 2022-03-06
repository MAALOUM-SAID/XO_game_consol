
from logique import player, auto_play
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
# print(tbl())
lst_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player_checked = set()
auto_checked = set()
def auto_player(symbol,auto_symbol):
    first=True
    game_over = 0
    is_player = False
    is_auto = False
    while game_over < 9:
        if len(lst_nums) > 1:
            x = player(symbol, len(lst_nums))
            if x in lst_nums:
                lst_nums.remove(x)
            player_checked.add(x)
            for i in win_lst:
                if player_checked.issuperset(i):
                    print("Game over Player win !")
                    is_player = True
        elif len(lst_nums) == 1:
            x = player(symbol, len(lst_nums))
            if x in lst_nums:
                lst_nums.remove(x)
            player_checked.add(x)
            for i in win_lst:
                if player_checked.issuperset(i):
                    print("\033[1;35m"+"Game over Player win !")
                    is_player = True
        # Auto play
        if len(lst_nums) > 0:
            if first:
                y = auto_play(auto_symbol, lst_nums)
                auto_checked.add(str(y))
                if y in lst_nums:
                    lst_nums.remove(y)
                first=False
                continue
            if len(player_checked)>=2:
                for i in win_lst:
                    if player_checked.issubset(i):
                        z=i.difference(player_checked).pop()
                        auto_play(auto_symbol, z)
                        auto_checked.add(str(z))
                        if z in lst_nums:
                            lst_nums.remove(z)
                        break
                    elif player_checked.issuperset(i):
                        x=player_checked.difference(i).pop()
                        auto_play(auto_symbol,x)
                        auto_checked.add(str(x))
                        if x in lst_nums:
                            lst_nums.remove(x)
                        break
                else:
                    m = auto_play(auto_symbol, lst_nums)
                    auto_checked.add(str(m))
                    if y in lst_nums:
                        lst_nums.remove(m)
                for i in win_lst:
                    if auto_checked.issuperset(i):
                        print("\033[1;35m"+"Game over Auto win !")
                        is_auto = True
        if is_player or game_over==7 or is_auto:
            break
        if game_over==8:
            print("\033[1;35m"+"Draw!")
        game_over += 2
#auto_player()



