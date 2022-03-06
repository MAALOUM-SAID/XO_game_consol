
import random
def tbl():
    return f"""
        +-------+-------+-------+
        |   {a}   |   {b}   |   {c}   |
        |_______|_______|_______|
        |   {d}   |   {e}   |   {f}   |
        |_______|_______|_______|
        |       |       |       |
        |   {i}   |   {g}   |   {k}   |
        +-------+-------+-------+
    """

def place_cases(smbl,place):
    global a,b,c,d,e,f,i,g,k
    if place=="1":
        try :
            a=smbl
            return tbl()
        except Exception as NameError:
            b="2"
            c="3"
            d="4"
            e="5"
            f="6"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="2":
        try :
            b=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            c="3"
            d="4"
            e="5"
            f="6"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="3":
        try:
            c=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            d="4"
            e="5"
            f="6"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="4":
        try:
            d=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            e="5"
            f="6"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="5":
        try:
            e=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            d="4"
            f="6"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="6":
        try:
            f=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            d="4"
            e="5"
            i="7"
            g="8"
            k="9"
            return tbl()
    elif place=="7":
        try:
            i=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            d="4"
            e="5"
            f="6"
            g="8"
            k="9"
            return tbl()
    elif place=="8":
        try:
            g=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            d="4"
            e="5"
            f="6"
            i="7"
            k="9"
            return tbl()
    elif place=="9":
        try:
            k=smbl
            return tbl()
        except Exception as NameError:
            a="1"
            b="2"
            c="3"
            d="4"
            e="5"
            f="6"
            i="7"
            g="8"
            return tbl()
    
def player(smbl,length):
    place=place=input("\033[1;31m"+"Player 1  : ")
    if length==1:
        print(place_cases(smbl,place))
        return place
    place_cases(smbl,place)
    return place
def auto_play(smbl,list):
    place=random.choice(list)
    print(place_cases(smbl,place))
    return place
def player1(smbl):
    place=place=input("\033[1;31m"+"Player 1  : ")
    print(place_cases(smbl,place))
    return place
def multi_players(smbl):
    place=input("\033[1;35m"+"player 2 :")
    print(place_cases(smbl,place))
    return place