autores: Davi Rodrigues Alves e Iago Fernando
Etec vasco antonio venchirutte
Enunciado:Leia um número inteiro positivo e calcule a soma de todos os números pares de 1 até esse número.

  numero = int(input("Digite um numero inteiro positivo: "))

if numero > 0:
    soma = 0
    contador = 1
    
    while contador <= numero:
        if contador % 2 == 0:
            soma = soma + contador
        contador += 1
        
    print(f"Soma dos pares: {soma}")
else:
    print("Numero invalido.")
