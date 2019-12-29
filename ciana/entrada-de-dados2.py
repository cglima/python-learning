nomeDaMae = input ("Qual o nome da sua mãe?")
nomeDoPai = input ("Qual o nome do seu pai?")

print("Bom dia Sra.", nomeDaMae, "!! E bom dia Sr.", nomeDoPai,".")

# Conversão de um numero em horas/minutos/segundos
segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int(segundos_str)

horas = total_segs // 3600
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(f' {horas} Horas, {minutos} Minutos, {segs_restantes_final} Segundos')

