def numero_par(numero):
    if numero % 2 == 0:
        lista_s_impar.append(numero)
lista = [15, 30, 16, 28, 19, 32, 11, 3]
lista_s_impar = []
for x in lista:
    numero_par(x)
print("lista original: {}".format (lista))
print("lista sem numeros impares: {}".format(lista_s_impar))
