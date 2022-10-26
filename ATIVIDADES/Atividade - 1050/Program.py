from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

Destino_Repository = DestinoRepository()
Destino_Repository.adicionar_destino(Destino(61, "Brasília"))
Destino_Repository.adicionar_destino(Destino(75,"feira de santana"))

print(Destino_Repository)

user_interface = InterfaceUsuario(Destino_Repository)

while True:
    entrada = user_interface.adicionar_ddd()
    if (entrada == "DDD not found!"):
        print(entrada)
        break
    else:
        print(entrada)
