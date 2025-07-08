import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        lbl1 = tk.Label(self.janela, text='Label 1', fg='white', bg='red')
        lbl1.pack(fill='x', expand=True, side='left')
        lbl2 = tk.Label(self.janela, text='Label 2', fg='black', bg='indigo')
        lbl2.pack(fill='x', expand=True, side='left')

gui = tk.Tk()
Tela(gui)
gui.mainloop()