# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
