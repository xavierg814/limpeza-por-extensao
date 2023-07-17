import os
import sys

#imports para a parte de UI 
from tkinter import *
from tkinter import Tk, ttk
from tkinter.ttk import *
from tkinter import messagebox

def limpar_extensao():
    extensao = input("selecione o tipo de extensão desejada ")
    dir = input("selecione o caminho a ser limpo ")
    list_dir = os.listdir(dir)
    for item in list_dir:
        if item.endswith(f"{extensao}"):
            os.remove(os.path.join(dir, item))
            print(f"Item {item} deletado")

### -- PARTE RESPONSÁVEL PELA UI -- ###


# - Criação da janela
janela = Tk()
janela.title("limpeza de arquivos")
width = 700
height = 400

# - Labels e  Botões

# Título #

titulo = Label(janela, text='Automção para limpeza de arquivos', anchor='center', foreground='darkblue', background='darkgray', font=('Helvetica', 40), padding='5')
titulo.pack(fill='both')

subtitulo = Label(janela, text='Favor selecionar a extensão do arquivo e o caminho a ser limpo', ancho='center', foreground='darkblue', background='darkgray', font=('Helvetica', 15))
subtitulo.pack(pady=20)

# Legenda # 

labelpath = Label(text='Informe o caminho a ser limpo', font=('Helvetica', 12), foreground='brown')
labelpath.pack(anchor='w', padx=30)

labelext = Label(text='Informe (com ponto . ) a extensão a ser deletada', font=('Helvetica', 12), foreground='brown')
labelext.pack(anchor='w', padx=30)

# Botão # 

bt_iniciar = Button(janela, text='Iniciar', padding='8', command=limpar_extensao)
bt_iniciar.pack(side='left', padx=120,  expand=True)

janela.mainloop()