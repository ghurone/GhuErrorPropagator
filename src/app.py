from ghuerror import *

import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

fonte_titlo = "-family {Comic Sans MS} -size 26 -weight bold"
fonte_texto = "-family {Comic Sans MS} -size 14"
versao = '1.0.0'

class MainWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()

        window_height = 450
        window_width = 400
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        # Configuraçōes da Janela
        self.window.title('GhuErrorPropagator')
        self.window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.window.resizable(False, False)
        self.window.configure(background="#ffffff")

        # Logo
        self.titulo = tk.Label(self.window)
        self.titulo.configure(background="#ffffff")
        self.titulo.configure(font=fonte_titlo)
        self.titulo.configure(text='''GhuErrorPropagator''')
        self.titulo.place(x=0, y=0, height=50, width=400)
        
        # Texto Input
        self.tinput = tk.Label(self.window)
        self.tinput.configure(background="#ffffff")
        self.tinput.configure(anchor='w')
        self.tinput.configure(font=fonte_texto)
        self.tinput.configure(text="Função: ")
        self.tinput.place(x=10, y=60, height=25, width=380)
        
        # Input
        self.input = tk.Entry(self.window)
        self.input.configure(background="#ffffff")
        self.input.place(x=10, y=90, height=30, width=380)
        
        # Texto variaveis
        self.tvar = tk.Label(self.window)
        self.tvar.configure(background="#ffffff")
        self.tvar.configure(anchor='w')
        self.tvar.configure(font=fonte_texto)
        self.tvar.configure(text="Variáveis: ")
        self.tvar.place(x=10, y=130, height=20, width=380)
        
        # Variaveis
        self.var = ttk.Treeview(self.window, column=("c1", "c2", "c3"), show='headings')
        self.var.column("# 1", anchor='center', width=150, stretch=True)
        self.var.heading("# 1", text="Nome")
        self.var.column("# 2", anchor='w', width=114, stretch=True)
        self.var.heading("# 2", text="Valor")
        self.var.column("# 3", anchor='w', width=115, stretch=True)
        self.var.heading("# 3", text="Incerteza")
        self.var.place(x=10, y=160, height=200, width=380)
        
        # botao adicionar variavel
        self.b_add = tk.Button(self.window)
        self.b_add.configure(background="#ff5454")
        self.b_add.configure(activebackground="#ffffff")
        self.b_add.configure(activeforeground="#ff5454")
        self.b_add.configure(borderwidth=0)
        self.b_add.configure(text="Adicionar")
        self.b_add.configure(font=fonte_texto)
        self.b_add.configure(cursor='hand2')
        self.b_add.configure(command=self.adicionar)
        self.b_add.place(x=10, y=370, height=30, width=100)
        
        # botao editar variavel
        self.b_edit = tk.Button(self.window)
        self.b_edit.configure(background="#b28cff")
        self.b_edit.configure(activebackground="#ffffff")
        self.b_edit.configure(activeforeground="#b28cff")
        self.b_edit.configure(borderwidth=0)
        self.b_edit.configure(text="Editar")
        self.b_edit.configure(font=fonte_texto)
        self.b_edit.configure(cursor='hand2')
        self.b_edit.configure(command=self.editar)
        self.b_edit.place(x=150, y=370, height=30, width=100)

        # botao deletar variavel
        self.b_del = tk.Button(self.window)
        self.b_del.configure(background="#54a4ff")
        self.b_del.configure(activebackground="#ffffff")
        self.b_del.configure(activeforeground="#54a4ff")
        self.b_del.configure(borderwidth=0)
        self.b_del.configure(text="Deletar")
        self.b_del.configure(font=fonte_texto)
        self.b_del.configure(cursor='hand2')
        self.b_del.configure(command=self.deletar)
        self.b_del.place(x=290, y=370, height=30, width=100)
        
        # Botao propagar
        self.botao = tk.Button(self.window)
        self.botao.configure(background="#54ff73")
        self.botao.configure(activebackground="#ffffff")
        self.botao.configure(activeforeground="#54ff73")
        self.botao.configure(borderwidth=0)
        self.botao.configure(text="PROPAGAR!!")
        self.botao.configure(font=fonte_texto)
        self.botao.configure(cursor='hand2')
        self.botao.configure(command=self.propagar)
        self.botao.place(x=135, y=410, height=30, width=130)
        
        # Label versão
        self.lversao = tk.Button(self.window)
        self.lversao.configure(background="#ffffff")
        self.lversao.configure(activebackground="#ffffff")
        self.lversao.configure(activeforeground="#000000")
        self.lversao.configure(borderwidth=0)
        self.lversao.configure(text=f'v {versao}')
        self.lversao.configure(font="-family {Comic Sans MS} -size 10")
        self.lversao.configure(cursor='heart')
        self.lversao.configure(relief='raised')
        self.lversao.configure(command=self.abrir_navegador)
        self.lversao.place(x=350, y=420, height=30)
        
        self.jans = []
        self.window.protocol('WM_DELETE_WINDOW', self.fechar)
    
    @staticmethod
    def abrir_navegador():
        webbrowser.open('https://www.github.com/ghurone/GhuErrorPropagator')
        
    def fechar(self):
        for jan in self.jans:
            jan.window.destroy()
        
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

    def adicionar(self):
        jan = AddWindow(self)
        self.jans.append(jan)
        jan.run()

    def editar(self):
        s_item = self.var.selection()
        if len(s_item) == 1:
            item = s_item[0]
            
            jan = EditWindow(self, item)
            self.jans.append(jan)
            jan.run()

        else:
            showerror("ERRO", "Selecione somente uma variável.")
        
    def deletar(self):
        selected_items = self.var.selection()        
        for selected_item in selected_items:          
            self.var.delete(selected_item)
    
    def ja_existe(self, nome):
        for id in self.var.get_children():
            if nome in self.var.item(id)["values"]:
                return True
        return False
    
    def propagar(self):
        func = self.input.get()
        val = {}
        for id in self.var.get_children():
            nome, valor, inc = self.var.item(id)["values"]
            val[nome] = (N(valor), N(inc))

        if val:
            try:
                ghu = GhuErrorPropagator(func, val)
                ghu.resultado_final()
                
                jan = PropWindow(ghu, self)
                self.jans.append(jan)
                
                jan.run()
                
            except Exception as e:
                showerror('ERRO', 'Verifique sua função e suas variáveis')
        else:
            showerror('ERRO', 'Insira variáveis para sua função')
      
  
class AddWindow:
    def __init__(self, main: object) -> None:
        self.main = main
        self.window = tk.Tk()
                
        # Configuraçōes da Janela
        self.window.title('Adicionar variável')
        self.window.geometry('300x150')
        self.window.resizable(False, False)
        self.window.configure(background="#ffffff")
        
        # label nome
        self.nome = tk.Label(self.window)
        self.nome.configure(background="#ffffff")
        self.nome.configure(anchor='w')
        self.nome.configure(font=fonte_texto)
        self.nome.configure(text="Nome:")
        self.nome.place(x=10, y=10, height=20, width=280)
        
        # input nome
        self.inome = tk.Entry(self.window)
        self.inome.configure(background="#ffffff")
        self.inome.place(x=75, y=10, height=25, width=215)
        
        # label valor
        self.valor = tk.Label(self.window)
        self.valor.configure(background="#ffffff")
        self.valor.configure(anchor='w')
        self.valor.configure(font=fonte_texto)
        self.valor.configure(text="Valor:")
        self.valor.place(x=10, y=40, height=20, width=280)
        
        # input valor
        self.ivalor = tk.Entry(self.window)
        self.ivalor.configure(background="#ffffff")
        self.ivalor.place(x=70, y=40, height=25, width=220)
        
        # label incerteza
        self.inc = tk.Label(self.window)
        self.inc.configure(background="#ffffff")
        self.inc.configure(anchor='w')
        self.inc.configure(font=fonte_texto)
        self.inc.configure(text="Incerteza:")
        self.inc.place(x=10, y=70, height=20, width=280)
        
        # input incerteza
        self.iinc = tk.Entry(self.window)
        self.iinc.configure(background="#ffffff")
        self.iinc.place(x=115, y=70, height=25, width=175)
        
        # botao enviar
        self.botao = tk.Button(self.window)
        self.botao.configure(background="#03fcb1")
        self.botao.configure(activebackground="#ffffff")
        self.botao.configure(activeforeground="#03fcb1")
        self.botao.configure(borderwidth=0)
        self.botao.configure(text="Adicionar!")
        self.botao.configure(font=fonte_texto)
        self.botao.configure(cursor='hand2')
        self.botao.configure(command=self.enviar)
        self.botao.place(x=90, y=110, height=30, width=120)
        
        self.window.protocol('WM_DELETE_WINDOW', self.fechar)
    
    def fechar(self):
        del self.main.jans[self.main.jans.index(self)]
        self.window.destroy()
        
    def enviar(self):
        nome = self.inome.get()
        valor = self.ivalor.get()
        inc = self.iinc.get()
        
        if not N(nome).is_number and N(valor).is_number and N(inc).is_number:
            if not self.main.ja_existe(nome):
                self.main.var.insert('', index='end', text='', values=(nome, valor, inc))
            else:
                showerror('ERRO', 'Essa variável já existe!')
            self.fechar()
        else:
            showerror('ERRO', 'Digite os campos corretamente!')
        
    def run(self):
        self.window.mainloop()


class EditWindow:
    def __init__(self, main: object, item) -> None:
        self.main = main
        self.window = tk.Tk()
                
        # Configuraçōes da Janela
        self.window.title('Editar variável')
        self.window.geometry('300x150')
        self.window.resizable(False, False)
        self.window.configure(background="#ffffff")
        
        # label nome
        self.nome = tk.Label(self.window)
        self.nome.configure(background="#ffffff")
        self.nome.configure(anchor='w')
        self.nome.configure(font=fonte_texto)
        self.nome.configure(text="Nome:")
        self.nome.place(x=10, y=10, height=20, width=280)
        
        # input nome
        self.inome = tk.Entry(self.window)
        self.inome.configure(background="#ffffff")
        self.inome.place(x=75, y=10, height=25, width=215)
        
        # label valor
        self.valor = tk.Label(self.window)
        self.valor.configure(background="#ffffff")
        self.valor.configure(anchor='w')
        self.valor.configure(font=fonte_texto)
        self.valor.configure(text="Valor:")
        self.valor.place(x=10, y=40, height=20, width=280)
        
        # input valor
        self.ivalor = tk.Entry(self.window)
        self.ivalor.configure(background="#ffffff")
        self.ivalor.place(x=70, y=40, height=25, width=220)
        
        # label incerteza
        self.inc = tk.Label(self.window)
        self.inc.configure(background="#ffffff")
        self.inc.configure(anchor='w')
        self.inc.configure(font=fonte_texto)
        self.inc.configure(text="Incerteza:")
        self.inc.place(x=10, y=70, height=20, width=280)
        
        # input incerteza
        self.iinc = tk.Entry(self.window)
        self.iinc.configure(background="#ffffff")
        self.iinc.place(x=115, y=70, height=25, width=175)
        
        # botao enviar
        self.botao = tk.Button(self.window)
        self.botao.configure(background="#03fcb1")
        self.botao.configure(activebackground="#ffffff")
        self.botao.configure(activeforeground="#03fcb1")
        self.botao.configure(borderwidth=0)
        self.botao.configure(text="Editar!")
        self.botao.configure(font=fonte_texto)
        self.botao.configure(cursor='hand2')
        self.botao.configure(command=self.enviar)
        self.botao.place(x=90, y=110, height=30, width=120)
        
        self.item = item
        nome, valor, inc = self.main.var.item(item)["values"]
        self.nome = nome        
        
        self.iinc.insert(0, inc)
        self.inome.insert(0, nome)
        self.ivalor.insert(0, valor)
        
        self.window.protocol('WM_DELETE_WINDOW', self.fechar)
    
    def fechar(self):
        del self.main.jans[self.main.jans.index(self)]
        self.window.destroy()
        
    def enviar(self):
        nome = self.inome.get()
        valor = self.ivalor.get()
        inc = self.iinc.get()
        
        if not N(nome).is_number and N(valor).is_number and N(inc).is_number:
            if not self.main.ja_existe(nome) or nome == self.nome:
                self.main.var.item(self.item, text="", values=(nome, valor, inc))
            else:
                showerror('ERRO', 'Essa variável já existe!')
            
            self.fechar()
        else:
            showerror('ERRO', 'Digite os campos corretamente!')
        
    def run(self):
        self.window.mainloop()


class PropWindow:
    def __init__(self, ghu, main: MainWindow) -> None:
        self.ghu = ghu
        self.main = main
        self.window = tk.Tk()
                
        # Configuraçōes da Janela
        self.window.title('Propagação - GhuErrorPropagator')
        self.window.geometry('500x380')
        self.window.resizable(False, False)
        self.window.configure(background="#ffffff")

        # label funcao
        self.tfunc = tk.Label(self.window)
        self.tfunc.configure(background="#ffffff")
        self.tfunc.configure(anchor='w')
        self.tfunc.configure(font=fonte_texto)
        self.tfunc.configure(text="Função inserida:")
        self.tfunc.place(x=10, y=10, height=20, width=280)
        
        self.label = tk.Label(self.window)
        self.label.configure(background='#ffffff')
        self.label.configure(borderwidth=0)
        self.label.place(x=10, y=45)
        
        functext = "$"+ghu.get_latex_func()+"$"
        
        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(5, 1), dpi=100)
        wx = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=self.label)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Set the visibility of the Canvas figure
        wx.get_xaxis().set_visible(False)
        wx.get_yaxis().set_visible(False)
        wx.spines['bottom'].set_color('white')
        wx.spines['top'].set_color('white')
        wx.spines['left'].set_color('white')
        wx.spines['right'].set_color('white')
        wx.text(0,0.5, functext, fontsize=16)
        canvas.draw()
        
        self.tsigma = tk.Label(self.window)
        self.tsigma.configure(background="#ffffff")
        self.tsigma.configure(anchor='w')
        self.tsigma.configure(font=fonte_texto)
        self.tsigma.configure(text="Função sigma:")
        self.tsigma.place(x=10, y=130, height=20, width=280)
        
        self.label2 = tk.Label(self.window)
        self.label2.configure(background='#ffffff')
        self.label2.configure(borderwidth=0)
        self.label2.place(x=10, y=190)
        
        sigmatext = "$"+ghu.get_latex_sigma()+"$"
        
        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(5, 1), dpi=100)
        wx = fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(fig, master=self.label2)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Set the visibility of the Canvas figure
        wx.get_xaxis().set_visible(False)
        wx.get_yaxis().set_visible(False)
        wx.spines['bottom'].set_color('white')
        wx.spines['top'].set_color('white')
        wx.spines['left'].set_color('white')
        wx.spines['right'].set_color('white')
        wx.text(0,0.5, sigmatext, fontsize=16)
        canvas.draw()
        
        self.tvalor = tk.Label(self.window)
        self.tvalor.configure(background="#ffffff")
        self.tvalor.configure(anchor='w')
        self.tvalor.configure(font=fonte_texto)
        self.tvalor.configure(text=f"Valor: {ghu.valor}")
        self.tvalor.place(x=10,y=270)
        
        self.tresult = tk.Label(self.window)
        self.tresult.configure(background="#ffffff")
        self.tresult.configure(anchor='w')
        self.tresult.configure(font=fonte_texto)
        self.tresult.configure(text=f"Incerteza: {ghu.resultado}")
        self.tresult.place(x=10,y=300)
        
        self.prin = tk.Label(self.window)
        self.prin.configure(background="#ffffff")
        self.prin.configure(borderwidth=1)
        self.prin.configure(relief="solid")
        self.prin.configure(anchor='center')
        self.prin.configure(font=fonte_texto)
        self.prin.configure(text=f'{ghu.resultado_final()} ')
        self.prin.place(x=10,y=340, width=480)
        
        self.window.protocol('WM_DELETE_WINDOW', self.fechar)
    
    def fechar(self):
        del self.main.jans[self.main.jans.index(self)]
        self.window.destroy()
        
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()
