import tkinter as tk

class GerenciadorGrid:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('100x100')
        self.janela.title('Gerenciador Grid')
        
        self.btn1 = tk.Button(self.janela, text='1', width=3)
        self.btn1.grid(row=0, column=1, padx=2, pady=2)
        
        self.btn2 = tk.Button(self.janela, text='2', width=3)
        self.btn2.grid(row=1, column=0, padx=2, pady=2, columnspan=2)
        
        self.btn3 = tk.Button(self.janela, text='3', width=3)
        self.btn3.grid(row=1, column=1, padx=2, pady=2, columnspan=2)
        
        self.btn4 = tk.Button(self.janela, text='4', width=3)
        self.btn4.grid(row=2, column=0, padx=2, pady=2)
        
        self.btn5 = tk.Button(self.janela, text='5', width=3)
        self.btn5.grid(row=2, column=1, padx=2, pady=2)
        
        self.btn6 = tk.Button(self.janela, text='6', width=3)
        self.btn6.grid(row=2, column=2, padx=2, pady=2)
    
    

gui = tk.Tk()
GerenciadorGrid(gui)
gui.mainloop()