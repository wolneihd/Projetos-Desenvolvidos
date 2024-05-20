from tkinter import *
from tkinter import messagebox 

root = Tk()

class Funcs():
    global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio, operacao
    texto_mostrador = str(0)
    texto_mostrador_provisorio = str(0); 
    valor_01 = None
    valor_02 = None
    resultado = None
    operacao = None
    print('tela conta: ', texto_mostrador, type(texto_mostrador))
    print('Valor_01: ', valor_01, type(valor_01))
    print('Valor_02: ', valor_02, type(valor_02))
    print(f'texto_mostrador_provisorio: {texto_mostrador_provisorio}')
    
    def limpar(self):
        global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio
        texto_mostrador = str(0); 
        texto_mostrador_provisorio = str(0); 
        valor_01 = None
        valor_02 = None
        resultado = None        
        self.mostrador.configure(text=texto_mostrador)        
        self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
        print(f'Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')
        
    def somar(self):
        global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio, operacao
        operacao = '+'
        if valor_01 == None:
            valor_01 = int(texto_mostrador); print('inserido em  valor_01 = ', valor_01, type(valor_01))
            texto_mostrador_provisorio = str(valor_01) + ' + '
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            texto_mostrador = str(0); print('limpar tela: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)   
            print(f'if soma ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')
        else: 
            valor_02 = int(texto_mostrador); print('inserido em  valor_02 = ', valor_01, type(valor_01))
            resultado = str(valor_01 + valor_02)
            texto_mostrador = resultado
            texto_mostrador_provisorio = str(resultado) + ' + '
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            valor_02 = None
            valor_01 = int(resultado);
            self.mostrador.configure(text=str(0))
            texto_mostrador = str(0)
            print(f'else soma ==> Valores limpos: \n valor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio} \n resultado {resultado}')

    def subtrair(self):
        global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio, operacao
        operacao = '-'
        if valor_01 == None:
            valor_01 = int(texto_mostrador); print('inserido em  valor_01 = ', valor_01, type(valor_01))
            texto_mostrador_provisorio = str(valor_01) + ' - '
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            texto_mostrador = str(0); print('limpar tela: ', texto_mostrador, type(texto_mostrador))
            print(f'if soma ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')
        else:             
            valor_02 = int(texto_mostrador); print('inserido em  valor_02 = ', valor_01, type(valor_01))
            resultado = str(valor_01 - valor_02)
            texto_mostrador = resultado
            texto_mostrador_provisorio = str(resultado) + ' - '
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            valor_02 = None
            valor_01 = int(resultado);
            self.mostrador.configure(text=str(0))
            print(f'if soma ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')

    def igual(self):
        global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio, operacao
        if operacao == '-':
            print(f'clicado em IGUAL ===> SUBTRAIR ambos valores {valor_01} - {valor_02}')
            valor_02 = int(texto_mostrador); print('inserido em  valor_02 = ', valor_01, type(valor_01))
            resultado = str(valor_01 - valor_02); print(f'resultado: {resultado}')
            texto_mostrador = str(0)
            texto_mostrador_provisorio = str(resultado)
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            valor_02 = None
            valor_01 = int(resultado);
            self.mostrador.configure(text=str(0))
            print(f'if soma ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')
        elif operacao == '+':
            print(f'clicado em IGUAL ===> SOMAR ambos valores {valor_01} + {valor_02}')
            valor_02 = int(texto_mostrador); print('inserido em  valor_02 = ', valor_01, type(valor_01))
            resultado = str(valor_01 + valor_02); print(f'resultado: {resultado}')
            texto_mostrador = str(0)
            texto_mostrador_provisorio = str(resultado)
            self.mostrador_provisorio.configure(text=texto_mostrador_provisorio)
            valor_02 = None
            valor_01 = int(resultado);
            self.mostrador.configure(text=str(0))
            print(f'if soma ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio}')
            
    def add_07(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '7'; print('add 07: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
            print(f'+++ if ADD_7 ==> Valores: \n valor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio} \n resultado {resultado} \n {texto_mostrador == "0"}')
        else:             
            #texto_mostrador = str(0)
            texto_mostrador += '7'; print('add 07: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
            print(f'+++ else ADD_7 ==> Valores: \n valor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio} \n resultado {resultado} \n {texto_mostrador != "0"}')      
 
    def add_08(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '8'; print('add 08: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '8'; print('add 08: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_09(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '9'; print('add 09: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '9'; print('add 09: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_04(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '4'; print('add 04: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '4'; print('add 04: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_05(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '5'; print('add 05: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '5'; print('add 05: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_06(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '6'; print('add 06: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '6'; print('add 06: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_01(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '1'; print('add 01: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '1'; print('add 01: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_02(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '2'; print('add 02: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '2'; print('add 02: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_03(self):
        global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '3'; print('add 03: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
        else: 
            texto_mostrador += '3'; print('add 03: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)

    def add_00(self):
        global texto_mostrador, valor_01, valor_02, resultado, texto_mostrador_provisorio, operacao, resultado
        #global texto_mostrador
        if texto_mostrador == '0':
            texto_mostrador = '0'; print('add 00: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
            print(f'if ADD_00 ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio} \n resultado {resultado}')
        else: 
            texto_mostrador += '0'; print('add 00: ', texto_mostrador, type(texto_mostrador))
            self.mostrador.configure(text=texto_mostrador)
            print(f'else add_00 ==> Valores limpos: \nvalor_01 {valor_01} \n valor_02 {valor_02} \n texto_mostrador {texto_mostrador} \n texto_mostrador_provisorio {texto_mostrador_provisorio} \n resultado {resultado}')

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela_calculadora()
        self.entrada_dados()
        root.mainloop()
    def tela_calculadora(self):
        self.root.title("Calculadora")
        self.root.configure(background='lightblue')
        self.root.geometry("400x300")
        self.root.resizable(True, True) # Vertical, Horizontal
    def entrada_dados(self):
        # Label - provisório
        self.mostrador_provisorio = Label(self.root, text=texto_mostrador_provisorio, bg='lightgrey', relief='solid', font=('Trebuchet MS',12),fg='black', justify=RIGHT,anchor='e')
        self.mostrador_provisorio.place(relx=0.1,rely=0.05,relwidth=.8)         
                
        # Label - mostrador
        self.assinatura = Label(self.root, text='Criado por Wolnei Hellmann Dircksen', bg='lightblue', font=('Calibri',8), justify=RIGHT,anchor='e')
        self.assinatura.place(relx=0.1,rely=0.9,relwidth=.8) 
        
        # Label - assinatura
        self.mostrador = Label(self.root, text=texto_mostrador, bg='azure', relief='solid', font=('Trebuchet MS',12,'bold'),fg='red', justify=RIGHT,anchor='e')
        self.mostrador.place(relx=0.1,rely=0.155,relwidth=.8)       
        
        # Botão - 07
        self.btn_01 = Button(self.root, text="7", bd=2, font=('Verdana',8,'bold'), command=self.add_07)
        self.btn_01.place(relx=0.1,rely=0.26, relwidth=0.15, relheight=0.1)                  

        # Botão - 08
        self.btn_01 = Button(self.root, text="8", bd=2, font=('Verdana',8,'bold'), command=self.add_08)
        self.btn_01.place(relx=0.3,rely=0.26, relwidth=0.15, relheight=0.1)  

        # Botão - 09
        self.btn_01 = Button(self.root, text="9", bd=2, font=('Verdana',8,'bold'), command=self.add_09)
        self.btn_01.place(relx=0.5,rely=0.26, relwidth=0.15, relheight=0.1)  

        # Botão - Limpar
        self.btn_01 = Button(self.root, text="Limpar", bd=2, font=('Verdana',8,'bold'), command=self.limpar)
        self.btn_01.place(relx=0.7,rely=0.26, relwidth=0.2, relheight=0.1)  

        # Botão - 04
        self.btn_01 = Button(self.root, text="4", bd=2, font=('Verdana',8,'bold'), command=self.add_04)
        self.btn_01.place(relx=0.1,rely=0.40, relwidth=0.15, relheight=0.1)                  

        # Botão - 05
        self.btn_01 = Button(self.root, text="5", bd=2, font=('Verdana',8,'bold'), command=self.add_05)
        self.btn_01.place(relx=0.3,rely=0.40, relwidth=0.15, relheight=0.1)  

        # Botão - 06
        self.btn_01 = Button(self.root, text="6", bd=2, font=('Verdana',8,'bold'), command=self.add_06)
        self.btn_01.place(relx=0.5,rely=0.40, relwidth=0.15, relheight=0.1)  
        
        # Botão - adicionar (+)
        self.somar = Button(self.root, text="+", bd=2, font=('Verdana',8,'bold'), command=self.somar)
        self.somar.place(relx=0.7,rely=0.40, relwidth=0.2, relheight=0.1) 

        # Botão - 01
        self.btn_01 = Button(self.root, text="1", bd=2, font=('Verdana',8,'bold'), command=self.add_01)
        self.btn_01.place(relx=0.1,rely=0.55, relwidth=0.15, relheight=0.1)                  

        # Botão - 02
        self.btn_01 = Button(self.root, text="2", bd=2, font=('Verdana',8,'bold'), command=self.add_02)
        self.btn_01.place(relx=0.3,rely=0.55, relwidth=0.15, relheight=0.1)  

        # Botão - 03
        self.btn_01 = Button(self.root, text="3", bd=2, font=('Verdana',8,'bold'), command=self.add_03)
        self.btn_01.place(relx=0.5,rely=0.55, relwidth=0.15, relheight=0.1)  
        
        # Botão - subtrair (-)
        self.somar = Button(self.root, text="-", bd=2, font=('Verdana',8,'bold'), command=self.subtrair)
        self.somar.place(relx=0.7,rely=0.55, relwidth=0.2, relheight=0.1) 
        
        # Botão - 0 [zero]
        self.btn_01 = Button(self.root, text="0", bd=2, font=('Verdana',8,'bold'), command=self.add_00)
        self.btn_01.place(relx=0.3,rely=0.70, relwidth=0.15, relheight=0.1)       

        # Botão - igual (=)
        self.somar = Button(self.root, text="=", bd=2, font=('Verdana',8,'bold'), command=self.igual)
        self.somar.place(relx=0.7,rely=0.70, relwidth=0.2, relheight=0.1) 

Application()