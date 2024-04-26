def calcula_par_or_impar(numero):
    lista_numeros_impares = "1,3,5,7,9"
    ultimo_numero = numero[-1]

    if ultimo_numero in lista_numeros_impares:
        return "é impar"
    else:
        return "é par"

while True:
    numero_digitado = input ("Digite um número: ")
    res = calcula_par_or_impar(numero_digitado)
    print(res)