import os
import sys
from backup_f import check_backup, confronto 

#/ Università ----> Informatica.
#/ Programs   ----> C,  Pytthon.
# mdir = ["Università","Programmi"]

# Controllo inserimento chiavetta
if check_backup("/media/simone", "F9D5-81C2") == False:
    print("Chiavetta non inserita")

#Controllo cartelle principali
os.system('cp ~/Desktop/Università /media/simone/F9D5-81C2/Università_temp')
os.system('cp ~/Programs /media/simone/F9D5-81C2/Programs_temp')

