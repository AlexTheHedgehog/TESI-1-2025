import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x400')
        
        self.var_mod = tk.StringVar()
        self.var_c = tk.IntVar()
        self.var_java = tk.IntVar()
        self.var_python = tk.IntVar()
        
        self.lbl_nome = tk.Label(self.janela, text='Nome:')
        self.lbl_nome.grid(row=0, column=0)
        self.lbl_email = tk.Label(self.janela, text='Email:')
        self.lbl_email.grid(row=1, column=0)
        
        self.ent_nome = tk.Entry(self.janela)
        self.ent_nome.grid(row=0, column=1, columnspan=2)
        self.ent_email = tk.Entry(self.janela)
        self.ent_email.grid(row=1, column=1, columnspan=2)
        
        self.frm_curso = tk.LabelFrame(self.janela, text='Curso(s):')
        self.frm_curso.grid(row=2, column=1)
        
        self.cbt_c = tk.Checkbutton(self.frm_curso, text='C++')
        self.cbt_c.pack(anchor='w')
        self.cbt_java = tk.Checkbutton(self.frm_curso, text='Java')
        self.cbt_java.pack(anchor='w')
        self.cbt_python = tk.Checkbutton(self.frm_curso, text='Python')
        self.cbt_python.pack(anchor='w')
        
        self.frm_mod = tk.LabelFrame(self.janela, text='Modalidade:')
        self.frm_mod.grid(row=2, column=2, sticky='nw')
        
        self.rdb_ead = tk.Radiobutton(self.frm_mod, text='EAD')
        self.rdb_ead.pack(anchor='w')
        self.rdb_pres = tk.Radiobutton(self.frm_mod, text='Presencial')
        self.rdb_pres.pack(anchor='w')
        
        self.btn_enviar = tk.Button(self.janela, text='Enviar', width=27)
        self.btn_enviar.grid(row=3, column=0, columnspan=3)

gui = tk.Tk()
Tela(gui)
gui.mainloop()