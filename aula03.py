'''numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

print(numero1 == numero2, "Igual")
print(numero1 > numero2, "Maior")
print(numero1 < numero2, "Menor")
print(numero1 >= numero2, "Maior ou igual")
print(numero1 <= numero2, "Menor ou igual")
print(numero1 != numero2, "Diferente")
'''

'''
    idade é igual a 18
    ou
    idade é maior que 18
'''

'''
idade = 17
if (idade >= 18):
    print("É maior de idade")

    if (idade > 25):
        print("É maior de idade e maior de 25 anos")

        if (idade > 35):
            pass
else:
    print("Não é maior de idade")
'''

'''
idade = 2
if (idade >= 18):
    print("É um adulto")
elif (idade >= 14):
    print("É um adolescente")
elif (idade >= 3):
    print("É uma criança")
else:
    print("É um bebê")
'''

# def somaDoisNumeros(numero1, numero2):
#     return numero1 + numero2

# somatorio = somaDoisNumeros(15, 10)
# print(somatorio)

def soma(numero1, numero2):
    return numero1 + numero2

def imprimirIdadeNaFrase(idade, frase):
    print(f"{frase} - {idade}")


def verificarIdade(idade):
    if (idade >= 18):
        imprimirIdadeNaFrase(idade, "É um adulto")
    elif (idade >= 14):
        imprimirIdadeNaFrase(idade, "É um adolescente")
    elif (idade >= 3):
        imprimirIdadeNaFrase(idade, "É uma criança")
    else:
        imprimirIdadeNaFrase(idade, "É um bebê")

#early return = retorno antecipado
def verificarIdade2(idade):
    if (idade == 18 or idade > 18):
        imprimirIdadeNaFrase(idade, "É um adulto")
        return

    if (idade > 13 and idade < 18): 
        imprimirIdadeNaFrase(idade, "É um adolescente")
        return

    if (idade > 2 and idade < 14):
        imprimirIdadeNaFrase(idade, "É uma criança")
        return

    imprimirIdadeNaFrase(idade, "É um bebê")

numero = 40
print(numero > 50 and numero < 12 or numero == 40)

verificarIdade2(18)

# and - &&
# or - || (pipe)
# not (negação)
verificarIdade(17)

# verificarIdade(10)
# verificarIdade(15)
# verificarIdade(16)
# verificarIdade(17)
# verificarIdade(18)
# verificarIdade(1)

# resultado = soma(1, 2)
# print(soma(1, 2))


'''
Jogo de adivinhação (versão simples)

O programa escolhe um número fixo (ex.: 7).

O usuário tenta adivinhar digitando um número.

Se for igual, mostra “Parabéns, você acertou!”.

Se for maior, mostra “O número é menor”.

Se for menor, mostra “O número é maior”.

numero = 10
'''
