print("ELIJA EL PRODUCTO DESEADO")  # MOSTRAMOS LA TABLA DE PRODUCTOS
print("")
print("PRODUCTO CODIGO")
print("")
print("LECHE............................ 3")
print("HUEVOS........................... 4")
print("ARROZ............................ 5")
print("HARINA........................... 6")
print("YOGUR............................ 7")
print("GASEOSA.......................... 8")
print("AGUA............................. 9")
print("JAMON............................ 10")
print("QUESO............................ 11")
print("TOSTADAS......................... 12")
print("")


def factura():
    ter = "a"
    # DEFINIMOS VARIABLE
    li = []  # CREAMOS UNA LISTA

    productos = {1: 0.50, 2: 0.75, 3: 2000, 4: 12500, 5: 3400, 6: 4500, 7: 45400, 8: 45000, 9: 10000, 10: 5400,
                 11: 44400, 12: 45000}  # DICCIONARIO DE PRODUCTOS
    while ter == "a":  # SI WHILE ES IGUAL A "a" CONTINUA EL BUCLE
        rol = int(input("INGRESE SU ROL (1 si es estudiante, 2 si es docente): "))
        if rol == 1:
            rolname = ("ESTUDIANTE")
        if rol == 2:
            rolname = ("DOCENTE")
        documentacion = input("iNGRESE SU NUMERO DE DOCUMENTO: ")
        codigo = int(input("INGRESE EL codigo: "))
        # PEDIMOS EL CODIGO Y LO ALMACENAMOS
        cantidad = int(input("INGRESE la cantidad: "))
        # PEDIMOS LA CANTIDAD
        ter = input("Si desea terminar presione 'S' sino 'A': ")
        # "PARA TERMINAR PRECIONE "S"
        precio_original = cantidad * (productos[codigo])
        total = cantidad * (productos[codigo]) * (productos[rol])
        # MULTIPLICAMOS LA CANTIDAD X EL VALOR DEL PRODUCTO
        li.append(total)
        # AGREGAMOS EL TOTAL A UNA LISTA

    suma = 0  # DEFINIENDO VARIABLE
    indice = 0  # DEFINIENDO VARIABLE

    while indice < len(
            li):  # TERMINAR EL BUCLE CUANDO LLEGUE A LA CANTIDAD DE PRODUCTOS QUE SE ENCUENTRAN EN LA LISTA "LI"
        suma = suma + li[indice]
        # SUMAMOS LOS ELEMENTOS DE LA LISTA
        indice = indice + 1  # SUMAMOS 1 A LA VARIABLE INDICE(CUANDO LLEGUE A LA CANTIDAD DE PRODUCTOS DE LA LISTA LI SE TERMINA EL BUCLE)
    print("El precio original es: ", precio_original)
    print("El descuento de ", rolname, " que tiene el ", rolname, documentacion,
          " obtiene con su descuento un precio total de ", suma)  # MOSTRAMOS EL TOTAL


factura()