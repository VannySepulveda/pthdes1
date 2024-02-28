import math
p= int (input("Ingrese el precio de subscripción: "))
u= int (input("Ingrese la cantidad de usuarios standar: "))
up= int (input("Ingrese la cantidad de usuarios premium: "))
gt= int (input("Ingrese el gasto total: "))
util=p*u +p*up*1.5-gt
print(f"La utilidad es:  {util} ")
