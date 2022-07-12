# Importações
from cgitb import text
from tkinter import *
# Criar Janela
janela = Tk()
janela.title('ATLAS')
# Criar Textos
texto_orientacao = Label(janela, text="ATLAS")
texto_orientacao.grid(column=0, row=0)
texto_orientacao2 = Label(janela, text="Mapeamento de informações")
texto_orientacao2.grid(column=0, row=1)

# Botão Fechar
botao_close = Button(janela, text="Fechar", command=janela.destroy)
botao_close.grid(column=0, row=2)
# Manter janela aberta
janela.mainloop()