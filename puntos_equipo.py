inicio = int(input("Ingresar hace cuantas semanas se dió inicio al torneo: "))
partidos = int(input("Ingresar cantidad de partidos jugados por semana: "))

cantidad_partidos = inicio * partidos
print("Partidos jugados hasta hoy: ", cantidad_partidos)

perdido = int(input("Ingresar cantidad de partidos perdidos: "))
empate = int(input("Ingresa cantidad de partidos empatados: "))
ganado = int(input("Ingresar cantidad de partidos ganados: "))

puntos1 = perdido * 0
puntos2 = empate * 1
puntos3 = ganado * 3

total_pts = puntos1 + puntos2 + puntos3

print("Partidos perdidos: ", perdido)
print("Partidos empatados: ", empate)
print("Partidos ganados: ", ganado)
print("Partidos jugados: ", cantidad_partidos)
print("Cantidad total de puntos obtenidos: ", total_pts)