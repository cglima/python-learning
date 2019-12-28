#temperaturaFahrenheit = 78
temperaturaFahrenheit = input("Digite uma temperatura em Fahrenheit")
# a função input sempre devolve uma string, por isso é necessário
#definir o tipo de variável na entrada do dado

#temp = float (temperaturaFahrenheit)
temperaturaCelsius = (float(temperaturaFahrenheit) - 32) * 5 / 9

#print("A temperatura em Celsius é ", temperaturaCelsius)

# Em que situações é melhor usar o print (f) ?
print(f'A temperatura em Celsius é {temperaturaCelsius}')

temp = temperaturaCelsius 

temp >= 0 

print(f'A temperatura registrada é menor que 0: {"Sim" if temp else "Não"}')
