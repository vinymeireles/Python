print('=' * 30)
print('CURSO UDEMY: PYTHON 3 BASICO AO AVANÃ‡ADO')
print('=' * 30)
###########################################################
nome = 'Vinicius Meireles'
idade = 46
altura = 1.70
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)
print('{} tem {} anos de idade e seu IMC Ã©: {:.2f}\n'.format(nome, idade, imc))

#outra forma de formatar strings
print(f'{nome} tem {idade} anos de idade e seu IMC Ã©: {imc:.2f}')