#Calcula los dias restantes para una fecha futura especifica

from datetime import datetime

fecha = input("Feccha (formato: AAAA-MM-DD): ")
fecha = datetime.strptime(fecha,"%Y-%m-%d") 


hoy = datetime.now()
dias_restantes = (fecha - hoy).days

print(f"Faltan {dias_restantes}")
print(hoy)