
#Importação das funções matemáticas
import math

#Cabeçalho da calculadora
print ("CALCULADORA DE LOGARITMO")
print ("\nInstruções aos usuários: ")

#Inicio da coleta de inteção do usuário
escolha = int(input("\nEscolha a base do logaritmo que deseja calcular:\n1 - Base e\n2 - Base 2 \n10 - Base 10\n0 - Base Outras Bases\n\nBase = "))

#No caso da escolha da base 10
if escolha == 10:
  num10 = int(input("Digite o número que deseja calcular na base 10: "))
  print("\nO resultado de", num10,"na base", escolha,"é:", math.log10(num10))
  
#No caso da escolha da base 2
elif escolha == 2:
  num2 = int(input("Digite o número que deseja calcular na base 2: "))
  print("\nO resultado de", num2,"na base", escolha,"é:", math.log2(num2))

#No caso da escolha da base e
elif escolha == 1:
  num_e = int(input("Digite o número que deseja calcular na base e: "))
  print("\nO resultado de", num_e,"na base", escolha,"é:", math.exp(num_e))
  
#No caso da escolha de outras bases != 10 ou 2
elif escolha == 0:
  base = float(input("Digite a base do logaritmo que deseja calcular: "))
  num_x = float(input("Digite o número que deseja calcular na base escolhida:"))
  print("\nO resultado de", num_x,"na base", base,"é: ", math.log(num_x,base))
  
#Caso seja digitado um número != das opções
else:
  print("Comando inválido!")