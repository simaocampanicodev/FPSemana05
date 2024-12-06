class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("1")
        else: 
            print("0")

    def levantar(self,valor):
        if self.saldo >= valor:
            print("1")
            self.saldo =- valor
        else:
            print("0")
    
    def exibir_saldo(self):
        print(f"{self.saldo:.2f}")
    
    def exibir_info(self):
        print(f"{self.titular} {self.saldo:.2f} {self.limite:.2f}")


conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()