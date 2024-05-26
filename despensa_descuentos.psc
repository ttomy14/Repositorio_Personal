Algoritmo descuento_despensa
    Definir cantidad, precioUnidad, descuento, totalPagar como Real
	
    Escribir "Ingrese la cantidad de unidades compradas:"
    Leer cantidad
	
    precioUnidad = 1000
	
    Si cantidad > 24 Entonces
        descuento = 15 / 100
    Sino
        Si cantidad >= 12 y cantidad <= 24 Entonces
            descuento = 10 / 100
            descuento = 0
        FinSi
    FinSi
	
    totalPagar = cantidad * precioUnidad * (1 - descuento)
	
    Escribir "Ingrese 1 si es jubilado, de lo contrario ingrese 0:"
    Leer esJubilado
	
    Si esJubilado = 1 Entonces
        descuento = descuento + 10 / 100
        totalPagar = totalPagar * (1 - descuento)
    FinSi
	
    Escribir "El total a pagar es:", totalPagar
FinAlgoritmo