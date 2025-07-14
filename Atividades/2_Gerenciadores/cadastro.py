import tkinter as tk
from tkinter import messagebox

class Cadastro:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x200')
        self.janela.title('Cadastro de Aluno')
        
        self.var_nome = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_cpp = tk.IntVar()
        self.var_java = tk.IntVar()
        self.var_python = tk.IntVar()
        self.var_mod = tk.IntVar()
        
        self.lbl_nome = tk.Label(self.janela, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        
        self.lbl_email = tk.Label(self.janela, text='E-mail:')
        self.lbl_email.grid(row=1, column=0)
        
        self.ent_nome = tk.Entry(self.janela, width=40, textvariable=self.var_nome)
        self.ent_nome.grid(row=0, column=1, columnspan=2)
        
        self.ent_email = tk.Entry(self.janela, width=40, textvariable=self.var_email)
        self.ent_email.grid(row=1, column=1, columnspan=2)
        
        self.lbl_cursos = tk.Label(self.janela, text='Curso(s):')
        self.lbl_cursos.grid(row=2, column=1)
        
        self.lbl_modalidade = tk.Label(self.janela, text='Modalidade:')
        self.lbl_modalidade.grid(row=2, column=2)
        
        self.cbn_cpp = tk.Checkbutton(self.janela, text='C++', variable=self.var_cpp)
        self.cbn_cpp.grid(row=3, column=1)
        
        self.cbn_java = tk.Checkbutton(self.janela, text='Java', variable=self.var_java)
        self.cbn_java.grid(row=4, column=1)
        
        self.cbn_python = tk.Checkbutton(self.janela, text='Python', variable=self.var_python)
        self.cbn_python.grid(row=5, column=1)
        
        self.rbn_ead = tk.Radiobutton(self.janela, text='EAD', variable=self.var_mod, value=1)
        self.rbn_ead.grid(row=3, column=2)
        
        self.rbn_presencial = tk.Radiobutton(self.janela, text='Presencial', variable=self.var_mod, value=2)
        self.rbn_presencial.grid(row=4, column=2)
        
        self.btn_exibir = tk.Button(self.janela, text='Exibir Dados', width=41, height=3, command=self.exibir)
        self.btn_exibir.grid(row=6, column=0, columnspan=3)
        
    def exibir(self):
        resp = f'Nome: {self.var_nome.get()}\nE-mail: {self.var_email.get()}'
        cursos = []
        
        if self.var_cpp.get() == 1:
            cursos.append('C++')
        if self.var_java.get() == 1:
            cursos.append('Java')
        if self.var_python.get() == 1:
            cursos.append('Python')
        
        if len(cursos) > 0:
            resp += f'\nCurso(s): {cursos}'
        else:
            resp += f'\nNenhum curso foi selecionado.'
        
        if self.var_mod.get() == 1:
            resp += f'\nModalidade: EAD'
        else:
            resp += f'\nModalidade: Presencial'
        
        
        messagebox.showinfo('Dados', resp)
        
        #print(resp)
        
    

gui = tk.Tk()
Cadastro(gui)
gui.mainloop()