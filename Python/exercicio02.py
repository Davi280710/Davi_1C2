autores: Davi Rodrigues Alves e Iago Fernando
Etec vasco antonio venchirutte
Enuciado:Leia dois números inteiros e informe qual deles é o maior. Caso sejam iguais, informe que os valores são iguais.


numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

if numero1 > numero2:
 print(f"o numero {numero1} é maior")
 
elif numero1 < numero2:
  print(f"o numero {numero2} é maior")
 
else :
  print(f"os numeros são iguais")
