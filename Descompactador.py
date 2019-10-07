#!/usr/bin/python3
#Descompactador automático.

import sys
from pathlib import Path #Tratar caminhos e arquivos
import os #Tratar extensao de arquivos e comandos do sistema.

argumento = sys.argv

#Verifica parâmetro passado
if len(argumento) == 1:
    print("Insira um argumento!")
elif len(argumento) > 3:
    print("Aceito apenas um arquivo!")
elif len(argumento) == 2: #Se houver apenas o argumento indicando o arquivo. Extrai 
    extensao = os.path.splitext(argumento[1])
    if  extensao[1] == ".rar":
        os.system("unrar x {} > /dev/null;".format(argumento[1])) #Jogar saída para fora do terminal
        print("Arquivo descompactado para:")
        print(os.system("pwd"))
    elif extensao[1] == ".zip":
        os.system("gunzip {} > /dev/null;  ".format(argumento[1])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar":
        os.system("tar -xvf {} > /dev/null;  ".format(argumento[1])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar.gz":
        os.system("tar -vzxf  {} > /dev/null;  ".format(argumento[1])) #Jogar saída para fora do terminal
    elif extensao[1] == ".bz2":
        os.system("bunzip {} > /dev/null;  ".format(argumento[1])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar.bz2":
        os.system("tar -jxvf {} > /dev/null;  ".format(argumento[1])) #Jogar saída para fora do terminal
    else:
        print("Insira apenas arquivos compactados!")

#Se houver um argumento indicando o diretório do arquivo descompactado
elif len(argumento) == 3:
    extensao = os.path.splitext(argumento[1])
    if extensao[1] == ".rar":
        os.system("unrar x {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
        print("Arquivo descompactado para: {}".format(argumento[2]))
    elif extensao[1] == ".zip":
        os.system("gunzip {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar":
        os.system("tar -xvf {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar.gz":
        os.system("tar -vzxf  {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
    elif extensao[1] == ".bz2":
        os.system("bunzip {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
    elif extensao[1] == ".tar.bz2":
        os.system("tar -jxvf {} {} > /dev/null;  ".format(argumento[1], argumento[2])) #Jogar saída para fora do terminal
