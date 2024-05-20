from tkinter import *
from tkinter import messagebox
import random
import os 


root = Tk()

class Funcs():
    global lista_todos_cpfs
    lista_todos_cpfs = []
    
    def listar_cpf(self):
        os.system('cls')
        print('Lista completa de CPFs já criados: \n')
        for index, cpf in enumerate(lista_todos_cpfs):            
            print(f'{index}. {cpf}')
            
    def gerar_cpf_novo(self):
        os.system('cls'); print('Rodando a função: gerar_cpf_novo()')
        lista_aleatorio_numeros = []
        for numero in range(0,9):
            novo_numero_aleatorio = random.randint(0,9)
            lista_aleatorio_numeros.append(novo_numero_aleatorio)
        print(f'1. Criada lista provisória de 09 números aleatórios: {lista_aleatorio_numeros}')
        
        coeficiente = 10
        somador = 0
        print('2. Cálculo digito 01:')
        for numero in lista_aleatorio_numeros:            
            somador = somador + (numero * coeficiente)
            print(f'-- {numero} * {coeficiente} = {somador}')
            coeficiente -= 1
        digito_01 = 11 - (somador%11)
        if digito_01 >= 10:
            digito_01 = 0       
        print(f'3. O digito 01 é o {digito_01}.') 
        lista_aleatorio_numeros.append(digito_01); print(f'4. Inserido digito 01 na lista: {lista_aleatorio_numeros}')

        coeficiente = 11
        somador = 0
        for numero in lista_aleatorio_numeros:            
            somador = somador + (numero * coeficiente)
            print(f'-- {numero} * {coeficiente} = {somador}')
            coeficiente -= 1
        digito_02 = 11 - (somador%11)
        if digito_02 >= 10:
            digito_02 = 0       
        print(f'5. O digito 02 é o {digito_01}.')   
        lista_aleatorio_numeros.append(digito_02); print(f'6. Inserido digito 01 na lista: {lista_aleatorio_numeros}')
        
        global texto_novo_cpf
        texto_novo_cpf = ''
        for index,numero in enumerate(lista_aleatorio_numeros):
            if index==3 or index==6:
                texto_novo_cpf = texto_novo_cpf + '.'
            elif index==9:
                texto_novo_cpf = texto_novo_cpf + '-'
            texto_novo_cpf = texto_novo_cpf + str(numero)
        print(f'7. Texto CPF criado gerado com sucesso: {texto_novo_cpf}')
        self.label_cpf_aleatorio.configure(text=texto_novo_cpf)
        
        lista_todos_cpfs.append(texto_novo_cpf); print(f'8. Texto CPF {texto_novo_cpf} inserido na lista: lista_todos_cpfs')
    
    def validar_cpf_teste(self,cpf):
        os.system('cls')
        print('Validando CPF inserido manualmente!')
        global cpf_validado
        coeficiente = 10
        somador = 0
        print('1. Cálculo digito 01:')
        for index, numero in enumerate(cpf):
            somador = somador + (numero * coeficiente)
            print(f'-- {numero} * {coeficiente} = {somador}')
            coeficiente -= 1
            if index == 8:
                break
        digito_01 = 11 - (somador%11)
        if digito_01 >= 10:
            digito_01 = 0       
        if digito_01 == cpf[9]:
            print(f'2. digito_01: {digito_01} | cpf[9]: {cpf[9]} | validação: {digito_01 == cpf[9]}')
        else:
            print(f'2. digito_01: {digito_01} | cpf[9]: {cpf[9]} | validação: {digito_01 == cpf[9]}')
        
        print('\n3. Cálculo digito 02:')        
        coeficiente = 11
        somador = 0
        for index, numero in enumerate(cpf):          
            somador = somador + (numero * coeficiente)
            print(f'-- {index} {numero} * {coeficiente} = {somador}')
            coeficiente -= 1
            if index == 9:
                break
        digito_02 = 11 - (somador%11)
        if digito_02 >= 10:
            digito_02 = 0
        if digito_02 == cpf[10]:
            print(f'2. digito_02: {digito_02} | cpf[9]: {cpf[10]} | validação: {digito_02 == cpf[10]}')
        else: 
            print(f'2. digito_02: {digito_02} | cpf[9]: {cpf[10]} | validação: {digito_02 == cpf[10]}')
        
        texto_novo_cpf = ''
        for index,numero in enumerate(cpf):
            if index==3 or index==6:
                texto_novo_cpf = texto_novo_cpf + '.'
            elif index==9:
                texto_novo_cpf = texto_novo_cpf + '-'
            texto_novo_cpf = texto_novo_cpf + str(numero)
        
        if digito_01 == cpf[9] and digito_02 == cpf[10]:
            self.label_validacao_cpf.configure(text=f'O CPF informado {texto_novo_cpf} é válido!', fg='green')   
        else:
            self.label_validacao_cpf.configure(text=f'O CPF informado {texto_novo_cpf} é inválido!', fg='red')  
            
    def validar_cpf(self):
        os.system('cls')
        try:
            dado = self.entrada_cpf.get()
            dado = dado.replace('/','')
            dado = dado.replace('.','')
            dado = dado.replace('-','')
            dado = dado.replace(',','')           
            if len(dado) == 11:
                cpf_em_lista = []
                for numero in dado:
                    cpf_em_lista.append(int(numero))
                self.validar_cpf_teste(cpf_em_lista)
            else:
                self.entrada_cpf.delete(0,'end')
                messagebox.showerror("Erro dado", "Você inseriu um valor incorreto!") 
        except:
            messagebox.showerror("Erro encontrado", "Favor tentar novamente!")  


class MainWindow(Funcs):
    def __init__(self):
        self.root = root
        self.frame()
        root.mainloop()
    def frame(self):
        self.root.title("Gerador e validador de CPF")
        self.root.configure(background='#CCFFE5')
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Labels_frame01
        self.label_01 = Label(self.root, text=' Gerador de CPF aleatório',bd=3, background='#CCFFCC', font=('consolas',10),borderwidth=2, relief="solid", anchor='nw')
        self.label_01.place(relx=.05, rely=.05, relwidth=.9,relheight=.43)        
     
        self.desenvolvedor = Label(self.root, text='Desenvolvido por Wolnei Hellmann Dircksen.', anchor='e', background='#CCFFE5', font=('consolas',8))
        self.desenvolvedor.place(relx=.05, rely=.94, relwidth=.9)
        
        self.texto_cpf_gerado = Label(self.root, text='CPF gerador aleatoriamente:', font=('consolas',12), background='#CCFFCC')
        self.texto_cpf_gerado.place(relx=.17, rely=.24)

        self.label_cpf_aleatorio = Label(self.root, text='000.000.000-00', font=('consolas',12,'bold'), background='#CCFFCC')
        self.label_cpf_aleatorio.place(relx=.60, rely=.24)
        self.gerar_cpf_novo()

        self.desenvolvedor = Label(self.root, text='-- verificar no console do Python a listagem --', anchor='e', background='#CCFFCC', font=('consolas',10))
        self.desenvolvedor.place(relx=.22, rely=.41) 

        # Labels_frame02
        self.label_02 = Label(self.root, text=' Validador de CPF',bd=3, background='#CCFFCC', font=('consolas',10),borderwidth=2, relief="solid", anchor='nw')
        self.label_02.place(relx=.05, rely=.50, relwidth=.9,relheight=.43)
        
        self.label_input_cpf = Label(self.root, text='Digite o CPF a ser validado:', font=('consolas',12), background='#CCFFCC')
        self.label_input_cpf.place(relx=.16, rely=.60)
        
        self.label_validacao_cpf = Label(self.root, text='Aqui irá informar se CPF informado é válido ou não!', font=('consolas',12,'bold'), anchor='center', background='#CCFFCC')
        self.label_validacao_cpf.place(relx=.12, rely=.82, relwidth=.80)

        # Botões
        self.gerador_novo_cpf = Button(self.root, text='Gerar novo CPF aleatório',font=('consolas',10,'bold'), command=self.gerar_cpf_novo)
        self.gerador_novo_cpf.place(relx=.20,rely=.12, relwidth=.60, relheight=.10) 
        
        self.listar_cpf_gerados = Button(self.root, text='Listar no console todos os CPFs já gerados',font=('consolas',10,'bold'),command=self.listar_cpf)
        self.listar_cpf_gerados.place(relx=.20,rely=.32, relwidth=.60, relheight=.10)
        
        self.validar_cpf = Button(self.root, text='Validar CPF digitado',font=('consolas',10,'bold'), command=self.validar_cpf)
        self.validar_cpf.place(relx=.20,rely=.70, relwidth=.60, relheight=.10)
        
        # Entrada dados
        self.entrada_cpf = Entry(self.root, font=('consolas',12))
        self.entrada_cpf.place(relx=.60, rely=.60, relwidth=.25,relheight=.07)
        
MainWindow()