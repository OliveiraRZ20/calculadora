from os import system, name

class Utils:
    # Limpa o terminal dependendo do sistema operacional
    @staticmethod
    def limpar_terminal() -> None:
        system("cls" if name == "nt" else "clear")
        return None
    
    @staticmethod
    # Valida se a entrada é um número
    def validar_numero(numero: float) -> bool:
        if not numero:
            return False
        try:
            float(numero)
            return True
        except ValueError:
            return False

    @staticmethod
    # Captura um número validado do usuário
    def captar_numero_validado(mensagem: str) -> float:
        while True:
            entrada = input(mensagem)
            if Utils.validar_numero(entrada):
                return float(entrada)
            print("- ERRO: Entrada inválida. Por favor, insira um número válido.")
    
    @staticmethod
    # Valida o operador selecionado pelo usuário
    def validar_operador(operador: int) -> bool:
        if not operador:
            return False
        try:
            if int(operador) in (1, 2, 3, 4):
                return True
        except ValueError:
            return False
    
    @staticmethod
    # Captura um operador validado do usuário
    def captar_operador_validado(mensagem: str) -> int:
        while True:
            operador = input(mensagem)
            if Utils.validar_operador(operador):
                return int(operador)
            print("- ERRO: Entrada inválida. Por favor, insira um operador válido (1-4).")
    
    @staticmethod
    # Verifica se o usuário deseja finalizar a aplicação
    def checar_finalizacao() -> bool:
        resposta = input("Deseja realizar outra operação? (s/n): ").strip().lower()
        match resposta:
            case 's':
                return True
            case 'n':
                print("Obrigado por usar a calculadora! Até logo!")
                return False
            case _:
                print("- ERRO: Resposta inválida. Por favor, responda com 's' ou 'n'.")
                return Utils.checar_finalizacao()
