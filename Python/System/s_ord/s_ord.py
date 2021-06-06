import os
import shutil

path = "/home/simone/Scaricati"

os.chdir(path)
d_list = os.listdir();

for file in d_list:
    if file.find(".") >= 0:
        t = file.rsplit(".")
        tipo = t[-1]
        if tipo == "txt" or tipo == "pdf":
            os.rename(path + "/" + file, "/home/simone/Documents/" + file)
        elif tipo == "png" or tipo == "jpg":
            os.rename(path + "/" + file, "/home/simone/Images/" + file)
        elif tipo == "deb" or tipo == "sh" or tipo == "appimage":
            os.rename(path + "/" + file, "/home/simone/Pacchetti/" + file)


