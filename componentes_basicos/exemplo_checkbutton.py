import tkinter as tk

class Tela:
    def __init__(self, master):
        
        self.janela = master
        self.janela.geometry('200x200')
        self.verifica = tk.IntVar()
        self.cbt1 = tk.Checkbutton(self.janela, text='Juiz', variable=self.verifica, command=self.clicou)
        self.cbt2 = tk.Checkbutton(self.janela, text='Acaba pelamor de deus')
        self.cbt1.pack()
        self.cbt2.pack()
        
        
    
    def clicou(self):
        print(self.verifica.get())
        
           
gui = tk.Tk()
Tela(gui)
gui.mainloop()