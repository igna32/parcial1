
def cargar_ventas(lista):
    for i in lista:
        lista[i] = lista[i - 1]
        ventas_pais = int(input(f"Ingrese las ventas del pais: "))
        lista[i + 1] += ventas_pais


    return lista









def mostrar_ventas(ventas: int, pais: str)-> str:
    print("A- Argentina")
    print("B- Brasil")
    print("C- USA")
    print("D- China")
    print("E- Colombia")
    print("F- Rusia")
    
    while True:
        pais_elegido = input("Ingrese a que pais quiere cargar ventas:")
        match pais_elegido:
            case "a"| "A":
                ventas_pais = (f"{pais} vendió: {ventas} ")
            case "b"| "B":
                ventas_pais = (f"{pais} vendió: {ventas} ")
            case "c"| "C":
                ventas_pais = (f"{pais} vendió: {ventas} ")
            case "d"| "D":
                ventas_pais = (f"{pais} vendió: {ventas} ")
            case "e"| "E":
                ventas_pais = (f"{pais} vendió: {ventas} ")
            case "f"| "F":
                ventas_pais = (f"{pais} vendió: {ventas} ")

    return ventas_pais


