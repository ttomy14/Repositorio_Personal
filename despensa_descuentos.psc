Algoritmo Despensa
	Escribir "Ingresar cantidad de unidades que desea comprar: "
	Leer unidades
	Escribir "Cliente jubilado (si/no) "
	leer jubilado
	costo = 1000 * unidades
	Si  unidades > 12 y unidades <= 24 Entonces
		total = costo - costo * 0.1
	SiNo
		Si unidades > 24 Entonces
			total = costo - costo * 0.15
		SiNo 
			total = costo
		FinSi
	Fin Si
	
	Si jubilado == "si" Entonces
		total = total - total * 0.10
	Fin Si
	
	Escribir "El total es: ",total
			
FinAlgoritmo
