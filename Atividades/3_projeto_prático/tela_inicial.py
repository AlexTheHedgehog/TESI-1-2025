import tkinter as tk
from cadastro import Cadastro
import sqlite3


class TelaInicial:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('800x500')
        self.janela.title('Gerenciador de Finanças')
        self.var_usuario = tk.StringVar()
        self.var_senha = tk.StringVar()
        
        self.frm_login = tk.Frame(self.janela)
        self.frm_login.pack(expand=True)
        
        self.lbl_usuario = tk.Label(self.frm_login, text='Login: ')
        self.lbl_usuario.grid(row=0, column=0)
        self.ent_usuario = tk.Entry(self.frm_login, textvariable=self.var_usuario)
        self.ent_usuario.grid(row=0, column=1, columnspan=3)
        
        self.lbl_senha = tk.Label(self.frm_login, text='Senha: ')
        self.lbl_senha.grid(row=1, column=0)
        self.ent_senha = tk.Entry(self.frm_login, textvariable=self.var_senha, show='*')
        self.ent_senha.grid(row=1, column=1, columnspan=3)
        
        self.btn_entrar = tk.Button(self.frm_login, text='Entrar', width=10)
        self.btn_entrar.grid(row=2, column=0, columnspan=2)
        self.btn_cadastrar = tk.Button(self.frm_login, text='Cadastrar', width=10)
        self.btn_cadastrar.grid(row=2, column=2, columnspan=2)

gui = tk.Tk()
TelaInicial(gui)
gui.mainloop()