"""Formatando valores com modificadores
+:s - Texto (strings)
+:d - Inteiros (int)
+:f - NÃºmeros de ponto flutuante (float)
+:.(NÃºmero)f - Quantidade de casas decimais (float) == :.2f
+:(CARACTERE) (> ou < ou ^) (Quantidade)(Tipo - s, d ou f)
+> - Esquerda
+< - Direita
+^- Centro
+"""
num1 = 10
num2 = 3
divisao = num1 / num2
#print('{:.2f}'.format(divisao))

#preenchendo casas decimais
num3 = 1
#print(f'{num3:0<10}')

nome = 'Vinicius Meireles'
print(nome.lower()) #minusculo
print(nome.upper()) #maisculo
print(nome.title()) #somente as iniciais maisculas