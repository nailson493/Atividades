from Destino import Destino
from DestinoRepository import DestinoRepository



def test_adicionar_cidade():
    # Arrange
    cidade_repository = DestinoRepository()
    cidade = Destino(21, "Rio de Janeiro")

    # Act
    cidade_repository.adicionar_destino(Destino(63, "Brasília"))
    

    # Assert
    assert len(cidade_repository.lista_destino) == 1
    assert not cidade in cidade_repository.lista_destino
    assert type(cidade_repository.lista_destino) == list

def test_destino_existe():
    # Arrange
    cidade_repository = DestinoRepository()

    # Act
    cidade_repository.adicionar_destino(Destino(63, "Brasília"))
    resultOK = cidade_repository.checar_destino(63)
    resultNOK = cidade_repository.checar_destino(2)

    # Assert
    assert len(cidade_repository.lista_destino) == 2
    assert resultOK == True
    assert resultNOK == False

