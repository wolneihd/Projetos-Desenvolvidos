from tkinter import *
from cotacoes_novas import *
from tkinter import messagebox

root = Tk()

class Funcs():
    def limpar_entradas(self):
        self.entrada_01.delete(0,'end')
        self.entrada_02.delete(0,'end')
        self.entrada_03.delete(0,'end')
        self.entrada_04.delete(0,'end')
        self.entrada_05.delete(0,'end')
        self.entrada_06.delete(0,'end')
    def desabilitar_botoes(self):
        self.btn_brl.configure(state=NORMAL, bg='lightgray')
        self.btn_usd.configure(state=NORMAL, bg='lightgray')
        self.btn_gbp.configure(state=NORMAL, bg='lightgray')
        self.btn_eur.configure(state=NORMAL, bg='lightgray')
        self.btn_cny.configure(state=NORMAL, bg='lightgray')
        self.btn_jpy.configure(state=NORMAL, bg='lightgray')
        self.btn_krw.configure(state=NORMAL, bg='lightgray')
    def alterar_valores_configuracao_BRL(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_brl.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_brl:
            print(cotacao_brl[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_brl[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_USD(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_usd.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_usd:
            print(valor, cotacao_usd[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_usd[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_GBP(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_gbp.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_gbp:
            print(cotacao_gbp[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_gbp[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_cny(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_cny.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_cny:
            print(cotacao_cny[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_cny[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_eur(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_eur.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_eur:
            print(cotacao_eur[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_eur[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_jpy(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_jpy.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_jpy:
            print(cotacao_jpy[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_jpy[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    def alterar_valores_configuracao_krw(self):
        lista_valores = []
        self.desabilitar_botoes()
        self.btn_krw.configure(state=DISABLED, bg='cornsilk')
        self.limpar_entradas()
        lista_label = []
        for valor in cotacao_krw:
            print(cotacao_krw[valor])
            lista_label.append(valor)
            lista_valores.append(cotacao_krw[valor])
        self.entrada_01.insert(0, lista_valores[0])
        self.entrada_02.insert(0, lista_valores[1])
        self.entrada_03.insert(0, lista_valores[2])
        self.entrada_04.insert(0, lista_valores[3])
        self.entrada_05.insert(0, lista_valores[4])
        self.entrada_06.insert(0, lista_valores[5])
        self.lbl_conversao01.configure(text=f'{lista_label[0]}:')
        self.lbl_conversao02.configure(text=f'{lista_label[1]}:')
        self.lbl_conversao03.configure(text=f'{lista_label[2]}:')
        self.lbl_conversao04.configure(text=f'{lista_label[3]}:')
        self.lbl_conversao05.configure(text=f'{lista_label[4]}:')
        self.lbl_conversao06.configure(text=f'{lista_label[5]}:')
    global radio_de, radio_para, valor_inserido
    def limpar_valor_entry(self):
        global valor_inserido
        try:
            valor_inserido = self.entrada_valor.get()
            valor_inserido = valor_inserido.replace(',','.')
            valor_inserido = float(valor_inserido)
            print('Valor limpo: ', valor_inserido, type(valor_inserido))            
        except:
            messagebox.showerror('Erro','Inserido valor incorreto. Favor tentar novamente!')   
    def configurar_string_conversao(self):
        global valor_inserido
        self.label_conversao_final.configure(text='O valor {R$} {100,00} convertido em {USD} é {25,00}{USD}')
        if radio_de.get() == 0:
            for index, valor in enumerate(cotacao_brl):
                if radio_para.get()==0 and index==0:
                    self.label_conversao_final.configure(text='Converter BRL para BRL não é possível!',fg='red')
                elif radio_para.get()==1 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==1:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')                  
                elif radio_para.get()==4 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor R$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_brl[valor]:.2f}',fg='red')
        if radio_de.get() == 1:
            for index, valor in enumerate(cotacao_usd):
                #print(index, valor, cotacao_usd[valor])
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text='Converter USD para USD não é possível!',fg='red')
                elif radio_para.get()==2 and index==1:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')                  
                elif radio_para.get()==4 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor US$ {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_usd[valor]:.2f}',fg='red')
        if radio_de.get() == 2:
            for index, valor in enumerate(cotacao_gbp):
                #print(index, valor, cotacao_gbp[valor])
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==1:
                    self.limpar_valor_entry()
                    print(index, valor, cotacao_gbp[valor])
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==1:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text='Converter GBP para GBP não é possível!',fg='red')
                elif radio_para.get()==3 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')                  
                elif radio_para.get()==4 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor GBP {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_gbp[valor]:.2f}',fg='red')
        if radio_de.get() == 3:
            for index, valor in enumerate(cotacao_cny):
                #print(index, valor, cotacao_gbp[valor])
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==1:
                    self.limpar_valor_entry()
                    print(index, valor, cotacao_cny[valor])
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'Converter CNY para CNY não é possível!',fg='red')               
                elif radio_para.get()==4 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor CNY {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_cny[valor]:.2f}',fg='red')   
        if radio_de.get() == 4:
            for index, valor in enumerate(cotacao_eur):
                #print(index, valor, cotacao_gbp[valor])
                moeda = 'EUR'
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==1:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor EUR {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor EUR {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor EUR {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')              
                elif radio_para.get()==4 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'Converter EUR para EUR não é possível!',fg='red') 
                elif radio_para.get()==5 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor EUR {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor EUR {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_eur[valor]:.2f}',fg='red')   
        if radio_de.get() == 5:
            for index, valor in enumerate(cotacao_jpy):
                #print(index, valor, cotacao_gbp[valor])
                moeda = 'JPY'
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==1:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')              
                elif radio_para.get()==4 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'Converter {moeda} para {moeda} não é possível!',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_jpy[valor]:.2f}',fg='red')  
        if radio_de.get() == 6:
            for index, valor in enumerate(cotacao_krw):
                #print(index, valor, cotacao_gbp[valor])
                moeda = 'KRW'
                if radio_para.get()==0 and index==0:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')
                elif radio_para.get()==1 and index==1:
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')
                elif radio_para.get()==2 and index==2:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')
                elif radio_para.get()==3 and index==3:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')              
                elif radio_para.get()==4 and index==4:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')
                elif radio_para.get()==5 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'O valor {moeda} {valor_inserido:.2f} convertido em {valor} é {valor_inserido*cotacao_krw[valor]:.2f}',fg='red')
                elif radio_para.get()==6 and index==5:                    
                    self.limpar_valor_entry()
                    self.label_conversao_final.configure(text=f'Converter {moeda} para {moeda} não é possível!',fg='red')
                    
class MainWindow(Funcs):
    def __init__(self):
        self.root = root
        self.frame()
        root.mainloop()

    def frame(self):
        self.root.title("Conversor moedas")
        self.root.configure(background='#caf0b4')
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Labels
        self.label_01 = Label(self.root, text=' Conversor de moedas', bd=3, background='#caf0b4',
                              font=('consolas', 10, 'bold'), borderwidth=1, relief="solid", anchor='nw')
        self.label_01.place(relx=.05, rely=.05, relwidth=.9, relheight=.87)

        self.label_inserir_dado = Label(self.root, text='Digite o valor a ser convertido: ', background='#caf0b4',
                                        font=('consolas', 10))
        self.label_inserir_dado.place(relx=.08, rely=.15)

        self.label_desenvolvedor = Label(self.root, text='Desenvolvido por Wolnei Hellmann Dircksen',
                                         background='#caf0b4', font=('consolas', 8))
        self.label_desenvolvedor.place(relx=.45, rely=.93)

        self.label_conversao_final = Label(self.root, text='',font=('consolas', 10, 'bold'), background='#caf0b4', anchor='center')
        self.label_conversao_final.place(relx=.10, rely=.70,relwidth=.8)

        # De
        global radio_de
        radio_de = IntVar(value=0)

        self.label_de = Label(self.root, text=' De', bd=3, background='#caf0b4', font=('consolas', 10, 'bold'),
                              borderwidth=1, relief="solid", anchor='nw')
        self.label_de.place(relx=.25, rely=.25, relwidth=.2, relheight=.43)

        self.radio_de_BRL = Radiobutton(self.root, text='BRL R$', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=0)
        self.radio_de_BRL.place(relx=.26, rely=.3)
        self.radio_de_USD = Radiobutton(self.root, text='USD US$', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=1)
        self.radio_de_USD.place(relx=.26, rely=.35)
        self.radio_de_GBP = Radiobutton(self.root, text='GBP £', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=2)
        self.radio_de_GBP.place(relx=.26, rely=.40)
        self.radio_de_CNY = Radiobutton(self.root, text='CNY ¥', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=3)
        self.radio_de_CNY.place(relx=.26, rely=.45)
        self.radio_de_EUR = Radiobutton(self.root, text='EUR €', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=4)
        self.radio_de_EUR.place(relx=.26, rely=.5)
        self.radio_de_JPY = Radiobutton(self.root, text='JPY ¥', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=5)
        self.radio_de_JPY.place(relx=.26, rely=.55)
        self.radio_de_KRW = Radiobutton(self.root, text='KRW ₩', background='#caf0b4', font=('consolas', 10),
                                        variable=radio_de, value=6)
        self.radio_de_KRW.place(relx=.26, rely=.6)

        # Para
        global radio_para
        radio_para = IntVar(value=0)

        self.label_para = Label(self.root, text=' Para', bd=3, background='#caf0b4', font=('consolas', 10, 'bold'),
                                borderwidth=1, relief="solid", anchor='nw')
        self.label_para.place(relx=.55, rely=.25, relwidth=.2, relheight=.43)

        self.radio_para_BRL = Radiobutton(self.root, text='BRL R$', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=0)
        self.radio_para_BRL.place(relx=.56, rely=.3)
        self.radio_para_USD = Radiobutton(self.root, text='USD US$', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=1)
        self.radio_para_USD.place(relx=.56, rely=.35)
        self.radio_para_GBP = Radiobutton(self.root, text='GBP £', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=2)
        self.radio_para_GBP.place(relx=.56, rely=.4)
        self.radio_para_CNY = Radiobutton(self.root, text='CNY ¥', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=3)
        self.radio_para_CNY.place(relx=.56, rely=.45)
        self.radio_para_EUR = Radiobutton(self.root, text='EUR €', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=4)
        self.radio_para_EUR.place(relx=.56, rely=.5)
        self.radio_para_JPY = Radiobutton(self.root, text='JPY ¥', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=5)
        self.radio_para_JPY.place(relx=.56, rely=.55)
        self.radio_para_KRW = Radiobutton(self.root, text='KRW ₩', background='#caf0b4', font=('consolas', 10),
                                          variable=radio_para, value=6)
        self.radio_para_KRW.place(relx=.56, rely=.6)

        # Botões configurar:
        self.configurar = Button(self.root, text='Configurar cotações', font=('consolas', 10), command=self.configurar)
        self.configurar.place(relx=.65, rely=.85,relheight=.05)
        
        # Botão CONVERTER:
        self.configurar = Button(self.root, text='CONVERTER', font=('consolas', 12,'bold'), command=self.configurar_string_conversao)
        self.configurar.place(relx=.32, rely=.76,relwidth=.4)        

        # Entrada valor a ser convertido:
        self.entrada_valor = Entry(self.root, font=('consolas', 12), justify=RIGHT)
        self.entrada_valor.insert(0,'0,00')
        self.entrada_valor.place(relx=.55, rely=.14, relwidth=.25, relheight=.07)

    def configurar(self):
        self.root2 = Toplevel()
        self.root2.title("Alterar cotações")
        self.root2.configure(background='#caf0b4')
        self.root2.geometry("400x300")
        self.root2.resizable(False, False)

        # Labels

        self.lbl_conversao01 = Label(self.root2, text='BRL para USD: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao01.place(relx=.15, rely=.2)
        self.lbl_conversao02 = Label(self.root2, text='BRL para GBP: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao02.place(relx=.15, rely=.3)
        self.lbl_conversao03 = Label(self.root2, text='BRL para EUR: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao03.place(relx=.15, rely=.4)
        self.lbl_conversao04 = Label(self.root2, text='BRL para CNY: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao04.place(relx=.15, rely=.5)
        self.lbl_conversao05 = Label(self.root2, text='BRL para JPY: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao05.place(relx=.15, rely=.6)
        self.lbl_conversao06 = Label(self.root2, text='BRL para KRW: ', font=('consolas', 12), bg='#caf0b4')
        self.lbl_conversao06.place(relx=.15, rely=.7)

        # entrys cotações para alterar:

        self.entrada_01 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_01.place(relx=.5, rely=.2, relwidth=.3)
        self.entrada_02 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_02.place(relx=.5, rely=.3, relwidth=.3)
        self.entrada_03 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_03.place(relx=.5, rely=.4, relwidth=.3)
        self.entrada_04 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_04.place(relx=.5, rely=.5, relwidth=.3)
        self.entrada_05 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_05.place(relx=.5, rely=.6, relwidth=.3)
        self.entrada_06 = Entry(self.root2, font=('consolas', 12), justify=RIGHT)
        self.entrada_06.place(relx=.5, rely=.7, relwidth=.3)

        # Botões cotacoes configurar:
        self.btn_brl = Button(self.root2, text='BRL', font=('consolas', 10), command= self.alterar_valores_configuracao_BRL)
        self.btn_brl.place(relx=.15, rely=.1, relwidth=.1)

        self.btn_usd = Button(self.root2, text='USD', font=('consolas', 10), command= self.alterar_valores_configuracao_USD)
        self.btn_usd.place(relx=.25, rely=.1, relwidth=.1)

        self.btn_gbp = Button(self.root2, text='GBP', font=('consolas', 10), command= self.alterar_valores_configuracao_GBP)
        self.btn_gbp.place(relx=.35, rely=.1, relwidth=.1)

        self.btn_cny = Button(self.root2, text='CNY', font=('consolas', 10), command=self.alterar_valores_configuracao_cny)
        self.btn_cny.place(relx=.45, rely=.1, relwidth=.1)

        self.btn_eur = Button(self.root2, text='EUR', font=('consolas', 10), command=self.alterar_valores_configuracao_eur)
        self.btn_eur.place(relx=.55, rely=.1, relwidth=.1)

        self.btn_jpy = Button(self.root2, text='JPY', font=('consolas', 10),command=self.alterar_valores_configuracao_jpy)
        self.btn_jpy.place(relx=.65, rely=.1, relwidth=.1)

        self.btn_krw = Button(self.root2, text='KRW', font=('consolas', 10),command=self.alterar_valores_configuracao_krw)
        self.btn_krw.place(relx=.75, rely=.1, relwidth=.1)

        self.salvar = Button(self.root2, text='Salvar', font=('consolas', 10))
        self.salvar.place(relx=.7, rely=.85, relwidth=.17)

        self.cancelar = Button(self.root2, text='Cancelar', font=('consolas', 10), command=self.fechar_salvar)
        self.cancelar.place(relx=.52, rely=.85, relwidth=.17)

        self.alterar_valores_configuracao_BRL()

    def fechar_salvar(self):
        self.root2.destroy()
MainWindow()