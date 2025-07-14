import tkinter as tk

class GerenciadorPack:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry('220x180')
        self.janela.title('Gerenciador Pack')
        
        self.lbl_red = tk.Label(self.janela, text='RED', fg='white', bg='red')
        self.lbl_red.pack(fill='x')
        
        self.lbl_green = tk.Label(self.janela, text='GREEN', fg='white', bg='green')
        self.lbl_green.pack(fill='x')
        
        self.lbl_blue = tk.Label(self.janela, text='BLUE', fg='white', bg='blue')
        self.lbl_blue.pack(fill='x')
        
        self.lbl_gray1 = tk.Label(self.janela, text='GRAY', fg='white', bg='gray')
        self.lbl_gray1.pack(fill='y', anchor='w', side='left')
        
        self.lbl_gray2 = tk.Label(self.janela, text='GRAY', fg='white', bg='gray')
        self.lbl_gray2.pack(fill='y', anchor='e', side='right')
        
        self.cnt_3cores = tk.Frame(self.janela)
        self.cnt_3cores.pack()
        
        self.lbl_cyan = tk.Label(self.cnt_3cores, text='CYAN', fg='black', bg='cyan')
        self.lbl_cyan.pack(side='left', anchor='n')
        
        self.lbl_magenta = tk.Label(self.cnt_3cores, text='MAGENTA', fg='black', bg='magenta')
        self.lbl_magenta.pack(side='left', anchor='n')
        
        self.lbl_yellow = tk.Label(self.cnt_3cores, text='YELLOW', fg='black', bg='yellow')
        self.lbl_yellow.pack(side='left', anchor='n')
        
        self.lbl_black = tk.Label(self.janela, text='BLACK', fg='white', bg='black', height=20)
        self.lbl_black.pack(fill='both')
    
    

gui = tk.Tk()
GerenciadorPack(gui)
gui.mainloop()