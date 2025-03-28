from classes.Cliente import Cliente
from enums.Tipo_conta import TipoConta
from enums.Plano import Plano
from enums.Estado_Conta import EstadoLinha
from services.DatabaseManager import DatabaseManager
from services.Util import Util


class Cliente_Service:

    def registar_numero():
        nome = input("Digite seu nome: ")
        apelido = input("Digite o apelido: ")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        identificacao = input("Digite o número de identificação (BI): ")
        endereco = input("Digite o endereço: ")

        tipo_conta = TipoConta.PRE_PAGO
        plano = Plano.PADRAO
        estado_linha = EstadoLinha.ATIVA
        numero_telefone = Util.numero_cliente()

        new_customer = Cliente(
            nome, apelido, data_nascimento, saldo=0, tipo_conta=tipo_conta, plano=plano,
            estado_linha=estado_linha, numero_telefone=numero_telefone, 
            identificacao=identificacao, endereco=endereco
        )

        db_manager = DatabaseManager()
        db_manager.save_customer(new_customer)


    def servicos(self):
        pass

    

    