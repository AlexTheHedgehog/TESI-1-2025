import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        d = {1:'Pudim', 2:'Bolo', 3:'Pavê',  4:'Muçir de Chucolate'}
        
        self.var_rbt = tk.IntVar()
        for chave, valor in d.items():
            rbt = tk.Radiobutton(self.janela, text=valor, value=chave, variable=self.var_rbt, command=self.clicou)
            rbt.pack()
    
    
    def clicou(self):
        valor = self.var_rbt.get()
        match valor:
            case 1:
                messagebox.showinfo('Sobremesa', 'Pudim')
            case 2:
                messagebox.showinfo('Sobremesa', 'Bolo')
            case 3:
                messagebox.showinfo('Sobremesa', 'Pavê')
            case 4:
                messagebox.showinfo('Sobremesa', 'Muçir de Chucolate')
            

gui = tk.Tk()
Tela(gui)
gui.mainloop()
