#Matheus Ribeiro dos Santos

#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def tem_duplicados(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
    return False






# Teste a sua função aqui (caso ache necessário)
lista = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
print(tem_duplicados(lista))
 










