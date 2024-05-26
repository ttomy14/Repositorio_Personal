'''Identificar situaciones donde se utilice la estructura condicional para cada uno de estos casos:

1. Condicional parcial (solo el if) con expresión lógica simple

2. Condicional completo (if - else) con expresión lógica simple

3. Condicional parcial (solo el if) con expresión lógica compuesta (and)

4. Condicional completo (if - else) con expresión lógica compuesta (or)

5. El ejemplo comentado en clases: 

Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%.
Si compra más de 24 unidades, el descuento es del 15%.
Además posee la promoción a los jubilados. La promoción de jubilados es sumarle un 10% de descuento
(si posee otros descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.'''



cantidadLeche = int(input("Ingresar cantidad de cajas que el cliente va a comprar: "))
jubilado = int(input("Ingresar 1 si el cliente es jubilado. Cualquier otro número si no lo está: "))

precio = cantidadLeche * 1000
print(f"cantidadLeche {cantidadLeche} jubilado {jubilado}")

if (cantidadLeche <= 12 and not jubilado):
    print("cantiadadLeche <= 12 and not jubilado")
    precioTotal = precio
elif((cantidadLeche >= 12 and cantidadLeche <= 24)and not jubilado):
    print("(cantidadLeche >12 and cantidadLeche <=24) and not jubilado")
    precioTotal = precio * 0.9
elif ("cantidadLeche > 24 and not jubialdo"):
    print("cantidadLeche > 24 and not jubilado")
    preciotTotal = precio * 0.85

elif(cantidadLeche <=12 and jubilado):
    print("cantidadLeche <= 12 and jubilado")
    precioTotal = precio * 0.9
elif((cantidadLeche >= 12 and cantidadLeche <= 24) and jubilado):
    print("(cantidadLeche > 12 and cantidadLeche <= 24) and jubilado")
    precioTotal = precio * 0.8
elif(cantidadLeche > 24 and jubilado):
    print("cantidadLeche > 24 and jubilado")
    precioTotal = precio * 0.75

    print(f"El monto sin descuento es: {precio} y el precio total con el descuento incluído es: {precioTotal}")







