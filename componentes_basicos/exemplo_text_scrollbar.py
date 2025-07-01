import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('400x90')
        self.scb = tk.Scrollbar(self.janela)
        self.scb.pack(side=tk.RIGHT, fill='y')
        self.txt = tk.Text(self.janela, height=5, yscrollcommand=self.scb.set)
        linha = 'a\nb\nc\nd\nf\ng\nh\ni\nj\nk'
        self.txt.insert(tk.END, linha)
        self.txt.pack(side='left')
        self.scb.config(command=self.txt.yview)
        self.stx = ScrolledText(self.janela)
        self.stx.pack(side='right')

gui = tk.Tk()
Tela(gui)
gui.mainloop()