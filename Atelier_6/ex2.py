# (X°C × 9/5) + 32 = 32°F
celciustoFahrenheit = lambda cel : (cel * 9 / 5) + 32
print(celciustoFahrenheit(25))

capit = lambda string:  string.lower().capitalize()
print(capit("pYTHON"))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impairs = list(filter(lambda x: x % 2 != 0, numeros))
print(impairs)


