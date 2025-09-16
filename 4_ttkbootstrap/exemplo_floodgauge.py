import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkbootstrap!')
        self.lbl.pack()
        self.flo = ttk.Floodgauge(self.janela, mode='determinate', value=0, maximum=100, mask='Transferindo {}%')
        self.flo.pack()
        self.btn_start = ttk.Button(self.janela, text='Iniciar', bootstyle='light')
        self.btn_start.pack()
        self.btn_start.bind('<Button-1>', self.iniciar)
        self.btn_stop = ttk.Button(self.janela, text='Parar')
        self.btn_stop.pack()
        self.btn_stop.bind('<Button-1>', self.parar)
    
    def iniciar(self, event):
        self.flo.start()
    
    def parar(self, event):
        self.flo.stop()

app = ttk.Window(themename='vapor')#tk.Tk()
Tela(app)
app.mainloop()