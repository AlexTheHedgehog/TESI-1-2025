import tkinter as tk

class Tela:
    def __init__(self, master):
        
        self.janela = master
        self.janela.geometry('200x200')
        self.var_cbt1 = tk.IntVar()
        self.var_cbt2 = tk.IntVar()
        
        self.cbt1 = tk.Checkbutton(self.janela, text='Uauro', variable=self.var_cbt1)
        self.cbt1.pack()
        
        self.cbt2 = tk.Checkbutton(self.janela, text='Aluisio', variable=self.var_cbt2)
        self.cbt2.pack()
        
        self.btn = tk.Button(self.janela, text='Confirmar', command=self.clicou)
        self.btn.pack()
        
        self.lbl = tk.Label(self.janela)
        self.lbl.pack()
        
    
    def clicou(self):
        if self.var_cbt1.get() == self.var_cbt2.get() == 1:
            self.lbl.config(text='Empatou')
        elif self.var_cbt1.get() == 1 != self.var_cbt2.get():
            self.lbl.config(text='Uauro ganhou!')
        else:
            self.lbl.config(text='Aluisio ganhou!')
           
gui = tk.Tk()
Tela(gui)
gui.mainloop()