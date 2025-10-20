from tkinter import StringVar

class Calculadora:
    def __init__(self):
        self.primeiro_digito: bool = True
        self.resultado_apertado: bool = False
        self.divisao_por_zero: bool = False
        self.parenteses_aberto: bool = False
        
        self.expressao = StringVar()
        self.expressao.set("")
        self.resultado = StringVar()
        self.resultado.set("")
        self.memoria: str = ""
    
    def digitar(self, digito: str) -> None:
        if self.divisao_por_zero:
            return
        
        expressao_atual: str = self.expressao.get()
        
        if self.resultado_apertado:
            # depois de apertar o resultado, somente operadores são permitidos
            if self.check_operador(digito):
                self.expressao.set(f"{self.memoria}{digito}")
                self.resultado_apertado = False
            return

        if self.primeiro_digito:
            # como primeiro digito só é permitido números ou abre parênteses
            if self.check_numero(digito) or self.check_valor(digito, '('):
                self.expressao.set(f"{expressao_atual}{digito}")
                self.primeiro_digito = False
            return

        ultimo_digito = expressao_atual[-1]
        match self.check_tipo(ultimo_digito):
            case 'NUMERO':
                if self.check_valor(digito, '(') or (self.check_valor(digito, ')') and not self.parenteses_aberto):
                    return
            case 'OPERADOR':
                if not self.check_numero(digito) and not self.check_valor(digito, '('):
                    return
            case 'VIRGULA':
                if not self.check_numero(digito):
                    return
            case 'ABRE PARENTESES':
                if not self.check_numero(digito):
                    return
                self.parenteses_aberto = True
            case 'FECHA PARENTESES':
                if not self.check_operador(digito) and not self.parenteses_aberto:
                    return
                self.parenteses_aberto = False
        self.expressao.set(f"{expressao_atual}{digito}")
        
    def calcular(self):
        expressao_str: str = self.expressao.get()
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
                    self.resultado.set("Erro: Divisão por 0")
                    self.divisao_por_0 = True
                else:
                    self.resultado.set(calculo)
                    self.memoria = str(calculo)
                    # print(self.memoria)
                    self.expressao.set("")
                self.primeiro_digito = True
                self.resultado_apertado = True
    
    def limpar(self):
        self.memoria = ""
        self.primeiro_digito = True
        self.resultado_apertado = False
        self.divisao_por_0 = False
        self.expressao.set("")
        self.resultado.set("")
    
    def deletar(self):
        expressao_str: str = self.expressao.get()
        if self.primeiro_digito:
            pass
        else:
            if len(expressao_str) == 1:
                self.primeiro_digito = True
            resultado_pos_delete = expressao_str[:-1]
            self.expressao.set(resultado_pos_delete)
    
    @staticmethod
    def check_operador(valor: str):
        return valor in {"+", "-", "x", "÷"}
    
    @staticmethod
    def check_numero(valor: str):
        return valor in {"1","2","3","4","5","6","7","8","9","0"}

    @staticmethod
    def check_valor(valor: str, valor_alvo: str) -> bool:
        return valor == valor_alvo
    
    @staticmethod
    def check_tipo(valor: str) -> str:
        if valor in {"1","2","3","4","5","6","7","8","9","0"}:
            return 'NUMERO'
        if valor in {"+", "-", "x", "÷"}:
            return 'OPERADOR'
        if valor == ',':
            return 'VIRGULA'
        if valor == '(':
            return 'ABRE PARENTESES'
        if valor == ')':
            return 'FECHA PARENTESES'