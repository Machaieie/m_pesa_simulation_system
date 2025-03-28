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
        print("Menu YA/16-25 anos \n")
        print("1. SoPraTi")
        print("2. Chamadas e SMS")
        print("3. Super Jackpot")
        print("4. ILIMITADO(Tudo Top)")
        print("5. Megas YA")
        print("6. M-Pesa")
        print("7. Roaming/Internacional")
        print("8. Txuna")
        print("9. Entretenimento")
        print("10. Servicos")
        print("11. EN")

        while True:
            try:
                opc = int(input("Digite uma opcao: "))
            except ValueError:
                print("\n❌ Opção inválida! Digite um número.\n")
                continue
            match opc:
                case 1:
                    print("1. 10MT = 12Min+150MB+100SMS/1d")
                    print("2. 2MT = 5min/1d(TodasRedes)")
                    print("3. 7MT = 206MB/1d")
                    print("4. 4MT = 11.2min/1d(Todasredes)")
                    print("5. Mais SoPraTi")
                case 2:
                    print("Voda Jackpot")
                    print("Todas redes Jackpot")
                    print("3. Super Janckpot")
                    print("4. SoPapo (Todas Redes)")
                    print("5. Bom dia")
                    print("6. Meu Numero 1")
                    print("7. SMS")
                    print("8. Turno da Noite")
                    print("0. Voltar")
                case 3:
                    print("Dados+SMS e Minutos p/todas redes \n")
                    print("1. 10MT = 13min+200MB+100SMS/1d")
                    print("2. 20MT = 26min+400MB+100SMS/1d")
                    print("3. 50MT = 54min+1GB+250SMS/1d")
                    print("4. Mais")
                    print("0. Voltar(00. Inicio)")
               


            

        


    

    