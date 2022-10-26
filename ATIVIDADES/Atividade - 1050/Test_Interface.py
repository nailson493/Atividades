from email.utils import encode_rfc2231
from pytest import MonkeyPatch

from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario


def test_input(monkeypatch: MonkeyPatch):
    # Arrange
    Destino_Repository = DestinoRepository()
    Interface_usuario = InterfaceUsuario(Destino_Repository)

    # Act
    monkeypatch.setattr("builtins.input", lambda _: "71")
    entrada = Interface_usuario.solicitar_input_usuario()

    # Assert
    assert entrada == 71
    assert type(entrada) == int


