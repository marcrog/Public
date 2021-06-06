import os
import sys


Reset = "\x1b[0m"
Hidden = "\x1b[8m"

# color = ["\033[38;5;9m" ,"\x1b[34m" , "\x1b[32m","\x1b[33m","\x1b[36m", "\x1b[35m", "\x1b[37m"]
color = ["\033[38;2;226;10;23m", "\033[38;2;238;67;11m", "\033[38;2;254;115;24m", "\033[38;2;255;166;0m", "\033[38;2;255;240;1m", "\033[38;2;109;175;25m", "\033[38;2;2;129;49m", "\033[38;2;0;131;213m",
        "\033[38;2;1;60;130m", "\033[38;2;1;45;118m", "\033[38;2;55;21;98m", "\033[38;2;155;7;101m", "\033[38;2;255;255;255m"]


#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stampa(name, indent, serie, tipo):
    #Stampa prime due righe
    if tipo == "file":
        indent = indent + 1
    for x in range(0):
        a = 0
        # i parte da 0 e arriva a indent - 1 
        for i in range(indent):
            if i in serie:
                text = Hidden + "|"
            else:
                text =  color[a] + "|"
            a = a + 1
            if a >= len(color):
                a = len(color) - 1
            print(text + "\t", end='')
            print(Reset, end='')
        print()
    
    #Stampa riga file /dir colorata
    #Bisogna stamapare un indentazione in meno per fare spazio al nome del fil
    indent = indent - 1
    a = 0
    for i in range(indent):
        if i in serie:
            text = Hidden + "|"
        else:
            text = color[a] + "|"
        a = a + 1
        if a >= len(color):
            a = len(color) - 1
        print(text + "\t", end='')
        print(Reset, end='')
    
    if tipo == "file":
        file_c =  color[a] + "|______" + name
        print(file_c)
    else:
        file_c = color[a] + "|--------->" + name
        print(file_c)

# #/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


