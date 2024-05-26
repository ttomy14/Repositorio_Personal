Algoritmo ejercicio_3
		
		Escribir "Ingresar hace cuantas semanas se dio inicio al torneo: "
		Leer inicio
		Escribir "Ingresar cantidad de partidos jugados por semana: "
		Leer partidos
		
		
		cantidad_partidos = inicio * partidos
		Escribir "Partidos jugados hasta hoy: ", cantidad_partidos
		
		Escribir "Ingresar cantidad de partidos perdidos: "
		Leer perdido
		Escribir "Ingresar cantidad de partidos empatados: "
		Leer empate
		Escribir "Ingresar cantidad de partidos ganados: "
		Leer ganado
		
		puntos1 = perdido * 0
		puntos2 = empate * 1
		puntos3 = ganado * 3
		
		total_pts = puntos1 + puntos2 + puntos3
		
		Escribir "Partidos perdidos: ", perdido
		Escribir "Partidos empatados: ", empate
		Escribir "Partidos ganados: ", ganado
		Escribir "Partidos jugados: ", cantidad_partidos
		Escribir "Cantidad total de puntos obtenidos: ", total_pts
		
FinAlgoritmo
