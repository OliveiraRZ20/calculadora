class Calculator():

    @staticmethod
    # Realiza a soma de dois números
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    # Realiza a subtração de dois números
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    # Realiza a multiplicação de dois números
    def multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    # Realiza a divisão de dois números
    def dividir(a: float, b: float) -> float | None:
        if b == 0:
            print("- ERRO: Divisão por 0 detectada!")
            return None
        return a / b

    @staticmethod
    # Calcula o resultado com base no operador selecionado
    def calcular(a: float, b: float, operador: int) -> float | None:
        match operador:
            case 1:
                return Calculator.somar(a, b)
            case 2:
                return Calculator.subtrair(a, b)
            case 3:
                return Calculator.multiplicar(a, b)
            case 4:
                return Calculator.dividir(a, b)