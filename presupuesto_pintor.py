
altura = float(input("Ingresar altura en metros de la pared a pintar: "))
ancho = float(input("Ingresar ancho en metros de la pared a pintar: "))
costo = int(input("Mano de obra. Ingrese el monto fijo de su pintor por metro cuadrado: "))

producto = altura * ancho
presupuesto = producto * costo

print("Total metros cuadrados a pintar: ", producto)
print("PRESUPUESTO FINAL: ", presupuesto)