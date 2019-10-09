#!/usr/bin/python3
import sys 
import os

argumento = sys.argv

permitidas = ['bz2', 'rar', 'zip', 'tar', 'tar.gz', 'tar.bz2'] #Formatos permitidos para descompactação.

if len(argumento) == 1:
    print("      ____  ____                _____           _       ")
    print("     |  _ \|  _ \  ___  ___  __|_   _|__   ___ | |      ")
    print("     | |_) | | | |/ _ \/ __|/ __|| |/ _ \ / _ \| |      ")
    print("     |  _ <| |_| |  __/\__ \ (__ | | (_) | (_) | |      ")
    print("     |_| \_\____/ \___||___/\___||_|\___/ \___/|_|      ")
    print("--------------------------------------------------------")

    print('Como usar: Basta executar o script e passar um arquivo como parâmetro, por exemplo: ')
    print('rdesctool.py arquivo.zip')
    sys.exit()

arquivo = argumento[1] #obtém nome do arquivo

if os.path.isfile(arquivo) == False:
    print('Arquivo nâo existe!')
    sys.exit()
else:
    print('Arquivo existe')
    quebra = arquivo.split(".", 1) #Quebra string só no primeiro ponto.
    extensao = quebra[1] #Obtém extensão do arquivo.
    print('Extensão: ', extensao)
    
    if extensao in permitidas:
        if extensao == permitidas[0]:
            os.system("bunzip2 -d {}".format(arquivo))
        elif extensao == permitidas[1]:
            os.system("rar x {}".format(arquivo))
        elif extensao == permitidas[2]:
            os.system("unzip {}".format(arquivo))
        elif extensao == permitidas[3]:
            os.system("tar xf {}".format(arquivo))
        elif extensao == permitidas[4]:
            os.system("tar -vzxf {}".format(arquivo))
        elif extensao == permitidas[5]:
            os.system("tar -vxjpf {}".format(arquivo))
    else:
        print('Extensão de arquivo não permitida. Extensões permitidas: bz2, rar, zip, tar, tar.gz, tar.bz2')

