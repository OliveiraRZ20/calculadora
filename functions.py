# arquivo de funçoes do codigo da calculadora V4 (main.py)

from tkinter import Button, Label, StringVar

def centralizar_janela(janela, largura: int, altura: int) -> None:
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    soma_x = ((tela_largura - largura) // 2) - 8
    soma_y = ((tela_altura - altura) // 2) - 40
    janela.geometry(f"{largura}x{altura}+{soma_x}+{soma_y}")
    # print("centralizar_janela = OK")

expressao = StringVar()
expressao.set("")

resultado = StringVar()
resultado.set("")

class Calculadora:
    def __init__(self) -> None:
        self.primeiro_digito: bool = True
        self.resultado_apertado: bool = False
        self.divisao_por_0: bool = False
        self.memoria: str = ""
        
    def digitar(self, digito: str) -> None:
        expressao_str: str = expressao.get()
        operadores: list = ["+", "-", "x", "÷",","]
        numeros: list = ["1","2","3","4","5","6","7","8","9","0"]
        if self.resultado_apertado:
            if self.divisao_por_0:
                pass
            else:
                if digito in operadores:
                    expressao.set(f"{self.memoria}{digito}")
                    self.resultado_apertado = False
        else:
            if self.primeiro_digito:
                if digito in operadores:
                    pass
                else:
                    expressao.set(f"{expressao_str}{digito}")
                    self.primeiro_digito = False
            else:
                ultimo_digito: str = expressao_str[-1]
                if ultimo_digito in operadores and digito in operadores:
                    pass
                else:
                    expressao.set(f"{expressao_str}{digito}")
        

    def fazer_calculo(self) -> None:
        expressao_str: str = expressao.get()
        operadores: list = ["+", "-", "x", "÷",","]

        if self.primeiro_digito:
            pass
        else:
            ultimo_digito: str = expressao_str[-1]
            if ultimo_digito in operadores:
                pass
            else:
                expressao_str = expressao_str.replace("x","*").replace("÷","/").replace(",",".")
                try:
                    calculo = (round(eval(expressao_str),2))
                except ZeroDivisionError:
                    resultado.set("Erro: Divisão por 0")
                    self.divisao_por_0 = True
                else:
                    resultado.set(calculo)
                    self.memoria = str(calculo)
                    # print(self.memoria)
                    expressao.set("")
                self.primeiro_digito = True
                self.resultado_apertado = True

    def clear(self) -> None:
        self.memoria = ""
        self.primeiro_digito = True
        self.resultado_apertado = False
        self.divisao_por_0 = False
        expressao.set("")
        resultado.set("")
    
    def deletar_ultimo_digito(self) -> None:
        expressao_str: str = expressao.get()
        if self.primeiro_digito:
            pass
        else:
            if len(expressao_str) == 1:
                self.primeiro_digito = True
            resultado_pos_delete = expressao_str[:-1]
            expressao.set(resultado_pos_delete)

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
        command=lambda: calculadora.fazer_calculo()
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
        command=lambda: calculadora.clear()
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