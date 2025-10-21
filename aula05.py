# listaVazia = [] #array ou lista ou vetor
# lista = [1 , 5, 5.5, "texto", True, [1, 2, 4]] #podemos adicionar qualquer outro tipo dentro de listas

# print(listaVazia)
# print(lista)

# listaDeNumeros = list(range(1, 51))
# listaDeNumeros2 = list(range(10))
# listaDeNumeros3 = list(range(1, 50, 3))

# print(listaDeNumeros)
# print(listaDeNumeros2)
# print(listaDeNumeros3)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista)
# lista[2] = "Rebaixamentos do Grêmio" 
# print(lista)

# lista2 = lista.copy()

# lista2[0] = "Teste"

# print(lista2)
# print(lista)

# lista = ["Banana", "Laranja", "Maçã"]

# #Métodos para inserir dados na lista
# lista.insert(0, "Melancia") #insere baseado no índice
# lista.append("Uva") #insere no final da lista
# lista.extend(["Maracujá", "Romã"]) #insere uma lista de valores no final da lista
# print(lista)

#Métodos para remover dados da lista
# lista.remove("Melancia") #Remove um valor específico, porém, obrigagoriamente, ele precisa estar na lista
# lista.pop() #(Sem passar parâmetros) remove o último dado da lista
# lista.pop(0) #remove o índice que nós passarmos
# lista.pop(1) #remove o índice que nós passarmos
# del lista[0] #remove o índice que nós passarmos
# print(lista)
# lista.clear() #devolve uma lista vazia (limpa a lista)
# print(lista)

#Métodos utilitários - não alteram o estado da lista
# lista = list(range(10, 150))
# print(len(lista)) # devolve a quantidade de dados na lista
# print(max(lista)) # devolve o maior valor da lista
# print(min(lista)) # devolve o menor valor da lista
# print(sum(lista)) # devolve a soma dos valores da listas
# print("Média: ", sum(lista) / len(lista)) # cálculo da média

#Método slicing
# lista = [10, 20, 30, 40, 50, 60, 70]
# primeiro_indice = 0
# ultimo_indice = len(lista) - 1
# indice_do_meio = int((len(lista) / 2))
# print(lista[primeiro_indice], lista[ultimo_indice], lista[indice_do_meio])
# print(lista[primeiro_indice:indice_do_meio])
# print(lista[indice_do_meio:ultimo_indice])


#Matrizes
# lista = [1, 2, 3, 4, 5]
# matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# print(matriz)
# lista[2] = "X"
# matriz[1][1] = "X"
# print(matriz)
# print(matriz[2][1])

# # #Métodos utilitários (alteram o estado da lista)
# lista = ["Laranja", "Banana", "Maçã"]
# lista.sort() #Ordena em ordem ascendente
# lista.sort(reverse=True) #Ordena em ordem decresente
# #lista.reverse() #Inverte a ordem da lista
# print(lista)

#Laços de repetição 

#FOR
lista = ["Augusto", "Maria", "João", "Luiza", "José"]

# indice = 0
# for nome in lista:
#     print(indice, nome)
#     if indice == len(lista) - 1:
#         print(nome, " é o ultimo da lista")

#     indice += 1

# for indice, nome in enumerate(lista):
#     print(indice, nome)
#     if indice == len(lista) - 1:
#         print(nome, " é o ultimo da lista")

# for indice in range(len(lista)):
#     print(lista[indice])

# for indice, nome in enumerate(lista):
#     print(indice, nome)
#     lista.append("Teste")
#     if indice == len(lista) - 1:
#         print(nome, " é o ultimo da lista")

#Exercício: separar uma lista em duas listas de pares e ímpares
# lista = list(range(1, 101))

# lista_par = []
# lista_impar = []

# for numero in lista:
#     if numero == 50:
#         lista_par.append(numero)
#         break # para todo o fluxo do for
    
#     lista_impar.append(numero)

# for numero in lista:
#     if numero % 2 == 0:
#         lista_par.append(numero)
#         continue #continua para o proximo indice a ser iterado
    
#     lista_impar.append(numero)

# print(lista_par)
# print(lista_impar)

# matriz = [["X", 2, 3],
#           [4,"X", 6],
#           [7, 8, "X"]]

# #Aninhados
# for linha in matriz:
#     print(linha)
#     for coluna in linha:
#         print(coluna)