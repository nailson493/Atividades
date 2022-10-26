from Destino import Destino

class DestinoRepository:

    
            
    lista_destino: Destino = []

    def __init__(self) -> None:
        pass

    def adicionar_destino(self,lista_destino: Destino) -> None:
        self.lista_destino.append(lista_destino)

    
    def checar_destino(self, ddd: int) -> bool:
        for Destino in self.lista_destino:
            if (ddd == Destino.ddd):
                return True
        
        return False

    def obter_destino_pelo_ddd(self,ddd):
        for Destino in self.lista_destino:
            if (ddd == Destino.ddd):
                return Destino.nome_destino
        return "Ciddade n encontrada!"

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "Nome da Cidade")

        for Destino in self.lista_destino:
            menu += formatText.format(Destino.ddd, Destino.nome_destino)

        return menu
