class ContaRestaurante:
    def __init__(self,codigo,nome, senha, saldo, limite,numero):
        print("Construindo obj {}".format(self))
        self.__codigo = codigo
        self.__nome = nome
        self.__senha = senha
        self.__saldo = saldo
        self.__limite = limite
        self.__numero = "3465"
    def extrato(self):
        print("O saldo é {} Do Titular {}".format(self.__saldo, self.__nome))
    def deposita(self,valor):
        self.__saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar =self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca (self,valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
         print("O Valor {} passou o limite".format(valor))

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_nome(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,limite):
        self.__limite = limite
    def numero(self):
        return self.__numero

        # e se o saldo de uma for insuficiente?
