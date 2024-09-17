# Construir um algoritmo que leia o valor de uma compra e a quantidade de parcelas, 
# e calcule e mostre na tela o valor das parcelas. 
# Qualquer compra nesta loja terá 5% de juros para compras parceladas.


def parcela(valor, qtde):
  res = (valor + 0.05*valor)/ qtde
  return(res)

valor = float(input("Digite o valor da compra em R$: "))
qtde = int(input("Digite a quantidade de parcelas: "))
print("Valor das parcelas será: ", parcela (valor,qtde))