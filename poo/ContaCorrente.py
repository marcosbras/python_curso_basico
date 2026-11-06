from rich import print

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

# Mostra a documentação da classe
print('1)', ContaCorrente.__doc__)

# Mostra os atributos e métodos da classe
print('2)', ContaCorrente.__dict__)

# Mostra o módulo em que a classe está definida
print('3)', ContaCorrente.__module__)

# Mostra o nome da classe
print('4)', ContaCorrente.__name__)

# Mostra as classes base da classe
print('5)', ContaCorrente.__bases__)

# Mostra a classe do objeto
print('6)', ContaCorrente.__class__)

# Mostra a documentação do método __init__
print('7)', ContaCorrente.__init__.__doc__)

# Mostra a documentação do método depositar
print('8)', ContaCorrente.depositar.__doc__)

# Mostra a documentação do método sacar
print('9)', ContaCorrente.sacar.__doc__)

# Mostra a documentação do método consultar_saldo
print('10)', ContaCorrente.consultar_saldo.__doc__)

# Mostra a documentação do método __str__
print('11)', ContaCorrente.__str__.__doc__)

# Mostra a documentação do método __class__.__doc__
print('12)', ContaCorrente.__class__.__doc__)





# Exemplo de uso
print('[green]Infornações da conta corrente[/green] :earth_americas:')
conta = ContaCorrente("Ana", 100.00)
conta.consultar_saldo()
conta.depositar(50.00)
conta.sacar(30.00)
conta.consultar_saldo()
print('[bold green on white]Fim da execução do programa.[/] :zap:')


       





