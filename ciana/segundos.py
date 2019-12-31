""" Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, 
faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos. """

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segs_restante = segundos % 86400
horas = segs_restante // 3600 
segs_restante = segs_restante % 3600
minutos = segs_restante // 60
segs_restante_final = segs_restante % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restante_final,"segundos.")
