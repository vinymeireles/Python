print('=' * 30)
print('CURSO UDEMY: PYTHON 3 BASICO AO AVANÃ‡ADO')
print('=' * 30)
###########################################################
frase = 'o rato roeu a roupa do rei de roma' #iterÃ¡vel
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qula letra deseja colocar maiÃºscula: ')
#for com string: substituindo os 'r' por 'R': InteraÃ§Ã£o
while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)