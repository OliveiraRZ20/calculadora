# objetivo: refazer minha calculadora antiga só que agora com mais
# conhecimento na cabeça

from tkinter import *
import sys

# criacao e ajuste da janela
win_main = Tk()
win_main.title("Calculadora-V4")
win_main.resizable(False,False)
win_main.configure(bg="black")
win_main.iconbitmap(sys.executable)

from functions import *

centralizar_janela(win_main,524,750)

# |==============================================================|
visor_expressao = Frame(win_main,bg='green')
visor_expressao.pack(side='top',anchor='nw')

label_expressao = criar_label(visor_expressao,expressao)
label_expressao.pack()


visor_resultado = Frame(win_main,bg='black')
visor_resultado.pack(side='top',anchor='se')

label_resultado = criar_label(visor_resultado,resultado)
label_resultado.pack(pady=100)
# |==============================================================|
teclado_numerico = Frame(win_main, bg='blue')
teclado_numerico.pack(side='bottom')

botao_0 = criar_botao("0",teclado_numerico,tamanho=10)
botao_0.grid(column=0,row=4,columnspan=2,sticky="We")

botao_virgula = criar_botao(",",teclado_numerico)
botao_virgula.grid(column=2,row=4)

botao_1 = criar_botao("1",teclado_numerico)
botao_1.grid(column=0,row=3)

botao_2 = criar_botao("2",teclado_numerico)
botao_2.grid(column=1,row=3)

botao_3 = criar_botao("3",teclado_numerico)
botao_3.grid(column=2,row=3)

botao_4 = criar_botao("4",teclado_numerico)
botao_4.grid(column=0,row=2)

botao_5 = criar_botao("5",teclado_numerico)
botao_5.grid(column=1,row=2)

botao_6 = criar_botao("6",teclado_numerico)
botao_6.grid(column=2,row=2)

botao_7 = criar_botao("7",teclado_numerico)
botao_7.grid(column=0,row=1)

botao_8 = criar_botao("8",teclado_numerico)
botao_8.grid(column=1,row=1)

botao_9 = criar_botao("9",teclado_numerico)
botao_9.grid(column=2,row=1)

botao_resultado = criar_botao_resultado(teclado_numerico)
botao_resultado.grid(column=4,row=4)

botao_soma = criar_botao("+",teclado_numerico,"orange")
botao_soma.grid(column=3,row=3)

botao_diferenca = criar_botao("-",teclado_numerico,"orange")
botao_diferenca.grid(column=4,row=3)

botao_multiplicacao = criar_botao("x",teclado_numerico,"orange")
botao_multiplicacao.grid(column=3,row=2)

botao_clear = criar_botao_clear(teclado_numerico)
botao_clear.grid(column=3,row=4)

botao_abre_parenteses = criar_botao("(",teclado_numerico,"#a5a5a5")
botao_abre_parenteses.grid(column=3,row=1)

botao_fecha_parenteses = criar_botao(")",teclado_numerico,"#a5a5a5")
botao_fecha_parenteses.grid(column=4,row=1)

botao_divisao = criar_botao("÷",teclado_numerico,"orange")
botao_divisao.grid(column=4,row=2)
# |==============================================================|

for i in range(10):
    win_main.bind(f"{i}", lambda Event, digito=i: calculadora.digitar(digito))

operadores = ["+", "-",","]
for i in operadores:
    win_main.bind(f"{i}", lambda Event, digito=i: calculadora.digitar(digito))

win_main.bind("*", lambda Event: calculadora.digitar("x"))
win_main.bind("/", lambda Event: calculadora.digitar("÷"))
win_main.bind(".", lambda Event: calculadora.digitar(","))
win_main.bind("<Return>", lambda Event: calculadora.fazer_calculo())
win_main.bind("<BackSpace>", lambda Event: calculadora.deletar_ultimo_digito())

# iniciar janela
win_main.mainloop()

