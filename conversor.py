conversor.py
# Conversor de Celsius para Fahrenheit

def converter_celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Conversor de Temperatura")
temperatura = float(input("Informe a temperatura em Celsius: "))
resultado = converter_celsius_para_fahrenheit(temperatura)
print(f"{temperatura}°C é igual a {resultado}°F")
