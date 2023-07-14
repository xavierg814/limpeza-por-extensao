import os
import sys

def limpar_extensao():
    extensao = input("selecione o tipo de extensão desejada ")
    dir = input("selecione o caminho a ser limpo ")
    list_dir = os.listdir(dir)
    for item in list_dir:
        if item.endswith(f"{extensao}"):
            os.remove(os.path.join(dir, item))

limpar_extensao()