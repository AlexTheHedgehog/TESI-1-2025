import tkinter as tk

class MinhaTela():
    def __init__(self, gui):
        self.janela = gui
        #características básicas
        self.janela.title('Já pode desinstalar')
        self.janela.geometry('400x200')
        #self.janela.resizable(width=False, height=False)
        self.janela.maxsize(800, 400)
        #adicionar um componente do tipo Frame
        self.container = tk.Frame(self.janela, width=100, height=100, bg='indigo') #Declaração do frame com o parâmetro pai (janela)
        #Gerenciador de layout
        self.container.pack() #Adiciona o componente na janela
        self.nome = tk.Label(self.container, text='Daniel', anchor='w')
        self.email = tk.Label(self.janela, text='chavesdaniel462@gmail.com')
        self.nome.pack()
        self.email.pack()

gui = tk.Tk()
minhatela = MinhaTela(gui)
gui.mainloop()