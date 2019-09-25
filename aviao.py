listacodigo = []
listanome = []
listanumerobanco = []

codigo = 0
nome = 0
numerobanco = 0

def adicionar():
    codigo = (input("Informe o código da passagem: "))
    listacodigo.append(codigo)
    nome = (input("Informe o nome do passageiro: "))
    listanome.append(nome)
    numerobanco = (input("Informe o número do banco: "))
    listanumerobanco.append(numerobanco)

def listar():
    listanumerobanco.list()