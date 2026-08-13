autores: Davi Rodrigues Alves e Iago Fernando
Etec vasco antonio venchirutte
Enunciado: Leia um número inteiro de 1 a 10 e exiba sua tabuada. Caso o número esteja fora do intervalo, solicite novamente até que o valor seja válido.

numero = int(input("Digite um numero de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Valor invalido. Digite novamente: "))

contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
