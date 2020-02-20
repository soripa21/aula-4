def somar(a, b):
    resultado = a + b
    return resultado

argumento_1 =  float(input('Digite o valor_1: '))

argumento_2 =  float(input('Digite o valor_2: '))

soma = somar(argumento_1, argumento_2)


if soma > 40:
    print(soma)

else:
    print('Ops, só retorno valores maiores que 40') 
    
