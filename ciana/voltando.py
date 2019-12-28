print("voltando os estudos...")

#exibir na tela
print("Tipos de dados")

#descobrir o tipo de variável
type(10)
type("tudo bem")
type(23.2)

#divisão inteira do número
10 // 3

peso  = 84 
altura = 1.65

IMC = peso / (altura ** 2)
IMCInteiro = int(IMC)

print(" O indice de massa corporea é", IMCInteiro)

#tranformar variavel tipo (int,float) para string
imc = str(IMC)
print("",imc)

#verificar tamanho da variavel
tamanho = len(imc)
print("",tamanho)


comprimento = len(str(IMC))
print("", comprimento)

#exercicio com a função len
palavra1 = "caderno"
palavra2 = "caneta"
palavra3 = "lapis"

cad = len(palavra1)
can = len(palavra2)
lap = len(palavra3)
material = cad + can + lap
print(material)
 




