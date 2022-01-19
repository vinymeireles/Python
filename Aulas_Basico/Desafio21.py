print('=' * 30)
print('CURSO UDEMY: PYTHON 3 BASICO AO AVANÃ‡ADO')
print('=' * 30)
###########################################################
nome = 'Vinicius'
idade = 46
altura = 1.70
peso = 80.5
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print('{} tem {} anos, {} de altura e pesa {}Kg.'.format(nome, idade, altura, peso))
print('O IMC de {} Ã© {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.\n'.format(nome, ano_nasc))

#Ou 
print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu IMC Ã© {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')