'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Produto Acima de 5kg Até 5 kg
Morango 2,20 por kg 2,50 por kg
Maçã 1,50 por kg 1,80 por kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
cliente.

'''

#PEDIR MORANGO | APRESENTAR O QUANTO PEDIU
pedir_morango = float(input("Quantos kilos de morango você quer? "))
print(f'Então {pedir_morango}kg de morango')

#O IF É PARA DAR O VALOR CORRETO DE ACORDO COM O PESO, PERGUNTADO EM "pedir_morango"
if pedir_morango > 5.0:
   #AQUI SE FAZ A ATRIBUIÇÃO DO VALOR AO MORANGO, CASO SEJA MAIS QUE 5 KILOS
   valor_morango = pedir_morango * 2.2
   #QUANTO CUSTA [o f na string é para injetar variável] ex: print(f'meu nome é: {nome}')
   print(f'O morango está saindo por R${valor_morango}0')
elif pedir_morango <= 5.0:
   #AQUI SE FAZ A ATRIBUIÇÃO DO VALOR AO MORANGO, CASO SEJA MENOS OU IGUAL 5 KILOS
   valor_morango = pedir_morango * 2.5
   #QUANTO CUSTA 
   print(f'O morango está saindo por R${valor_morango}0')

#PEDIR MAÇÃ | APRESENTAR O QUANTO PEDIU E CUSTA
pedir_maca = float(input("Quantos kilos de maçã você quer? "))
print(f'Então {pedir_maca}kg de maçã')

#O IF É PARA DAR O VALOR CORRETO DE ACORDO COM O PESO, PERGUNTADO EM "pedir_maca"
if pedir_maca > 5.0:
   #AQUI SE FAZ A ATRIBUIÇÃO DO VALOR A MAÇÃ
   valor_maca = pedir_maca * 1.5
   print(f'A maçã vai estar saindo por R${valor_maca}0')
elif pedir_maca <= 5.0:
   #AQUI SE FAZ A ATRIBUIÇÃO DO VALOR A MAÇÃ
   valor_maca = pedir_maca * 1.8
   print(f'A maçã está saindo por R${valor_maca}0')

#ISSO DAQUI É PARA DAR ESPAÇO NO CONSOLE
print()

#CRITÉRIO PARA O DESCONTO         OU
if pedir_maca + pedir_morango > 8 or valor_maca + valor_morango > 25.0:
#FORMULA DO DESCONTO DE 10%
   desconto = 100/10
#VARIÁVEL QUE GUARDA O DESCONTO
   total_desconto = (valor_maca+valor_morango)/desconto
#VARIÁVEL QUE TEM O VALOR TOTAL - DESCONTO
   total = (valor_maca + valor_morango) - total_desconto
   print(f'Total a pagar: R${total}0')
#CASO NÃO HAJA DESCONTO
else:
   total = valor_maca + valor_morango
   print(f'Valor total da compra: R${total}0')
