def somar(i, j):
  return i + j

def subtrair(i, j):
  return i - j 

def multiplicar(i, j):
  return i * j

def dividir(i, j):
  if j == 0:
    print("escolha um divisor diferente de 0")
    return "invalido"
  return i / j


def printar_resultado(resultado):
  print(f"resultado = {resultado}")

while(True):
  print("voce deseja fazer quais das seguintes operações? ")
  print("1 (somar) ")
  print("2 (subtrair) ")
  print("3 (multiplicar)")
  print("4 (dividir)")

  escolha = input("digite 1, 2, 3 ou 4: ")
  if escolha in ('1', '2', '3', '4' ):
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    if escolha == '1':
      resultado = somar(num1, num2)
      printar_resultado(resultado)
    if escolha == '2':
      resultado = subtrair(num1, num2)
      printar_resultado(resultado)
    if escolha == '3':
      resultado = multiplicar(num1, num2)
      printar_resultado(resultado)
    if escolha == '4':
      resultado = dividir(num1, num2)
      printar_resultado(resultado)
    
  else:
    print("escolha invalida. por favor escolha 1, 2, 3 ou 4")

