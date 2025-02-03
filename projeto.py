#Crie um programa que pede salario de uma determinada pesso e calcula valor da hora extra com forme o salorio sabendo salario / 220
salario = float(input("Digite o valor do salario: "))
hora_extra_50 = int(input("Digite quantidade horas trabalhado 50%: "))
hora_extra_100 = int(input("Digite quantidade horas trabalhado 100%: "))

#Hora extra normal
valor_hora_extra_nomal = salario / 220

#Calculando o valor da hora extra com 50% e 100%
valor_hora_extra_ciquenta_porcenta = valor_hora_extra_nomal + valor_hora_extra_nomal * 0.50 
valor_extra_cem_porcento = valor_hora_extra_nomal + valor_hora_extra_nomal * 1.00

# Calcula os totais para cada tipo de hora extra
total1 = valor_hora_extra_ciquenta_porcenta * hora_extra_50
total2 = valor_extra_cem_porcento * hora_extra_100

# Exibe apenas os valores relacionados às horas extras realizadas
if hora_extra_50 > 0: 
    print(f"O valor Total 50% é R${total1:.2f}")
if hora_extra_100 > 0:
    print(f"O valor Total 100% é R${total2:.2f}")

#Exibe o total somente se houver horas extras registradas
if hora_extra_50 > 0 or hora_extra_100 > 0:
    totalGeral = total1 + total2
    print(f"O valor Total Geral é R${totalGeral:.2f} ")
else:
    print("Nenhuma hora extra foi registrado")

#Exibe informações gerais sobre os valores das horas extras
print(f"O valor da sua hora extra normal é de R$ {valor_hora_extra_nomal:.2f}")
print(f"O valor da sua hora extra com 50% de é de R$ {valor_hora_extra_ciquenta_porcenta:.2f}")
print(f"O valor da sua hora extra com 100% de é de R$ {valor_extra_cem_porcento:.2f}")
