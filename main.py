#Projeto Atlas por Magno Reis 2022
# Importações

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning

def login_clicked():
    if(user.get()=='magno' and password.get() =='master'):
        showinfo(title='info', message='BEM VINDO SENHOR CRIADOR DESTE PROGRAMA MARAVILHOSO')
    else:
        showwarning(title='ERRO', message='Usuário e Senha incorreto.')
# Criar Janela
janela = tk.Tk()
janela.title('ATLAS')
janela.resizable(False, False)
signin = ttk.Frame(janela)
signin.pack(padx=60, pady=60, fill='x', expand=True)
signin2 = ttk.Frame(janela)
signin2.pack(padx=60, pady=60, fill='y', expand=True)

#Guardando as variáveis
user = tk.StringVar()
password = tk.StringVar()

# Criar Textos
texto_orientacao = ttk.Label(signin, text="ATLAS")
texto_orientacao.pack(fill='x', expand=True)
texto_orientacao2 = ttk.Label(signin, text="Mapeamento de informações")
texto_orientacao2.pack(fill='x', expand=True)

# Botão Fechar
botao_close = ttk.Button(signin2, text="Entrar", command=login_clicked)
botao_close.pack(fill='x', side='bottom')

# Tela de login
user_label = ttk.Label(signin2, text='Usuário:')
user_label.pack(fill='y')
user_entry = ttk.Entry(signin2, textvariable=user)
user_entry.pack(fill='y', expand=False)
user_entry.focus()
password_label = ttk.Label(signin2, text='Senha:')
password_label.pack(fill='y', expand=False)
password_entry = ttk.Entry(signin2, textvariable=password)
password_entry.pack(fill='y', expand=False)

# Manter janela aberta
janela.mainloop()