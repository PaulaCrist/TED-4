num_macas = int(input("Digite o número de maçãs compradas: "))

if num_macas < 12:
    valor_total = num_macas * 1.30
else:
    valor_total = num_macas * 1.00

print("O valor total da compra é: R$ %.2f" % valor_total)

