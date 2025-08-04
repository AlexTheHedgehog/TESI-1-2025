import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        #Criar uma forma de centralizar a janela
        largura_monitor = self.janela.winfo_screenwidth()
        altura_monitor = self.janela.winfo_screenheight()
        largura_janela = 620
        altura_janela = 155
        self.janela.geometry(f'{largura_janela}x{altura_janela}+{largura_monitor//2-largura_janela//2}+{altura_monitor//2-altura_janela//2}')
        
        colunas = ['nome', 'cpf', 'email']
        self.tvw = ttk.Treeview(self.janela, height=5, columns=colunas, show='headings')
        #Configurar o cabaçalho das colunas
        self.tvw.heading('nome', text='NOME')
        self.tvw.heading('cpf', text='CPF')
        self.tvw.heading('email', text='EMAIL')
        #Preencher a tabela
        self.tvw.insert('', 'end', values=('Daniel', '20230300001', 'daniel.chaves@sou.ufac.br'))
        self.tvw.insert('', 'end', values=('Manoel', '00000000000', 'manoel@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste1', '00000000000', '1@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste2', '00000000000', '2@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste3', '00000000000', '3@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste4', '00000000000', '4@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste5', '00000000000', '5@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste6', '00000000000', '6@ufac.br'))
        self.tvw.insert('', 'end', values=('Teste7', '00000000000', '7@ufac.br'))
        self.tvw.grid(row=0, column=0)
        self.brl = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.brl.grid(row=0, column=1, sticky='ns')
        self.tvw.configure(yscrollcommand=self.brl.set)
        
        #Botões
        self.frm_botoes = ttk.Frame(self.janela)
        self.frm_botoes.grid(row=1, column=0)
        self.btn_cadastrar = ttk.Button(self.frm_botoes, text='Cadastrar', command=self.cadastrar)
        self.btn_excluir = ttk.Button(self.frm_botoes, text='Excluir', command=self.excluir)
        self.btn_editar = ttk.Button(self.frm_botoes, text='Editar', command=self.editar)
        
        self.btn_cadastrar.grid(row=0, column=0)
        self.btn_excluir.grid(row=0, column=1)
        self.btn_editar.grid(row=0, column=2)
        
    
    def cadastrar(self):
        self.janela.iconify()
        self.top_cadastrar = tk.Toplevel(self.janela)
        self.top_cadastrar.grab_set()
        
        self.lbl_nome = ttk.Label(self.top_cadastrar, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0)
        
        self.lbl_cpf = ttk.Label(self.top_cadastrar, text='CPF: ')
        self.lbl_cpf.grid(row=1, column=0)
        
        self.lbl_email = ttk.Label(self.top_cadastrar, text='E-mail: ')
        self.lbl_email.grid(row=2, column=0)
        
        self.ent_nome = ttk.Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0, column=1)
        
        self.ent_cpf = ttk.Entry(self.top_cadastrar)
        self.ent_cpf.grid(row=1, column=1)
        
        self.ent_email = ttk.Entry(self.top_cadastrar)
        self.ent_email.grid(row=2, column=1)
        
        self.btn_confirmar_cadastro = ttk.Button(self.top_cadastrar, text='Confirmar cadastro', command=self.confirmar_cadastro)
        self.btn_confirmar_cadastro.grid(row=3, column=0)
    
    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        cpf = self.ent_cpf.get()
        email = self.ent_email.get()
        if nome == '' or cpf == '' or email == '':
            messagebox.showwarning('Aviso', 'Todos os campos são obrigatórios.')
        
        else:
            self.tvw.insert('', 'end', values=(nome, cpf, email))
            self.top_cadastrar.destroy()
            self.janela.deiconify()
    
    def excluir(self):
        itens = self.tvw.selection()
        print(itens)
        
        
    
    def editar(self):
        item = self.tvw.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um.')
        

gui = tk.Tk()
principal = Tela(gui)
gui.mainloop()