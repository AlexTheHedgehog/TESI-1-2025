import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.lbl = ttk.Label(self.janela, text='Bem vindo ao ttkbootstrap!')
        self.lbl.pack()
        self.ent = ttk.Meter(self.janela, bootstyle='danger', subtext='Meter', interactive=True, amountused=23).pack()
        self.bnt = ttk.Button(self.janela, text='Enviar', bootstyle='light').pack()

app = ttk.Window(themename='vapor')#tk.Tk()
Tela(app)
app.mainloop()