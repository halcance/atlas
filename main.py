#Projeto Atlas por Magno Reis 2022
# Importações


import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


def login_clicked():
    usuario = user.get()
    senha = password.get()
    with sqlite3.connect('atlas.sqlite') as banco:
        cur = banco.cursor()
        sql = ("SELECT * FROM users")
        cur.execute(sql)
        resultados = cur.fetchall()
        banco.commit()

    validado = False
    for resultado in resultados:
        if usuario == resultado[2] and senha == resultado[3]:
            validado = True
    if validado == True:
       user_logado()
    else:
        showwarning(title='ERRO', message='Usuário e Senha incorreto.')

def user_logado():
    
    janela.withdraw()
    janela2 = tk.Toplevel()
    janela2.title('ATLAS - Interface')
    janela2.geometry('500x300')
    janela_label = tk.Label(janela2, text="ATLAS - Página Principal")
    janela_label.grid(row=0,column=0,padx=10,pady=30,columnspan=4)
    relatorio_label = tk.Label(janela2, text="Relatório")
    relatorio_label.grid(row=1,column=1,padx=5,pady=5)
    relatorio_label = tk.Label(janela2, text="Adicione eventos recentes relatando o que ocorreu")
    relatorio_label.grid(row=1,column=1,padx=5,pady=5)

def cadastrar_usuario():
    global janelacn_entry
    global janelacu_entry
    global janelacp_entry
    global janelace_entry
    global janelac
    janelac = tk.Toplevel()
    janelac.title("CADASTRAR USUÁRIO")

    #Label
    janelac_label = tk.Label(janelac, text="Cadastro de Usuário", font=("Camstasia", 15))

    janelac_label.grid(row=0,column=0,columnspan=3,pady=20)
    janelacn_label = tk.Label(janelac, text='Nome:')
    janelacn_label.grid(row=2,column=0,padx=10,pady=10)

    janelacu_label = tk.Label(janelac, text='Usuário:')
    janelacu_label.grid(row=3,column=0,padx=10,pady=10)

    janelacp_label = tk.Label(janelac, text='Senha:')
    janelacp_label.grid(row=4,column=0,padx=10,pady=10)

    janelace_label = tk.Label(janelac, text='Email:')
    janelace_label.grid(row=5,column=0,padx=10,pady=10)
    #Entry
    janelacn_entry = tk.Entry(janelac, text='Nome')
    janelacn_entry.grid(row=2, column=1, padx=10, pady=10)

    janelacu_entry = tk.Entry(janelac, text='Usuário')
    janelacu_entry.grid(row=3, column=1, padx=10, pady=10)

    janelacp_entry = tk.Entry(janelac, text='Senha')
    janelacp_entry.grid(row=4, column=1, padx=10, pady=10)

    janelace_entry = tk.Entry(janelac, text='Email')
    janelace_entry.grid(row=5, column=1, padx=10, pady=10)

    botao_cadastrar = tk.Button(janelac, text="Cadastrar", command=cad_usuario)
    botao_cadastrar.grid(row=6,column=1,padx=20,pady=20)

def cad_usuario():
    conexao = sqlite3.connect('atlas.sqlite')
    c = conexao.cursor()
    c.execute(" INSERT INTO users VALUES (null, :nome, :usuario, :senha, 0, :email) ",
     {
        'nome':janelacn_entry.get(),
        'usuario':janelacu_entry.get(),
        'senha':janelacp_entry.get(),
        'email':janelace_entry.get()
     }
     )
    conexao.commit()
    conexao.close()
    janelacn_entry.delete(0, "end")
    janelacu_entry.delete(0,"end")
    janelacp_entry.delete(0,"end")
    janelace_entry.delete(0,"end")
    janelac.destroy()
    showinfo(title="Sucesso", message="Usuário Cadastrado")


# Criar Janela
janela = tk.Tk()
janela.title('ATLAS - Sistema de Informações')
janela.resizable(False, False)
janela.geometry("600x500")

#Guardando as variáveis
user = tk.StringVar()
password = tk.StringVar()

# Criar Textos
texto_orientacao = ttk.Label(janela, text="ATLAS", font=("Helvetica", 30))
texto_orientacao.grid(row=0,column=0,padx=30,pady=30,columnspan=5)
texto_orientacao2 = ttk.Label(janela, text="Sistema de Arquivos Confidenciais")
texto_orientacao2.grid(row=1,column=0,pady=20,columnspan=5)

# Botão Entrar
botao_entrar = ttk.Button(janela, text="Entrar", command=login_clicked)
botao_entrar.grid(row=6,column=3,padx=10,pady=10)

#Botão Fechar
botao_fechar = ttk.Button(janela, text="Fechar", command=janela.destroy)
botao_fechar.grid(row=6,column=0,padx=20,pady=20)

#Botão Cadastrar
botao_fechar = ttk.Button(janela, text="Novo Usuário", command=cadastrar_usuario)
botao_fechar.grid(row=6,column=2,padx=20,pady=20)

# Tela de login
user_label = ttk.Label(janela, text='Usuário:')
user_label.grid(row=2,column=3,padx=10,pady=10)
user_entry = ttk.Entry(janela, textvariable=user)
user_entry.grid(row=3,column=3,padx=10,pady=10,sticky='w')
user_entry.focus()
password_label = ttk.Label(janela, text='Senha:')
password_label.grid(row=4,column=3,padx=10,pady=10)
password_entry = ttk.Entry(janela, textvariable=password)
password_entry.grid(row=5,column=3,padx=10,pady=10)

texto1 = ttk.Label(janela, text="-Gerenciamento Planilhas")
texto1.grid(row=3,column=0,padx=5,pady=5, ipadx=30)
texto2 = ttk.Label(janela, text="-Relatórios")
texto2.grid(row=4,column=0,padx=5,pady=10,ipadx=30)
texto3 = ttk.Label(janela, text="-Gerenciamento de Colaboradores")
texto3.grid(row=5,column=0,padx=5,pady=5,ipadx=30)

# Manter janela aberta
janela.mainloop()
