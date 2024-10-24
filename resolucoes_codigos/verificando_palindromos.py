# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Digite uma palavra: ").lower()  # converte para minúsculas para comparação sem case-sensitive

palavra_invertida = palavra[::-1] # percorre a string de trás para frente. O valor -1 no passo significa que você está percorrendo a sequência na direção oposta.

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
