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



unidades = int(input("Ingresar cantidad de unidades que desea comprar: "))
jubilado = input("Cliente jubilado: (si/no) ")

# Precio unitario de la leche
precio_unitario = 1000
costo = precio_unitario * unidades

# Aplicar descuentos por cantidad
if unidades > 12 and unidades <= 24:
    total = costo - costo * 0.1
elif unidades > 24:
    total = costo - costo * 0.15
else:
    total = costo

# Aplicar descuento adicional por ser jubilado
if jubilado.lower() == "si":
    total = total - total * 0.10

print("El total es: ", total)






