#receita bruta x 1,65%
receita_bruta = str(input('Qual a Receita Bruta do mês anterior?  ')).replace('.','').replace(',','.')
custo_prestacao = str(input('Quais são os custos de prestação de serviço do mês anterior?  ')).replace('.','').replace(',','.')
aliquota = 1.65

resultado_1 = float(receita_bruta) * (aliquota/100)
resultado_2 = float(custo_prestacao) * (aliquota/100)
print(f'Calculo da Receita Bruta : R$ {resultado_1:.2f}')
print(f'Calculo do custo de prestação de serviço: R$ {resultado_2:.2f}')

pis = resultado_1-resultado_2

print(f' OS valor correto do PIS é: R$ {pis:.2f}')

input('Verifique se o valor está igual ao que está na darf ^')

