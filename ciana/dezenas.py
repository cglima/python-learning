""" Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. """

numero = int(input("Digite um numero inteiro: "))

dezena = numero // 10
d = dezena % 10 

print(d)


