import tkinter as tk

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('200x200')
        self.btn = tk.Button(self.janela, text='Abrir Toplevel', command=self.abrir)
        self.btn.pack()
    
    def abrir(self):
        #self.janela.withdraw()
        self.janela.iconify()
        segunda_janela = tk.Toplevel(self.janela)
        segunda_janela.grab_set()
        
        def fechar():
            segunda_janela.destroy()
            self.janela.deiconify()
        
        btn_fechar = tk.Button(segunda_janela, text='Fechar', command=fechar)
        btn_fechar.pack()

gui = tk.Tk()
Tela(gui)
gui.mainloop()