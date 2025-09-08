import os
os.system("cls")

a = float(input("Digite o número 'A'."))
b = float(input("Digite o número 'B'."))
c = float(input("Digite o número 'C'."))
soma = a + b

if soma < c:
    print("A soma'A'+'B' é menor 'C'.")

else:
    print("A soma 'A'+'B' é maior que 'C'.")