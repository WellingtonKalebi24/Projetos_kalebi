# importando tkinter biblioteca de interface
from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b" #black/preta
cor2 = "#feffff" #white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # cizenta
cor5 = '#FFAB40' #Orange/laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("280x320")
janela.config(bg=cor1)


# criando frames
frame_tela = Frame(janela, width=280, height=50, bg=cor3) #Primeiro Frame = quadro
frame_tela.grid(row=0,column=0)

frame_corpo = Frame(janela, width=280, height=270) #Primeiro Frame = quadro
frame_corpo.grid(row=1,column=0)

# criando botoes

b_1 = Button(frame_corpo, text="C", width=18, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=9, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=150, y=0)
b_3 = Button(frame_corpo, text="/", width=9, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #fg=cor da fonte 
b_3.place(x=220, y=0)

b_4 = Button(frame_corpo, text="7", width=8, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8", width=8, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=85, y=52)
b_6 = Button(frame_corpo, text="9", width=6, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=150, y=52)
b_7 = Button(frame_corpo, text="*", width=9, height=2,bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=220, y=52)




janela.mainloop()