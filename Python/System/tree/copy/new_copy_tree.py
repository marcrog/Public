import os
import sys
from termcolor import colored
from colorama import Fore, Style


color = [ 'red', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'white', 'grey' ]
attrib = ['bold']

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stampa_file(name, indent, serie):
    #Stampa prime due righe
    indent = indent + 1
    for x in range(0):
        b = 0
        a = 0
        # i parte da 0 e arriva a indent - 1 
        for i in range(indent):
            if i in serie:
                text = colored("|", 'grey', attrs=['dark'])
            else:
                text = colored("|", color[a], attrs=[attrib[b]])
        
            b = b + 1
            if b == 1:
                b = 0
                a = a + 1
            print(text + "\t", end='')
        print()
    
    #Stampa riga file colorata
    #Bisogna stamapare un indentazione in meno per fare spazio al nome del file
    indent = indent - 1
    a = 0
    b = 0
    for i in range(indent):
        if i in serie:
            text = colored("|", 'grey', attrs=['dark'])
        else:
            text = colored("|", color[a], attrs=[attrib[b]])
        
        b = b + 1
        if b == 1:
            b = 0
            a = a + 1
        print(text + "\t", end='')
        
    file_c = colored("|______" + name, color[a], attrs=[attrib[b]])
    print(file_c)


#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def stampa_dir(name, indent, serie):
    #Stampa prime due righe
    for x in range(0):
        b = 0
        a = 0
        # i parte da 0 e arriva a index - 1 
        for i in range(indent):
            if i in serie:
                text = colored("|", 'grey', attrs=['dark'])
            else:
                text = colored("|", color[a], attrs=[attrib[b]])
        
            b = b + 1
            if b == 1:
                b = 0
                a = a + 1
            print(text + "\t", end='')
        print()
    
    #Stampa riga dir colorata
    #Bisogna stamapare un indentazione in meno per fare spazio al nome del file
    indent = indent - 1
    a = 0
    b = 0
    for i in range(indent):
        if i in serie:
            text = colored("|", 'grey', attrs=['dark'])
        else:
            text = colored("|", color[a], attrs=[attrib[b]])
        
        b = b + 1
        if b == 1:
            b = 0
            a = a + 1
        print(text + "\t", end='')
        
    file_c = colored(" --------->" + name, color[a], attrs=[attrib[b]])
    print(file_c)



# #/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def print_sub(path, indent, serie, last):
    os.chdir(path)
    files = os.listdir()
    dirs = []
    
    if indent == 0:
        arr = path.split('/')
        text = colored(arr[-1], color[0], attrs=[attrib[0]])
        print(text)
    else:
        stampa_dir(path, indent,serie)
        if last :
            serie.append(indent - 1)

    #Stampa file e crea lista dir
    for file in files:
        if os.path.isdir(file) == False and file[0] != '.':
            stampa_file(file, indent, serie)
        elif os.path.isdir(file) and file[0] != '.' and os.path.islink(file) == False:
            dirs.append(file)    

    if len(dirs) == 0:
        return 
    else:
        for cartella in dirs:
            if dirs.index(cartella) + 1 == len(dirs):
                last = True
            else:
                last = False
            print_sub(cartella, indent + 1, serie, last)
            if last == True:
                serie.pop(-1)
            os.chdir("../")
        last = False



#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Questo conteggio parte da 0
serie = []
last = False

print_sub(sys.argv[1], 0, serie, last)
# stampa_file("Python", 1,  serie)
# stampa_dir("Python", 2,  serie)
# print(2)
