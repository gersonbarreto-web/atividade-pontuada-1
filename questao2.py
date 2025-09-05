import os 
os.system("cls")

nome = input("Digite o seu nome ")
sexo = input("Digite o seu sexo(F pra femenino e M pra mascolino )")
estado_civil= input("Digite o seu estado civil")
tempo = float(input("digite quanto tempo de casado "))

if sexo == "f" and estado_civil == "casada" :
    tempo = input ("Digite o tempo de casados ")
    print(f"{nome} esta casada ha {tempo} anos")
else:
    print("nome:" , nome, "| sexo:", sexo, "| estado civil:", estado_civil)



