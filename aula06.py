import random

# def is_number(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False

# while True:
#     print('''
#             1 - Adicionar produto
#             2 - Listar produtos
#             3 - Remover produto
#             4 - Sair
#           ''')
#     opcao = input("Digite uma opção: ")

#     if not is_number(opcao):
#         print("Digite um número válido")
#         continue

#     opcao = int(opcao)
    
#     if opcao == 1:
#         print("Produto adicionado")
#     elif opcao == 2:
#         print("Produtos listados")
#     elif opcao == 3:
#         print("Produto excluído")
#     elif opcao == 4:
#         break
#     else:
#         print("Digite uma opção válida")


# contador = 0

# while contador <= 10:
#     print("Contador: ", contador)
#     contador += 1

# Sistema deve gerar um numero aleatorio
# Usuario deve tentar adivinhar
# Sistema deve informar se o numero informado é maior ou menor que o numero escolhido

def valida_tentativa(numero_sorteado, escolha_usuario, excessao):
    try:
        mensagem = "Informe um número: "

        if excessao:
             mensagem = "Informe um número válido: "

        escolha_usuario = int(input(mensagem))  

        if escolha_usuario > numero_sorteado:
            print("Número sorteado é menor que o número escolhido")
            contador += 1
            return True
        elif escolha_usuario < numero_sorteado:
            print("Número sorteado é maior que o número escolhido")
            contador += 1
            return True
        else:
            print("Parabéns! Você acertou!")
            return False
    except:
        return valida_tentativa(contador, numero_sorteado, escolha_usuario, True)

numero_sorteado = random.randint(1, 100)
contador = 0

print("Números de 1 a 100")
while True:
    escolha_usuario = 0

    if contador > 5:
            print("Você atingiu o número máximo de 5 tentantivas! Perdeu!")
            break

    deve_continuar = valida_tentativa(numero_sorteado, escolha_usuario, False)

    if not deve_continuar:
            break

# grade = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for linha in grade:
#     print(*linha)