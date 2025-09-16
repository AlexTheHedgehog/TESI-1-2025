import tkinter as tk
from tkinter import messagebox

class Tela:
    def __init__(self, master):
        self.janela = master
        self.btn = tk.Button(self.janela, text='Clicar')
        self.btn.pack()
        self.btn.bind('<Key>', self.clicou)
        self.btn.bind('<Control_L><v>', self.mensagem)
    
    def clicou(self, event):
        print(f'Pressionou {event.char}{event.keysym}')
        
    def mensagem(self, event):
        messagebox.showinfo('Mensagem', f'{event.keysym}')
        
        

app = tk.Tk()
Tela(app)
app.mainloop()