from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk


co0 = '#2e2d2b'
co1 = '#feffff'
co2 = '#4fa882'
co3 = '#38576b'
co4 = '#403d3d'
co5 = '#e06636'
co6 = '#038cfc'
co7 = '#3fbfb9'
co8 = '#263238'
co9 = '#e9edf5'
co10 = '#6e8faf'
co11 = '#f2f4f2'

janela = Tk()
janela.title("Budget")
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBaixo.grid(row=2, column=0)

# Logo
app_ = Label(frameCima, text='Budget', compound=LEFT, padx=5, relief=FLAT, anchor=NW,
             font='Verdana 20', bg=co1, fg=co4)
app_.place(x=0, y=0)

# Image
app_image = Image.open('logo.png')
app_image = app_image.resize((40, 40))
app_image = ImageTk.PhotoImage(app_image)

# FRAME TOP
app_ = Label(frameCima, image=app_image, compound=LEFT, padx=5, relief=FLAT, anchor=NW,
             font='Verdana 20', bg=co1, fg=co4)
app_.place(x=160, y=0)

app_ = Label(frameCima, width=295, padx=5, relief=FLAT, anchor=NW, font='Verdana 1', bg=co3, fg=co4)
app_.place(x=0, y=47)


# Função de Calcular
def calcular():
    rensa_mensal_valor = float(rensa_mensal.get())
    necessidades['text'] = 'R${:,.2f}'.format(0.5 * rensa_mensal_valor)
    gastos['text'] = 'R${:,.2f}'.format(0.3 * rensa_mensal_valor)
    poupanca['text'] = 'R${:,.2f}'.format(0.2 * rensa_mensal_valor)


# FRAME MEIO
app_ = Label(frameMeio, text='Qual sua renda mensal?', compound=LEFT, relief=FLAT, anchor=NW,
             font='Ivy 10', bg=co1, fg=co4)
app_.place(x=7, y=15)

rensa_mensal = Entry(frameMeio, width=10, font='Ivy 14', justify='center', relief='solid')
rensa_mensal.place(x=10, y=40)

botao_calcular = Button(frameMeio, command=calcular, text='CALCULAR', relief=RIDGE, anchor=NW,
                        font='Ivy 9', bg=co1, fg=co0)
botao_calcular.place(x=150, y=40)

# FRAME BAIXO
app_ = Label(frameBaixo, text='Seus números de 50% 30% 20%', relief=FLAT,
             width=35, anchor=NW, font='Verdana 11', bg=co3, fg=co1)
app_.place(x=0, y=0)

# NECESSIDADES
necessidades_total = Label(frameBaixo, text='Necessidades', relief=FLAT,
                     width=35, anchor=NW, font='Verdana 10', bg=co9, fg=co0)
necessidades_total.place(x=10, y=40)

necessidades = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font='Verdana 12', bg=co1, fg=co4)
necessidades.place(x=10, y=75)

# GASTOS
gastos_total = Label(frameBaixo, text='Gastos', relief=FLAT,
                     width=35, anchor=NW, font='Verdana 11', bg=co9, fg=co0)
gastos_total.place(x=10, y=115)

gastos = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font='Verdana 12', bg=co1, fg=co4)
gastos.place(x=10, y=145)

# POUPANÇA
poupanca_total = Label(frameBaixo, text='Poupanças', relief=FLAT,
                       width=35, anchor=NW, font='Verdana 10', bg=co9, fg=co0)
poupanca_total.place(x=10, y=185)

poupanca = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font='Verdana 12', bg=co1, fg=co4)
poupanca.place(x=10, y=215)

janela.mainloop()
