print('=' * 30)
print('CURSO UDEMY: PYTHON 3 BASICO AO AVANÃ‡ADO')
print('=' * 30)
###########################################################
numero_inteiro = input('Digite um nÃºmero inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso nÃ£o Ã© um nÃºmero inteiro')
else:
    numero_inteiro = int(numero_inteiro)

if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} Ã© Ã­mpar')
else:
        print(f'{numero_inteiro} Ã© par')    