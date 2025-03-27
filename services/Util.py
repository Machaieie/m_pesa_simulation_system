import random

class Util:

    def numero_cliente(self):
        prefixo = random.choice(["85","84"])
        sufixo = random.randint(1000000,9999999)
        numero = f"{prefixo}{sufixo}"
        return numero
    
    