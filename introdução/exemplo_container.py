import tkinter as tk

janela = tk.Tk()
#características básicas
janela.title('Besteira besteirinha')
janela.geometry('400x200')
#janela.resizable(width=False, height=False)
janela.maxsize(800, 400)
#adicionar um componente do tipo Frame
container = tk.Frame(janela, width=100, height=100, bg='indigo') #Declaração do frame com o parâmetro pai (janela)
#Gerenciador de layout
container.pack() #Adiciona o componente na janela


janela.mainloop()