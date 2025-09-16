#Daniel Gomes Chaves

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('300x300')
        self.janela.title('Qualquer tecla')
        
        self.btn_press = tk.Button(self.janela, text='Pressione qualquer tecla')
        self.btn_press.pack()
        self.btn_press.bind('<Key>', self.tecla)
        self.btn_press.focus()
        
        self.stx = ScrolledText(self.janela, state='disable')
        self.stx.pack()
        
        self.btn_limpar = tk.Button(self.janela, text='Limpar Tela')
        self.btn_limpar.pack()
        self.btn_limpar.bind('<Button-1>', self.limpar)
        
    
    def tecla(self, event):
        char = event.char
        key = event.keysym
        self.stx.config(state='normal')
        if char.isalnum():
            self.stx.insert('end', f'Tecla Normal: {char}\n')
        elif char == '':
            self.stx.insert('end', f'Tecla Especial: {key}\n')
        else:
            self.stx.insert('end', f'Tecla de Pontuação: {char}\n')
        self.stx.config(state='disable')
        
        #if tecla.startswith('Control') or tecla.startswith('Shift') or tecla.startswith('F') or tecla == 'comma' or tecla == 'period' or tecla == 'Print' or tecla in '!.,@#$%¨&*(?/|\)':
        #    self.stx.insert(f'Tecla Especial: {tecla}')
        #else:
        #    self.stx.insert(f'Tecla Normal: {tecla}')
    
    def limpar(self, event):
        self.stx.config(state='normal')
        self.stx.delete(1.0, 'end')
        self.stx.config(state='disable')

gui = tk.Tk()
Tela(gui)
gui.mainloop()