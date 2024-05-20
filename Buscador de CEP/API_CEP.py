import requests
from tkinter import *
from tkinter import messagebox

root = Tk()

class Funcs():
    def limpar_texto_entry(self):
        try:
            texto_cep = self.entry_cep.get()
            texto_cep = texto_cep.replace('-','')
            int(texto_cep)
            if len(texto_cep) == 8:
                print('texto CEP limpo: ', texto_cep)
                return texto_cep
            elif len(texto_cep) > 8:
                messagebox.showerror("Erro dado", "Tamanho do número CEP maior que o permitido!")
            else:
                messagebox.showerror("Erro dado", "Tamanho do número CEP menor que o permitido!")
        except:
            messagebox.showerror("Erro dado", "Você inseriu um valor incorreto!")
    def buscar_cep(self):
        cep_para_busca = self.limpar_texto_entry()
        try:
            link = f'https://viacep.com.br/ws/{cep_para_busca}/json'
            requisicao = requests.get(link)
            dict_cep = requisicao.json()
            print(dict_cep)
            for dados in dict_cep:
                if dados == 'cep':
                    self.resultado_cep.configure(text=dict_cep[dados])
                elif dados == 'logradouro':
                    self.resultado_logradouro.configure(text=dict_cep[dados])
                elif dados == 'complemento':
                    self.resultado_complemento.configure(text=dict_cep[dados])
                elif dados == 'bairro':
                    self.resultado_bairro.configure(text=dict_cep[dados])
                elif dados == 'localidade':
                    self.resultado_cidade.configure(text=dict_cep[dados])
                elif dados == 'uf':
                    self.resultado_uf.configure(text=dict_cep[dados])
                elif dados == 'ddd':
                    self.resultado_ddd.configure(text=dict_cep[dados])
        except:
            messagebox.showerror("Erro", "Erro ao fazer a consulta. Favor tentar novamente.")

    def click(self,event):
        self.buscar_cep()

class MainWindow(Funcs):
    def __init__(self):
        self.root = root
        self.frame()
        root.mainloop()

    def frame(self):
        self.root.title("Buscador de CEP")
        self.root.configure(background='#CCFFCC')
        self.root.geometry("400x300")
        self.root.resizable(True, False)

        self.lbl_digite_cep = Label(self.root, text='Digite o CEP:', bg='#CCFFCC', font=('Verdana',10))
        self.lbl_digite_cep.place(relx=.15, rely=.09)

        self.entry_cep = Entry(self.root, font=('Verdana',10))
        self.entry_cep.place(relx=.42, rely=.09,relwidth=.35)

        self.buscar = Button(self.root, text='Buscar CEP', command=self.buscar_cep, font=('Verdana',10,'bold'))
        self.buscar.place(relx=.45, rely=.2)
        # click <enter>
        self.root.bind('<Return>',self.click)

        self.lbl_caixa = Label(self.root, borderwidth=1, relief="solid", bg='#CCFFCC')
        self.lbl_caixa.place(relx=.05, rely=.32,relwidth=.9, relheight=.6 )

        self.copyrights = Label(self.root, text='Desenvolvido por Wolnei Hellmann Dircksen',bg='#CCFFCC', font=('consolas',8), anchor='e')
        self.copyrights.place(relx=.32, rely=.92)

        # texto fixo:
        self.cep = Label(self.root, text='CEP: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.cep.place(relx=.1, rely=.35,relwidth=.35)
        self.logradouro = Label(self.root, text='Logradouro: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.logradouro.place(relx=.1, rely=.43,relwidth=.35)
        self.complemento = Label(self.root, text='Complemento: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.complemento.place(relx=.1, rely=.51,relwidth=.35)
        self.bairro = Label(self.root, text='Bairro: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.bairro.place(relx=.1, rely=.59,relwidth=.35)
        self.cidade = Label(self.root, text='Cidade: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.cidade.place(relx=.1, rely=.67,relwidth=.35)
        self.uf = Label(self.root, text='UF: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.uf.place(relx=.1, rely=.75,relwidth=.35)
        self.ddd = Label(self.root, text='DDD: ', bg='#CCFFCC', font=('Verdana',10,'bold'), anchor='e')
        self.ddd.place(relx=.1, rely=.83,relwidth=.35)

        # texto resultado:
        self.resultado_cep = Label(self.root,bg='#CCFFCC', font=('Verdana',10), anchor='w')
        self.resultado_cep.place(relx=.43, rely=.35)
        self.resultado_logradouro = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_logradouro.place(relx=.43, rely=.43)
        self.resultado_complemento = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_complemento.place(relx=.43, rely=.51)
        self.resultado_bairro = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_bairro.place(relx=.43, rely=.59)
        self.resultado_cidade = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_cidade.place(relx=.43, rely=.67)
        self.resultado_uf = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_uf.place(relx=.43, rely=.75)
        self.resultado_ddd = Label(self.root, bg='#CCFFCC', font=('Verdana',10), anchor='e')
        self.resultado_ddd.place(relx=.43, rely=.83)

MainWindow()



