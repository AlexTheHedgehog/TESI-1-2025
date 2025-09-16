import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Pressione x')
        self.btn.pack()
        self.btn.bind('<KeyPress-x>', self.press)
        self.btn.bind('<KeyRelease-x>', self.release)
        self.btn.bind('<Button-1>', self.press)
        self.btn.bind('<ButtonRelease-1>', self.release)
        self.btn.bind('<Button-3>', self.press)
    
    def press(self, event):
        self.btn.config(text='Pressionou')
        
    def release(self, event):
        self.btn.config(text='Pressione x')
        
        

app = tk.Tk()
Tela(app)
app.mainloop()