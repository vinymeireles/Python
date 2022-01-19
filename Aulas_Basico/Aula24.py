print('=' * 30)
print('CURSO UDEMY: PYTHON 3 BASICO AO AVANÃ‡ADO')
print('=' * 30)
###########################################################
user = ['viny', 'meireles', 'admin']
senha = ['123456', '654321', '123654']

login = input('Digite o login: ')
password = input('Digite a senha: ')

if (login in user) and (password in senha): 
    print('{}, vocÃª estÃ¡ logado no sistema!'.format(login))
else:    
    print('UsuÃ¡rio ou senha invÃ¡lidos!')