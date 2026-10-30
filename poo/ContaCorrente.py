class ContaCorrente:
    """
    Classe que representa uma conta corrente.
    
    """   
    
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def consultar_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")

    #Sobreescrevendo métodos
    def __str__(self):
        return f"{self.saldo}"

print(ContaCorrente.__doc__)

# Exemplo de uso
conta = ContaCorrente("Ana", 100.00)
conta.consultar_saldo()
conta.depositar(50.00)
conta.sacar(30.00)
conta.consultar_saldo()


       





