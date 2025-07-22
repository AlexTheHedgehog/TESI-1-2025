import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.img = tk.PhotoImage(file='PngItem_4438467.png')
        self.img = self.img.subsample(3, 3)
        self.lbl= tk.Label(self.janela, image=self.img)
        self.lbl.img = self.img
        self.lbl.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()