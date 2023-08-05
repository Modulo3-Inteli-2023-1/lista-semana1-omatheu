#Matheus Ribeiro dos Santos

#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumutativo(lista):
    soma_cumutativa = 0
    nova_lista = []

    for i in lista:
        soma_cumutativa = soma_cumutativa + i
        nova_lista.append(soma_cumutativa)

    return nova_lista

# Teste a sua função aqui (caso ache necessário)
# tst = [1, 2, 3, 4, 5]

# print(cumutativo(tst))









