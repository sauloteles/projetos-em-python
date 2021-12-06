from tkinter import *
from tkinter import font

class Application:
    def __init__(self,master=None):
        
        self.fonte_padrao = ('Arial', '10')
        self.primeiro_container = Frame(master)
        self.primeiro_container['pady'] = 10
        self.primeiro_container.pack()

        self.segundo_container = Frame(master)
        self.segundo_container['padx'] = 20
        self.segundo_container.pack()

        self.terceiro_container = Frame(master)
        self.terceiro_container['pady'] = 20
        self.terceiro_container.pack()

        self.quarto_container = Frame(master)
        self.quarto_container['pady'] = 20
        self.quarto_container.pack()

        self.titulo = Label(self.primeiro_container,text='Decimal para binario')
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.digite = Label(self.segundo_container,text='Digite', font= self.fonte_padrao)
        self.digite.pack()

        self.entrada_digite = Entry(self.segundo_container)
        self.entrada_digite['font'] = self.fonte_padrao
        self.entrada_digite['width'] = 20
        self.entrada_digite.pack(side=LEFT)

        self.transformar = Button(self.quarto_container,text='Transformar', width=10)
        self.transformar['command'] = self.binario
        self.transformar.pack()

        self.resultado = Label(self.terceiro_container, text='Resultado',font= self.fonte_padrao)
        self.resultado.pack()

        self.mensagem = Label(self.terceiro_container,text='', font= self.fonte_padrao)
        self.mensagem.pack()
       
    
    #transformar decimal para binario
    def binario(self):	
        numero = (self.entrada_digite.get())
        numero = int(numero)

        lista = ''
        while True:
            codigo = numero % 2
            lista += str(codigo)
            numero = numero// 2
            if numero == 0:
                break
        self.mensagem['text'] = (lista[::-1])

janela = Tk()
Application(janela)
janela.geometry('250x250')
janela.mainloop()