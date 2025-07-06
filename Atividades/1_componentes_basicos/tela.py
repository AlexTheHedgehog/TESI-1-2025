import tkinter as tk
from datetime import date
import subprocess
import sys


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Atividade 1')
        self.janela.geometry('400x400')
        
        self.var_nome = tk.StringVar()
        self.var_dia = tk.IntVar()
        self.var_mes = tk.IntVar()
        self.var_ano = tk.IntVar()
        self.var_email = tk.IntVar()
        self.var_tipo1 = tk.IntVar()
        self.var_tipo2 = tk.IntVar()
        self.var_tipo3 = tk.IntVar()
        
        self.mnu_barra = tk.Menu(self.janela)
        self.mnu_item_menu = tk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_barra.add_cascade(label='Interfaces', menu=self.mnu_item_menu)
        self.mnu_item_menu.add_command(label='Label', command=self.trocar_label)
        self.mnu_item_menu.add_command(label='Entry', command=self.trocar_entry)
        self.mnu_item_menu.add_command(label='Button', command=self.trocar_button)
        self.mnu_item_menu.add_command(label='CheckButton', command=self.trocar_checkbutton)
        self.mnu_item_menu.add_command(label='RadioButton', command=self.trocar_radiobutton)
        self.mnu_item_menu.add_command(label='Text e Scrollbar', command=self.trocar_text_scrollbar)
        self.mnu_item_menu.add_command(label='Menu', command=self.trocar_menu)
        self.mnu_item_menu.add_command(label='Fechar', command=self.janela.destroy)
        
        self.cnt_nome = tk.Frame(self.janela, width=125, height=20)
        self.cnt_nome.pack()
        
        self.lbl_nome = tk.Label(self.cnt_nome, text='Nome:')
        self.lbl_nome.pack(side='left')
        
        self.ent_nome = tk.Entry(self.cnt_nome, width = 32, textvariable=self.var_nome)
        self.ent_nome.pack(side='left')
        
        self.cnt_data = tk.Frame(self.janela, width=125, height=20)
        self.cnt_data.pack()
        
        self.lbl_data = tk.Label(self.cnt_data, text='Data de nascimento:')
        self.lbl_data.pack(side='left')
        
        self.spn_dia = tk.Spinbox(self.cnt_data, from_=1, to=31, width=5, textvariable=self.var_dia)
        self.spn_dia.pack(side='left')
        
        self.spn_mes = tk.Spinbox(self.cnt_data, from_=1, to=12, width=5, textvariable=self.var_mes)
        self.spn_mes.pack(side='left')
        
        self.spn_ano = tk.Spinbox(self.cnt_data, from_=1, to=2025, width=5, textvariable=self.var_ano)
        self.spn_ano.pack(side='left')
        
        self.cbt_email = tk.Checkbutton(self.janela, text='Desejo receber atualizações pelo meu endereço de E-mail.', command=self.atv_email, variable=self.var_email)
        self.cbt_email.pack()
        
        self.cnt_tipos_email = tk.Frame(self.janela)
        self.cnt_tipos_email.pack()
        
        self.cbt_tipo1 = tk.Checkbutton(self.cnt_tipos_email, text='Inteligência Artificial', state='disabled', variable=self.var_tipo1)
        self.cbt_tipo2 = tk.Checkbutton(self.cnt_tipos_email, text='Meio ambiente e tecnologia', state='disabled', variable=self.var_tipo2)
        self.cbt_tipo3 = tk.Checkbutton(self.cnt_tipos_email, text='Videogames', state='disabled', variable=self.var_tipo3)
        self.cbt_tipo1.pack()
        self.cbt_tipo2.pack()
        self.cbt_tipo3.pack()
        
        self.btn_enviar = tk.Button(self.janela, text='Enviar', command=self.enviar)
        self.btn_enviar.pack()
        
        self.lbl_resp = tk.Label(self.janela)
        self.lbl_resp.pack()
        
        self.lbl_conteudo = tk.Label(self.janela)
        self.lbl_conteudo.pack()
        
        self.janela.config(menu=self.mnu_barra)
    
    def trocar(self, txt):
        subprocess.run([sys.executable, txt], check=True)
    
    def trocar_label(self):
        self.trocar('../../componentes_basicos/exemplo_label.py')
    
    def trocar_entry(self):
        self.trocar('../../componentes_basicos/exemplo_entry.py')
    
    def trocar_button(self):
        self.trocar('../../componentes_basicos/exemplo_button.py')
    
    def trocar_checkbutton(self):
        self.trocar('../../componentes_basicos/exemplo_checkbutton.py')
    
    def trocar_radiobutton(self):
        self.trocar('../../componentes_basicos/exemplo_radiobutton.py')
    
    def trocar_text_scrollbar(self):
        self.trocar('../../componentes_basicos/exemplo_text_scrollbar.py')
    
    def trocar_menu(self):
        self.trocar('../../componentes_basicos/exemplo_menu.py')
    
    def atv_email(self):
        if self.var_email.get() == 1:
            self.cbt_tipo1.config(state='normal')
            self.cbt_tipo2.config(state='normal')
            self.cbt_tipo3.config(state='normal')
        else:
            self.cbt_tipo1.config(state='disabled')
            self.cbt_tipo2.config(state='disabled')
            self.cbt_tipo3.config(state='disabled')
     
    def enviar(self):
        resp = ''
        
        if self.var_tipo1.get() == 1:
            resp += 'insira conteúdo sobre inteligência artificial aqui.\n'
        if self.var_tipo2.get() == 1:
            resp += 'insira conteúdo sobre meio ambiente e tecnologia aqui.\n'
        if self.var_tipo3.get() == 1:
            resp += 'insira conteúdo sobre videogames aqui.'
        
        self.lbl_conteudo.config(text=resp)
            
        
        ano, mes, dia = str(date.today()).split('-')
        idade_anos = int(ano) - self.var_ano.get()
        idade_meses = int(mes) - self.var_mes.get()
        idade_dias = int(dia) - self.var_dia.get()
        
        if idade_dias < 0:
            idade_dias += 30
            idade_meses -= 1
        
        if idade_meses < 0:
            idade_meses += 12
            idade_anos -= 1
        
        idade_somente_dias = idade_dias + idade_meses * 30 + idade_anos * 365
        #print(f'Nome: {self.var_nome.get()}\nIdade: {idade_anos} anos, {idade_meses} meses e {idade_dias} dias ou {idade_somente_dias} dias.')
        self.lbl_resp.config(text=f'Nome: {self.var_nome.get()}\nIdade: {idade_anos} anos, {idade_meses} meses e {idade_dias} dias ou {idade_somente_dias} dias.')

gui = tk.Tk()
Tela(gui)
gui.mainloop()