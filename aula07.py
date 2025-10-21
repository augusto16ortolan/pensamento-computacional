from datetime import datetime
# try:
#     print("Passou 1")
#     resultado = 10 /0
#     print("Passou 2")
# except NameError as e:
#     print("Ocorreu um erro")
# except ZeroDivisionError as e:
#     print("O valor nao pode ser dividido por zero")
# finally:
#     print("Passou 3")

# def diga_seu_some(nome):
#     print(nome)

#alteracao

# w = write = escrever, só que vai sobrescrever
# a = append = escrever, só que vai adicionar no final do arquivo
# r = read = ler, só vai poder ler o arquivo
# r+ = read and write = ler e escrever

# arquivo = open("teste.atitus", "a")
# # código;descricao;preco
# arquivo.write("1;Produto 1;10.5;" + str(datetime.now()) + "\n")
# arquivo.write("2;Produto 2;15.5" + "\n")
# arquivo.write("3;Produto 3;20.5" + "\n")
# arquivo.write("4;Produto 4;25.5" + "\n")
# arquivo.write("5;Produto 5;30.5" + "\n")
# arquivo.write("6;Produto 6;35.5" + "\n")
# arquivo.write("7;Produto 7;40.5" + "\n")
# arquivo.close()

arquivo = open("teste.atitus", "r")

linhas = arquivo.readlines()

somatorio_produtos = 0

for linha in linhas:
    print("="*20)
    print(linha)
    codigo, descricao, preco = linha.strip().split(";")
    print(codigo + "\n" + descricao + "\n" + preco)
    somatorio_produtos += float(preco)

print("Somatorio dos valores dos produtos = ", somatorio_produtos)












