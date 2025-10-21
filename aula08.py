from funcoes import soma, subtrai

# Tupla
# contato = ('João', '99999-9999', '3361-2325')

# lista_de_contatos = [('Augusto', '99999-9999'), ('João', '8545454'), ('Maria', '44545445')]
# print(lista_de_contatos)
# print(lista_de_contatos[2][1])

# Dicionários

#alterado
#altercao
endereco = {
    'rua': "teste",
    'numero': 123
}

contato = {
    'nome': 'Augusto',
    'idade': 24,
    'genero': 'M',
    'dataNascimento': '2001-03-16',
    'enderecos': [
        endereco,
        {
            'rua': 'teste 2',
            'numero': 456
        }
    ]
}

print(contato)

lista_de_contato = {
    'Augusto': '111111',
    'Maria': '22222',
    'João': '3333333',
    'José': '44444444'
}
print(lista_de_contato)
lista_de_contato['Augusto'] = "999999"
print(lista_de_contato)
lista_de_contato['Eduardo'] = "88888"

del lista_de_contato['Maria']

print(contato.get('altura', "Chave nao encontrada"))

print('Augusto' in lista_de_contato) #verifica nas chaves se existe ou não
print('999999' in lista_de_contato.values()) #verifica nos valores se existe ou não

for key in lista_de_contato:
    print(lista_de_contato[key])

pets_cadastrados = []

pet = {
    'nome': "",
    'idade': "",
    'especie': "",
    'raça': "",
    'vacinado': False,
    'dono': ""
}

# pet['nome'] = input("Digite o nome do seu pet: ")
pet['especie'] = "Gato"
pet['idade'] = 13
print(pet)

pets_cadastrados.append(pet)
print(pets_cadastrados)

resultado = soma(5, 3)
print(resultado)