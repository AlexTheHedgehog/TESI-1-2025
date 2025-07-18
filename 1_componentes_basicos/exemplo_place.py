import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('500x500')
        lbl1 = tk.Label(self.janela, text='Testando', fg='blue', bg='green')
        lbl2 = tk.Label(self.janela, text='Ebaaaaaaaaaa', fg='green', bg= 'blue')
        lbl1.place(x=250, y=250, anchor='center')
        lbl2.place(x=400, y=10)
        

gui = tk.Tk()
Tela(gui)
gui.mainloop()
        