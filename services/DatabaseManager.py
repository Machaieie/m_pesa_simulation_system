import os

class DatabaseManager:

    path = "db"
    file_name = "account_db.txt"
    path_name = os.path.join(path, file_name)
    
    @staticmethod
    def save_customer(conta):
        if not os.path.exists(DatabaseManager.path):
            os.makedirs(DatabaseManager.path)
        with open(DatabaseManager.path_name, "a", encoding="utf-8") as file:
            file.write(f"{conta.nome},{conta.apelido},{conta.data_nascimento},{conta.identificacao},"
                       f"{conta.endereco},{conta.tipo_conta.value},{conta.plano.value},{conta.estado_linha.value},"
                       f"{conta.numero_telefone},{conta.saldo}\n")

        print(f"✅ Conta de {conta.nome} salva com sucesso!")
