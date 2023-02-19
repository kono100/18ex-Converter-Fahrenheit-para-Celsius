
'''  Faça um programa que receba uma temperatura em graus Fahrenheit, calcule e escreva o 
valor correspondente em graus Celsius.'''

temperatura = float(input('Digite a temperatura atual em Fahrenheit: '))
conversao = (temperatura-32)/1.8
print(f'A temperatura atual em Celsius é de {conversao:.1f} graus')
