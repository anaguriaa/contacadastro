
def cria_conta(nome, codigo, senha, saldo):
        conta = {"nome": nome, "codigo": codigo, "senha": senha, "saldo":saldo}
        return conta
def deposita (conta,valor):
        conta["saldo"] += valor

def extrato(conta):
        print("saldo é {}".format(conta["saldo"]))
