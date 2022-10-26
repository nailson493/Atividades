from DestinoRepository import DestinoRepository

class InterfaceUsuario:
    def __init__(self, Destino_repository: DestinoRepository) -> None:
        self.Destino_repository = Destino_repository

    def solicitar_input_usuario(self)   -> int:
        entrada = int(input("informe o ddd: "))
        return entrada

    def adicionar_ddd(self) -> str:
        ddd = self.solicitar_input_usuario()

        if (self.Destino_repository.checar_destino(ddd) == False):
            print("Invalid code!")
            return False

        return self.Destino_repository.obter_destino_pelo_ddd(ddd)