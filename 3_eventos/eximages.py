import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

class Tela:
    def __init__(self, master):
        self.janela = master
        
        self.btn_abrir = tk.Button(self.janela, text='Abrir arquivo...')
        self.btn_abrir.pack()
        self.btn_abrir.bind('<Button-1>', self.abrir)
        
        self.lbl_imagem = tk.Label(self.janela)
        self.lbl_imagem.pack()

    def salvar(self, event):
        pass
        
            
    def abrir(self, event):
        #caminho = fd.askopenfilename()
        #print(caminho)
        
        #with open(caminho, 'r') as arquivo:
        #    for linha in arquivo:
        #        self.stx.insert('end', linha)
        
        caminho_imagem = fd.askopenfilename()
        imagem = Image.open(caminho_imagem)
        imagem_tk = ImageTk.PhotoImage(imagem)
        self.lbl_imagem.config(image = imagem_tk)
        self.lbl_imagem.image = imagem_tk
        
        


app = tk.Tk()
Tela(app)
app.mainloop()