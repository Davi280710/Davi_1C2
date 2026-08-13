autores: Davi Rodrigues Alves e Iago Fernando
Etec vasco antonio venchirutte
Enuciado: Leia um número inteiro positivo e exiba todos os números de 1 até esse valor.

numero = int(input("Digite um numero inteiro positivo: "))
contador = 1

if numero > 0:
    while contador <= numero:
        print(contador)
        contador += 1
else:
    print("Numero invalido. Digite um valor positivo.")
