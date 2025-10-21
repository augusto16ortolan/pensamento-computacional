#Match case (documentação = https://hub.asimov.academy/tutorial/entendendo-o-match-case-em-python/)

dia_da_semana = 8

match dia_da_semana:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Opção inválida")