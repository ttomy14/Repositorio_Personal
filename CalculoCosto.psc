Algoritmo CalculoCosto
    Definir unidades, precioUnitario, descuento, totalPagar, descuentoJubilado Como Real
	
    Escribir "Ingrese la cantidad de unidades compradas:"
    Leer unidades
	
    precioUnitario = 1000
	
    Si unidades > 24 Entonces
        descuento = 0.150
    Sino
        Si unidades > 12 Entonces
            descuento = 0.10
        Sino
            descuento = 0
        FinSi
    FinSi
	
    totalPagar = unidades * precioUnitario * (1 - descuento)
	
    Escribir "Ingrese 1 si es jubilado, de lo contrario ingrese 0:"
    Leer esJubilado
	
    Si esJubilado = 1 Entonces
        descuentoJubilado = 0.10
        totalPagar = totalPagar * (1 - descuentoJubilado)
    FinSi
	
    Escribir "El total a pagar es:", totalPagar
FinAlgoritmo