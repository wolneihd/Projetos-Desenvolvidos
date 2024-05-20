from tkinter import *
from tkinter import messagebox
from lista_paises_continente import *
import random
import sqlite3

root = Tk()


class Funcs():
    def conecta_bd(self):
        self.conn = sqlite3.connect("paises.bd");
        print("conectando ao banco de dados")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close();
        print("desconectado do bd")

    def montaTabelas(self):
        self.conecta_bd()
        # CRIA TABELA DE PAISES - CAPITAIS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS paises (
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT NOT NULL,
                capital TEXT NOT NULL,
                continente INTEGER NOT NULL
            );               
        """)
        self.conn.commit();
        print("Banco de dados PAISES criado com sucesso!")
        # CRIA TABELA DE PAISES - CONTINENTES
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS continente (
                cod INTEGER PRIMARY KEY,
                continente TEXT NOT NULL
            );               
        """)
        self.conn.commit();
        print("Banco de dados CONTINENTE criado com sucesso!")
        self.desconecta_bd()
    
    global qtd_paises
    def cadastro_paises_na_tabela(self):
        print('Rodar: cadastro_paises_na_tabela')
        self.conecta_bd()
        dados = self.cursor.execute("""SELECT COUNT (cod) FROM paises""")
        for i in dados:
            print(f'Quandidade de resultados: {i[0]} {type(i[0])}')
            if i[0] == 0:
                for pais in paises:
                    insert_sql = (
                        """INSERT INTO paises (country, capital,continente) VALUES (:country,:capital,:continente)""")
                    self.cursor.execute(insert_sql,
                                        {'country': pais, 'capital': paises[pais][0], 'continente': paises[pais][1]})
                    self.conn.commit()
                    print(f"Dados de {pais} inseridos na tabela com sucesso!")
            else:
                global qtd_paises
                qtd_paises = i[0]
                print(f"Tabela de dados de paises já cadastrada: {qtd_paises} cadastrados.")
        self.desconecta_bd()

    def cadastro_continentes_na_tabela(self):
        print('Rodar: cadastro_continentes_na_tabela')
        # for dado in continente:
        #    print(dado, continente[dado]) #index_continente,nome_continente
        self.conecta_bd()
        dados = self.cursor.execute("""SELECT COUNT (cod) FROM continente""")
        for i in dados:
            print(f'Quandidade de resultados: {i[0]} {type(i[0])}')
            if i[0] == 0:
                for dado in continente:
                    insert_sql = ("""INSERT INTO continente (cod, continente) VALUES (:cod,:continente)""")
                    self.cursor.execute(insert_sql, {'cod': dado, 'continente': continente[dado]})
                    self.conn.commit()
                    print(f"Dados de {continente[dado]} inseridos na tabela com sucesso!")
            else:
                #global qtd_continentes
                #qtd_continentes = i[0]
                print(f"Tabela de dados de CONTINENTES já cadastrada: {i[0]} cadastrados.")
        self.desconecta_bd()

    global texto_pergunta, tipo_pergunta
    texto_pergunta = ''

    def gerar_tipo_de_pergunta(self):
        #global texto_pergunta, tipo_pergunta
        index_tipo_pergunta = random.randint(0, 1)
        if index_tipo_pergunta == 0:
            #texto_pergunta = 'Qual a capital do país: '
            return 'pais'
        if index_tipo_pergunta == 1:
            #texto_pergunta = 'Qual o continente do país: '
            return 'continente'

    global cod_pais_resposta
    cod_pais_resposta = ''
    global texto_pais_resposta
    texto_pais_resposta = ''
    global texto_capital_resposta
    texto_capital_resposta = ''

    global texto_opcao01, texto_opcao02, texto_opcao03, texto_opcao04

    def gerar_quatro_respostas_paises(self):
        global texto_opcao01, texto_opcao02, texto_opcao03, texto_opcao04, cod_pais_resposta, texto_capital_resposta
        self.conecta_bd()
        print("gerar_quatro_respostas_paises")
        lista_index_quatro_paises = []
        lista_texto_quatro_capitais = []
        dados = self.cursor.execute("""SELECT COUNT (cod) FROM paises""")
        for i in dados:
            global qtd_paises
            qtd_paises = i[0]
            print(f'Quandidade de resultados: {i[0]} {type(i[0])}')    
        while True:
            aleatorio_novo = random.randint(1, qtd_paises)
            if aleatorio_novo not in lista_index_quatro_paises:
                lista_index_quatro_paises.append(aleatorio_novo)
            if len(lista_index_quatro_paises) == 4:
                break
        global cod_pais_resposta
        cod_pais_resposta = random.choice(lista_index_quatro_paises)
        print(f"Pais respostas {cod_pais_resposta}")
        dados = self.cursor.execute("""SELECT cod, country, capital FROM paises""")
        for row in dados:
            cod, country, capital = row
            for numero in lista_index_quatro_paises:
                if numero == cod:
                    lista_texto_quatro_capitais.append(capital)
                if cod == cod_pais_resposta:
                    global texto_pais_resposta, texto_capital_resposta
                    texto_pais_resposta = country
                    texto_capital_resposta = capital
        texto_opcao01 = lista_texto_quatro_capitais[0]
        texto_opcao02 = lista_texto_quatro_capitais[1]
        texto_opcao03 = lista_texto_quatro_capitais[2]
        texto_opcao04 = lista_texto_quatro_capitais[3]
        self.desconecta_bd()

    def gerar_quatro_respostas_continentes(self):
        global texto_opcao01, texto_opcao02, texto_opcao03, texto_opcao04, cod_pais_resposta, texto_capital_resposta
        print(f'pais respostas, verfiicar continente! {cod_pais_resposta}')
        lista_todos_codigos_continentes = []
        lista_quatro_respostas_continente = []
        lista_quatro_continentes_texto = []

        self.conecta_bd()

        sql = ("""SELECT continente FROM paises where cod=(:cod)""")
        dados = self.cursor.execute(sql, {'cod': cod_pais_resposta})
        for row in dados:
            lista_quatro_respostas_continente.append(row[0])
            # print(f'cod_pais {cod_pais_resposta} inserido lista_quatro_respostas_continente: ',row[0])

        dados = self.cursor.execute(
            """SELECT paises.cod,paises.country,paises.capital,continente.continente from 'paises' inner join 'continente' where paises.continente=continente.cod""")
        for row in dados:
            cod, pais, capital, continente = row
            if cod_pais_resposta == cod:
                texto_pais_resposta = continente
                texto_capital_resposta = continente
                print('===>', texto_capital_resposta)

        dados = self.cursor.execute("""SELECT cod FROM continente""")
        for row in dados:
            lista_todos_codigos_continentes.append(row[0])
        print(lista_todos_codigos_continentes)

        while True:
            aleatorio_novo = random.choice(lista_todos_codigos_continentes)
            if aleatorio_novo not in lista_quatro_respostas_continente:
                lista_quatro_respostas_continente.append(aleatorio_novo)
            if len(lista_quatro_respostas_continente) == 4:
                break

        dados = self.cursor.execute("""SELECT cod,continente FROM continente""")
        for row in dados:
            cod, continente = row
            # print(cod,continente)
            for codigo in lista_quatro_respostas_continente:
                if codigo == cod:
                    lista_quatro_continentes_texto.append(continente)
                    # print(continente)
        texto_opcao01 = lista_quatro_continentes_texto[0]
        texto_opcao02 = lista_quatro_continentes_texto[1]
        texto_opcao03 = lista_quatro_continentes_texto[2]
        texto_opcao04 = lista_quatro_continentes_texto[3]
        self.desconecta_bd()

    def texto_pais_selecionado(self):
        return texto_pais_resposta

    global respostas_certas
    respostas_certas = 0

    def zerar_contador_certas(self):
        global respostas_certas
        respostas_certas = 0
        print(f"resposta certas zeradas com sucesso: {respostas_certas}")

    def contar_respostas_certas(self):
        global respostas_certas
        respostas_certas = respostas_certas + 1
        print(f'Total de respostas certas consecutivas: {respostas_certas}')
        return respostas_certas

    def validar_resposta_01(self):
        print(texto_opcao01, texto_capital_resposta)
        if texto_opcao01 == texto_capital_resposta:
            self.opcao_1.configure(bg='springgreen')
            self.resposta_certa_gerar_novas_respostas()
            self.contar_respostas_certas()
        else:
            self.opcao_1.configure(bg='lightcoral')
            self.root2.destroy()
            messagebox.showerror(title='GeoQuiz', message=f'Você infelizmente errou! Você acertou {respostas_certas}!')
            self.zerar_contador_certas()

    def validar_resposta_02(self):
        print(texto_opcao02, texto_capital_resposta)
        if texto_opcao02 == texto_capital_resposta:
            self.opcao_2.configure(bg='springgreen')
            self.resposta_certa_gerar_novas_respostas()
            self.contar_respostas_certas()
        else:
            self.opcao_2.configure(bg='lightcoral')
            self.root2.destroy()
            messagebox.showerror(title='GeoQuiz', message=f'Você infelizmente errou! Você acertou {respostas_certas}!')
            self.zerar_contador_certas()

    def validar_resposta_03(self):
        print(texto_opcao03, texto_capital_resposta)
        if texto_opcao03 == texto_capital_resposta:
            self.opcao_3.configure(bg='springgreen')
            self.resposta_certa_gerar_novas_respostas()
            self.contar_respostas_certas()
        else:
            self.opcao_3.configure(bg='lightcoral')
            self.root2.destroy()
            messagebox.showerror(title='GeoQuiz', message=f'Você infelizmente errou! Você acertou {respostas_certas}!')
            self.zerar_contador_certas()

    def validar_resposta_04(self):
        print(texto_opcao04, texto_capital_resposta)
        if texto_opcao04 == texto_capital_resposta:
            self.opcao_4.configure(bg='springgreen')
            self.resposta_certa_gerar_novas_respostas()
            self.contar_respostas_certas()
        else:
            self.opcao_4.configure(bg='lightcoral')
            self.root2.destroy()
            messagebox.showerror(title='GeoQuiz', message=f'Você infelizmente errou! Você acertou {respostas_certas}!')
            self.zerar_contador_certas()

    def resposta_certa_gerar_novas_respostas(self):
        self.opcao_1.configure(state=DISABLED)
        self.opcao_2.configure(state=DISABLED)
        self.opcao_3.configure(state=DISABLED)
        self.opcao_4.configure(state=DISABLED)
        answer = messagebox.askquestion("GeoQuiz", "Deseja ir a próxima questão?")
        if answer == 'no':
            self.root.destroy()
        elif answer == 'yes':
            # self.gerar_tipo_de_pergunta()
            tipo_pergunta = self.gerar_tipo_de_pergunta()
            print('====> tipo pergunda 2', tipo_pergunta)
            if tipo_pergunta == 'pais':
                texto_pergunta = 'Qual a capital do país: '
                self.lbl_pergunta.configure(text=texto_pergunta)
                self.gerar_quatro_respostas_paises()
            if tipo_pergunta == 'continente':
                texto_pergunta = 'Qual o continente do país: '
                self.lbl_pergunta.configure(text=texto_pergunta)
                self.gerar_quatro_respostas_paises()
                self.gerar_quatro_respostas_continentes()
            # self.gerar_quatro_respostas_paises()

            self.lbl_pais.configure(text=self.texto_pais_selecionado())
            self.opcao_1.configure(bg='cornsilk', state=NORMAL, text=texto_opcao01)
            self.opcao_2.configure(bg='cornsilk', state=NORMAL, text=texto_opcao02)
            self.opcao_3.configure(bg='cornsilk', state=NORMAL, text=texto_opcao03)
            self.opcao_4.configure(bg='cornsilk', state=NORMAL, text=texto_opcao04)

class MainWindow(Funcs):
    def __init__(self):
        self.root = root
        self.frame()
        self.montaTabelas()
        self.cadastro_paises_na_tabela()
        self.cadastro_continentes_na_tabela()
        root.mainloop()

    def frame(self):
        self.root.title("GeoQuiz")
        self.root.configure(background='lightblue')
        self.root.geometry("400x200")

        self.lbl_instrucoes = Label(self.root,
                                    text="Responda a capital do país e \nveja quantas acerta consecutivamente!",
                                    bg='lightblue', font=('Cooper Black', 12))
        self.lbl_instrucoes.place(relx=0.1, rely=.1)

        self.iniciar = Button(self.root, text='Começar', command=self.open, bg='limegreen', font=('Corbel', 12, 'bold'),
                              relief='groove', borderwidth=3)
        self.iniciar.place(relx=.3, rely=.4, relwidth=0.4)

        self.fechar = Button(self.root, text='Fechar', command=self.close, bg='lightcoral', font=('Corbel', 12, 'bold'),
                             borderwidth=3)
        self.fechar.place(relx=.3, rely=.6, relwidth=0.4)

    def open(self):
        self.root2 = Toplevel()
        self.root2.title("GeoQuiz")
        self.root2.configure(background='lightblue')
        self.root2.geometry("400x400")

        global tipo_pergunta
        tipo_pergunta = self.gerar_tipo_de_pergunta()
        print('====> tipo pergunda', tipo_pergunta)
        #self.gerar_quatro_respostas_paises()

        global texto_pergunta
        if tipo_pergunta == 'pais':
            texto_pergunta = 'Qual a capital do país: '
            self.gerar_quatro_respostas_paises()
        if tipo_pergunta == 'continente':
            texto_pergunta = 'Qual continente do país: '
            self.gerar_quatro_respostas_paises()
            self.gerar_quatro_respostas_continentes()

        self.lbl_pergunta = Label(self.root2, bg='lightblue', font=('Verdana', 12))
        self.lbl_pergunta.configure(text=texto_pergunta)
        self.lbl_pergunta.place(relx=0.05, rely=.1)

        self.lbl_pais = Label(self.root2, text=self.texto_pais_selecionado(), bg='lightblue',
                              font=('Verdana', 12, 'bold'))
        self.lbl_pais.place(relx=0.60, rely=.1)

        self.opcao_1 = Button(self.root2, text=texto_opcao01, bg='cornsilk', font=('Corbel', 12, 'bold'),
                              relief='groove',
                              borderwidth=3, command=self.validar_resposta_01)
        self.opcao_1.place(relx=.3, rely=.25, relwidth=0.4)

        self.opcao_2 = Button(self.root2, text=texto_opcao02, bg='cornsilk', font=('Corbel', 12, 'bold'),
                              relief='groove',
                              borderwidth=3, command=self.validar_resposta_02)
        self.opcao_2.place(relx=.3, rely=.40, relwidth=0.4)

        self.opcao_3 = Button(self.root2, text=texto_opcao03, bg='cornsilk', font=('Corbel', 12, 'bold'),
                              relief='groove',
                              borderwidth=3, command=self.validar_resposta_03)
        self.opcao_3.place(relx=.3, rely=.55, relwidth=0.4)

        self.opcao_4 = Button(self.root2, text=texto_opcao04, bg='cornsilk', font=('Corbel', 12, 'bold'),
                              relief='groove',
                              borderwidth=3, command=self.validar_resposta_04)
        self.opcao_4.place(relx=.3, rely=.70, relwidth=0.4)

    def close(self):
        self.root.destroy()


MainWindow()