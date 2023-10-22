 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print("saiba se um ano é ou não bisexto")
ano = int(input("insira o ano:"))

if ano % 4 == 0 and ano % 100 != 0 :
    print(f"o ano é bisexto")
else:
    print(f"o ano não é bisexto")