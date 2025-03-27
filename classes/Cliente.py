from enums.Tipo_conta import TipoConta 

class Cliente:
    def __init__(self, nome, apelido, data_nascimento, saldo, tipo_conta: TipoConta, plano, estado_linha, numero_telefone, identificacao, endereco, pacotes=None):
        self.nome = nome
        self.apelido = apelido
        self.data_nascimento = data_nascimento
        self.saldo = saldo
        self.tipo_conta = tipo_conta  
        self.plano = plano
        self.estado_linha = estado_linha
        self.numero_telefone = numero_telefone
        self.identificacao = identificacao
        self.endereco = endereco
        self.pacotes = pacotes if pacotes is not None else {}

    def __str__(self):
        return (f"Cliente: {self.nome} {self.apelido}, Tipo de Conta: {self.tipo_conta.value}, "
                f"Saldo: {self.saldo}, Número: {self.numero_telefone}")
