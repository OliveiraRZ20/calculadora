from utils import Utils
from calculator import Calculator

def main() -> None:
    Utils.limpar_terminal()
    print("| =============================================================== |")
    print("|             Bem-vindo à Calculadora no Terminal!                |")
    print("| =============================================================== |")
    print("| Operações disponíveis:                                          |")
    print("| 1. Soma                                                         |")
    print("| 2. Subtração                                                    |")
    print("| 3. Multiplicação                                                |")
    print("| 4. Divisão                                                      |")
    print("| =============================================================== |")
    operador: int = Utils.captar_operador_validado("Digite o número da operação desejada (1-4): ")
    a: float = Utils.captar_numero_validado("Digite o primeiro número: ")
    b: float = Utils.captar_numero_validado("Digite o segundo número: ")
    resultado: float | None = Calculator.calcular(a, b, operador)
    if resultado:
        print(f"Resultado: {resultado}")
    else:
        print("- ERRO: Não foi possível realizar a operação.")

if __name__ == "__main__":
    Utils.limpar_terminal()
    while True:
        main()
        if not Utils.checar_finalizacao():
            break
