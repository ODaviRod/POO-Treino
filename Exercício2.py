#Construir um algoritmo que leia o valor de uma compra, a quantidade de parcelas e o
#percentual de juros que será aplicado, e calcule e mostre na tela o valor das parcelas.
#Utilize um método para calcular e retornar o valor das parcelas.

def parcela(valor, qtde, juros):
    res = (valor + valor*juros) / qtde
    return(res)

valor = float(input("Digite o valor da Compra em R$: "))
qtde = int(input("Digite a quantidade de parcelas: "))
juros = float(input("Digite o valor do juros em porcentagem: "))
print("O valor das parcelas será: ", parcela(valor, qtde, juros))