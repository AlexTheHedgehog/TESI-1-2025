import tkinter as tk

class PackSimples:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x200')
        self.janela.title('Pack Simples')
        
        self.lbl_topo = tk.Label(self.janela, text='TOPO', fg='black', bg='yellow', height=4)
        self.lbl_topo.pack(fill='x')
        
        self.cnt_esqdir = tk.Frame(self.janela, height=2)
        self.cnt_esqdir.pack(fill='x')
        
        self.lbl_esquerda = tk.Label(self.cnt_esqdir, text='ESQUERDA', fg='black', bg='red', height=2)
        self.lbl_esquerda.pack(side='left', expand=True, anchor='nw', fill='x')
        
        self.lbl_direita = tk.Label(self.cnt_esqdir, text='DIREITA', fg='black', bg='green', height=2)
        self.lbl_direita.pack(side='left', expand=True, anchor='ne', fill='x')
        
        self.lbl_rodape = tk.Label(self.janela, text='RODAPÉ', fg='black', bg='cyan', height=4, )
        self.lbl_rodape.pack(expand=True, fill='both', side='bottom')    

gui = tk.Tk()
PackSimples(gui)
gui.mainloop()