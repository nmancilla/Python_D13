def fact(numero):
    retorno = 1
    for i in range(1,numero+1):
        retorno = retorno * i 
    return retorno

def prod(lista):
    retorno =1
    for i in lista: 
        retorno = retorno *i
    return retorno

def calcular (**kwargs):
    retorno = {}

    for key, value in kwargs.items():
        if 'fact_' in key:
            retorno.update({key:[value,fact(value)]})
        else:
            retorno.update({key:[value,prod(value)]})

    return retorno

for key, value in calcular(fact_1=4, fact_2 =6, prod_1 = {4,5.6}).items():
    if "prod" in key:
        texto = "la productoria"
    else:
        texto = "El factorial"

    print(f'{texto}de {value[0]} es {value[1]}.')