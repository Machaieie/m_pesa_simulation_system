from enum import Enum


class EstadoLinha(Enum):
    ATIVA = "Ativa"
    BLOQUEADA = "Bloqueada"
    EXPIRADA = "Expirada"