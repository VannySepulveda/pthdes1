import math

p= int (input("Ingrese el precio de subscripción: "))
u= int (input("Ingrese la cantidad de usuarios: "))
gt= int (input("Ingrese el gasto total: "))
utAnt= int (input("Ingrese Utilidades Anteriores: "))
util=p*u-gt
r=utAnt/util
print(f"La razon es:  {r:.2f}")
