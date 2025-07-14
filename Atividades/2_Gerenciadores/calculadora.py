import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('132x250')
        self.janela.title('Calculadora Simples')
        self.janela.resizable(False, False)
        self.var_conteudo = tk.StringVar()
        
        self.lbl_conteudo = tk.Label(self.janela, textvariable=self.var_conteudo, fg='white', bg='black', width=18, height=2)
        self.lbl_conteudo.grid(row=0, column=0, columnspan=5)
        
        self.btn7 = tk.Button(text='7', width=3, height=2, fg='white', bg='grey')
        self.btn7.grid(row=1, column=1, padx=1, pady=1)
        
        self.btn8 = tk.Button(text='8', width=3, height=2, fg='white', bg='grey')
        self.btn8.grid(row=1, column=2, padx=1, pady=1)
        
        self.btn9 = tk.Button(text='9', width=3, height=2, fg='white', bg='grey')
        self.btn9.grid(row=1, column=3, padx=1, pady=1)
        
        self.btn_mais = tk.Button(text='+', width=3, height=2, fg='white', bg='grey')
        self.btn_mais.grid(row=1, column=4, padx=1, pady=1)
        
        self.btn4 = tk.Button(text='4', width=3, height=2, fg='white', bg='grey')
        self.btn4.grid(row=2, column=1, padx=1, pady=1)
        
        self.btn5 = tk.Button(text='5', width=3, height=2, fg='white', bg='grey')
        self.btn5.grid(row=2, column=2, padx=1, pady=1)
        
        self.btn6 = tk.Button(text='6', width=3, height=2, fg='white', bg='grey')
        self.btn6.grid(row=2, column=3, padx=1, pady=1)
        
        self.btn_menos = tk.Button(text='-', width=3, height=2, fg='white', bg='grey')
        self.btn_menos.grid(row=2, column=4, padx=1, pady=1)
        
        self.btn1 = tk.Button(text='1', width=3, height=2, fg='white', bg='grey')
        self.btn1.grid(row=3, column=1, padx=1, pady=1)
        
        self.btn2 = tk.Button(text='2', width=3, height=2, fg='white', bg='grey')
        self.btn2.grid(row=3, column=2, padx=1, pady=1)
        
        self.btn3 = tk.Button(text='3', width=3, height=2, fg='white', bg='grey')
        self.btn3.grid(row=3, column=3, padx=1, pady=1)
        
        self.btn_ast = tk.Button(text='*', width=3, height=2, fg='white', bg='grey')
        self.btn_ast.grid(row=3, column=4, padx=1, pady=1)
        
        self.btn0 = tk.Button(text='0', width=3, height=2, fg='white', bg='grey')
        self.btn0.grid(row=4, column=1, padx=1, pady=1)
        
        self.btn0 = tk.Button(text='0', width=3, height=2, fg='white', bg='grey')
        self.btn0.grid(row=4, column=1, padx=1, pady=1)
        
        self.btn_dot = tk.Button(text='.', width=3, height=2, fg='white', bg='grey')
        self.btn_dot.grid(row=4, column=2, padx=1, pady=1)
        
        self.btn_c = tk.Button(text='C', width=3, height=2, fg='white', bg='grey')
        self.btn_c.grid(row=4, column=3, padx=1, pady=1)
        
        self.btn_bar = tk.Button(text='/', width=3, height=2, fg='white', bg='grey')
        self.btn_bar.grid(row=4, column=4, padx=1, pady=1)
        
        self.btn_ingual = tk.Button(text='=', width=17, height=2, fg='white', bg='grey')
        self.btn_ingual.grid(row=5, column=1, padx=1, pady=1, columnspan=5)
    
    

gui = tk.Tk()
Calculadora(gui)
gui.mainloop()