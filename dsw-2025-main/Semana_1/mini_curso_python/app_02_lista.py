frutas = ["maça", "banana", "laranja", "maracuja"]
print(frutas)
print(frutas[3])
frutas[1] = "abacaxi"
print(frutas)
for fruta in frutas:
    print(fruta)

frutas.remove('laranja')
print(frutas)