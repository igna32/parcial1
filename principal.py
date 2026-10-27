from funciones import cargar_ventas, mostrar_ventas
argentina = 0
brasil = 0
usa = 0
china = 0
colombia = 0
rusia = 0
españa = 0

paises = [argentina , brasil, usa, china, colombia, rusia ]


def cargar_ventas(lista):
    for i in lista:
        lista[i] = lista[i - 1]
        ventas_pais = int(input(f"Ingrese las ventas del pais: "))
        lista[i + 1] += ventas_pais


    return lista