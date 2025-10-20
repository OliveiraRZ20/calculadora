# arquivo de funçoes do codigo da calculadora V4 (main.py)

from tkinter import Button, Label
from calculadora import Calculadora

def centralizar_janela(janela, largura: int, altura: int) -> None:
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")
    # print("centralizar_janela = OK")

calculadora = Calculadora()

def criar_botao(digito: str,frame,cor: str = "#333333",tamanho: int=5) -> None:
    botao = Button(
        frame,
        text=digito,
        width=tamanho,
        height=2,
        font=("Arial", 25),
        bg=cor,
        fg="white",
        command=lambda: calculadora.digitar(digito)
    )
    # print(f"Botão {digito} = OK")
    return botao

def criar_botao_resultado(frame) -> None:
    botao = Button(
        frame,
        text="=",
        width=5,
        height=2,
        font=("Arial", 25),
        bg="#333333",
        fg="white",
        command=lambda: calculadora.calcular()
    )
    # print(f"Botão Resultado = OK")
    return botao

def criar_botao_clear(frame) -> None:
    botao = Button(
        frame,
        text="AC",
        width=5,
        height=2,
        font=("Arial", 25),
        bg="#333333",
        fg="white",
        command=lambda: calculadora.limpar()
    )
    # print(f"Botão Clear = OK")
    return botao

def criar_label(frame,texto: str = "NULL") -> None:
    label = Label(
        frame,
        textvariable=texto,
        bg='black',
        fg='white',
        font=("Arial",40)
    )
    # print(f"Label criado!")
    return label