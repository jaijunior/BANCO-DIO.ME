from abc import ABC, abstractmethod

SAQUE_MAXIMO 	= 500
LIMITE_SAQUES 	= 3

class Conta:
    def __init__(self, saldo:float,numero:int, agencia:str, cliente:Cliente, historico:Historico):
        self.__saldo = saldo
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente
        self.__historico = historico

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self):
            return self.__saldo
        
    def sacar(self, valorSaque:float):
        pass

    def nova_conta(self, cliente:Cliente, numero:int):
        pass

    def depositar(self,valorDeposito):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, saldo:float,numero:int, agencia:str, cliente:Cliente, historico:Historico, limite:float, limite_saques: int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        pass

class Cliente:
    def __init__(self, endereco:str, contas:list):
        self.__endereco = endereco
        self.__contas = contas

    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        pass

    def adicionar_conta(self, conta:Conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco:str, contas:list, cpf:str, nome:str, data_nascimento:date):
        super().__init__(endereco, contas)

class Historico:
    def adicionar_transacao(self, transacao:Transacao):
        pass

class Transacao:
    @abstractmethod
    def registrar(self, conta:Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor:floar):
        self.__valor = valor

    def registrar(self, conta:Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor:floar):
        self.__valor = valor

    def registrar(self, conta:Conta):
        pass


