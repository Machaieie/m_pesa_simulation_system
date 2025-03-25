class M_Pesa:
    def __init__(self, saldo_mpesa=0.0, numero_conta_mpesa=None, limite_transferencia=0.0, pin_mpesa=None, status_mpesa="Ativa", servicos_ativos=None, limite_retirada=0.0):
        self.saldo_mpesa = saldo_mpesa
        self.numero_conta_mpesa = numero_conta_mpesa
        self.limite_transferencia = limite_transferencia
        self.pin_mpesa = pin_mpesa
        self.status_mpesa = status_mpesa
        self.servicos_ativos = servicos_ativos if servicos_ativos is not None else []
        self.limite_retirada = limite_retirada