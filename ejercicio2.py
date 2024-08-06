#Función para recibir un numero 'n' de parte del usuario y validarlo
def user_num_input(mensaje):
    while True:
        try:
            num = int(input(mensaje))
        except:
            print('No ha ingresado un numero.')
            continue
        if num < 1000000:
            return num
        else:
            print('el numero ingresado es mayor a 10^6')
            continue

#Declaración de variable numerica para comprobar la función
num = user_num_input('Ingrese un numero menor a 10^6: ')

#Función de imprimir lista de pares que al sumarse son iguales al número ingresado en la función
def print_list(num):
    x = 1
    y = num - 1
    lista = [[x, y]]

    #while loop para rellenar la lista con los pares que al sumarse son iguales que el numero ingresado
    #en la función
    while True:
        x = x + 1
        y = y - 1
        if y < (num / 2):
            break
        lista.append([x, y])

    #Imprimiendo la lista
    print(lista)

#Llamado de la función para comprobar su funcionamiento
print_list(num)