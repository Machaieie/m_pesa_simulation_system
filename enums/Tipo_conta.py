from enum import Enum


class TipoConta(Enum):
    PRE_PAGO = "Pré-pago"
    POS_PAGO = "Pós-pago"
    CONTROLE = "Controle"