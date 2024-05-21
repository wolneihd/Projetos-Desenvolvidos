from tkinter import *
from tkinter import messagebox
import random
from threading import Thread
from time import sleep


root = Tk()

class MainWindow():
    def __init__(self):
        self.root = root
        self.frame()
        self.widgets()
        self.tempo()
        root.mainloop()

    def tempo(self):
        timer_thread = Thread(target=self.timer)
        timer_thread.start()

    global respondido_em_tempo
    respondido_em_tempo = False
    def timer(self):
        global respondido_em_tempo
        sleep_duration = 3
        while sleep_duration > 0:
            print(f"you have {sleep_duration} seconds left")
            if respondido_em_tempo == False:
                self.label_tempo.configure(text=f'Tempo para acertar {sleep_duration}')
            else:
                self.label_tempo.configure(text=f'Acertou em tempo!')
            sleep(1)
            sleep_duration -= 1
        if respondido_em_tempo == False:
            self.label_tempo.configure(text=f'Não acertou em tempo!')
            messagebox.showerror('Não deu!', "Não respondeu em tempo!")
            self.tempo()
            self.widgets()
        print("timer completed")

    def frame(self):
        self.root.title("Jogo do Pega-Pega")
        self.root.configure(background='#CCFFCC')
        self.root.geometry("500x300")
        self.root.resizable(False, False)

    def widgets(self):
        global respondido_em_tempo
        self.label_tempo = Label(self.root, text=f'Tempo para acertar {0}',bg='gray',anchor='center',font=('consola',8,'bold'),background='#CCFFCC')
        self.label_tempo.place(relx=.05,rely=0.01,relwidth=.87)
        valor_y = 0.1
        valor_x = 0.05
        coordenada_aleatorio_x = random.randint(0, 8)
        coordenada_aleatorio_y = random.randint(0, 8)
        print(f'{coordenada_aleatorio_x},{coordenada_aleatorio_y}')
        for numero_x in range(0,9):
            for numero_y in range(0, 9):
                if coordenada_aleatorio_x == numero_x and coordenada_aleatorio_y == numero_y:
                    self.botao_resposta = Button(self.root, text=f'', bg='green',command=self.acertar)
                    self.botao_resposta.place(relx=valor_x, rely=valor_y, relwidth=.07)
                else:
                    self.botao_errado = Button(self.root, text=f'', bg='cornsilk',command=self.errar)
                    self.botao_errado.place(relx=valor_x, rely=valor_y, relwidth=.07)
                valor_y += .1
            valor_x += .1
            valor_y = 0.1

    def acertar(self):
        global respondido_em_tempo
        respondido_em_tempo = True
        messagebox.showinfo('acertou!',"acertou em tempo!")
        self.tempo()
        self.widgets()

    def errar(self):
        global respondido_em_tempo
        respondido_em_tempo = False
        messagebox.showerror('errou!',"errou!")
        self.tempo()
        self.widgets()

MainWindow()




