import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Abrir', )

gui = tk.Tk()
Tela(gui)
gui.mainloop()