# https://docs.python.org/pt-br/3.13/library/ documentação
import os
import random
import datetime
import math
import emoji
from art import tprint

#Formatações de Strings
nome = "Augusto"
sobrenome = "Ortolan"
idade = 24
#print("O meu nome é " + nome + " " + sobrenome + " e eu tenho " + str(idade) + " anos")
#print("O meu nome é {} {} e eu tenho {} anos".format(nome, sobrenome, str(idade)))

#Interpolação
#print(f"O meu nome é {nome.lower()} {sobrenome.upper()} e eu tenho {str(idade)} anos")

#lower() = transforma o texto todo em minusculo
#upper() = transforma o texto todo em maiusculo
#capitalize() = transforma a primeira letra do texto em maiusculo

#Formatações de Números
valor = 123.4567
# print("O valor é {:.4f}".format(valor))

valor1 = 10
# print("O valor completo é {:05}".format(valor1))

print("Produto {:05}: {}".format(1,"Mouse"))
print("Produto {:05}: {}".format(2, "Teclado"))
print("Produto {:05}: {}".format(10, "Monitor"))

print(f"{"Refrigerante":.<30} R${10.5:>5.2f}")
print(f"{'Pastel':.<30} R${15:>5.2f}")

os.system('cls')

numero_aleatorio = random.randint(1, 100)
print(f"O número sorteado foi {numero_aleatorio}")

print(random.choice(["Augusto", "Maria", "João"]))

print(datetime.datetime.now())

print(math.sqrt(12))

print(emoji.emojize("Python é uma boa linguagem de programação :vulcan_salute: :rocket:"))

tprint("Python")