import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.lbl_login = tk.Label(self.janela, text='Login:')
        self.ent_login = tk.Entry(self.janela, width=20)
        self.lbl_senha = tk.Label(self.janela, text='Senha:')
        self.ent_senha = tk.Entry(self.janela, width=20, show='*')
        
        self.lbl_login.pack()
        self.ent_login.pack()
        self.lbl_senha.pack()
        self.ent_senha.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()