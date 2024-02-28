import math

radio =int (input("Ingrese el radio en Kilometros: "))
gravedad = float (input("Ingrese la constante de g: "))

radio = radio * 1000

ve = math.sqrt(2*(gravedad*radio))
print(f"LA VELOCIDAD DE ESCAPE ES: {ve:.1f} mt/seg ")