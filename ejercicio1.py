#Listas ejemplo para probar la función
lista1 = [[2,2], [2,2]]
lista2 = [[2,1,3], [4,5,2], [6,6,6]]

#Función que revisa la lista 'n*n' y retorna otra lista con la cantidad de numeros unicos y la cantidad de
#numeros repetidos de la lista n*n
def return_list_check(lista):

    #listas auxiliares para numeros unicos e iguales
    unique_num_list = []
    same_num_list = []

    #contadores para la matriz a retornar
    unique_num_cont = 0
    same_num_cont = 0

    #for loops que recorren las columnas y las filas de la lista 'n*n' y agregan los numeros a las listas
    #auxiliares
    for row in lista:
        for element in row:
            if element not in unique_num_list:
                unique_num_list.append(element)
            else:
                same_num_list.append(element)

    #for loop que recorre la lista de numeros unicos y verifica si estan en la lista de numeros iguales,
    #sumando los contadores dados los casos
    for element in unique_num_list:
        if element not in same_num_list:
            unique_num_cont = unique_num_cont + 1
        else:
            same_num_cont = same_num_cont + 1
    
    #imprimiendo la lista con los contadores de numeros unicos y numeros repetidos
    print([unique_num_cont, same_num_cont])

    #retornando la lista con los contadores
    return [unique_num_cont, same_num_cont]

#Comprobando el funcionamiento de la función creada
return_list_check(lista2)